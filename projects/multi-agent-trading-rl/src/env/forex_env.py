import gymnasium as gym
from gymnasium import spaces
import numpy as np
import pandas as pd

class ForexEnv(gym.Env):
    metadata = {"render_modes": ["human"]}

    def __init__(self, df, initial_balance=10000, commission=0.0001, spread=0.0002, slippage=0.0001):
        super(ForexEnv, self).__init__()
        
        self.df = df.reset_index(drop=True)
        self.initial_balance = initial_balance
        self.commission = commission
        self.spread = spread
        self.slippage = slippage
        
        # Action space: 0: Hold, 1: Buy, 2: Sell
        self.action_space = spaces.Discrete(3)
        
        # Observation space: OHLCV + Indicators (7 features)
        self.observation_space = spaces.Box(
            low=-np.inf, high=np.inf, shape=(7,), dtype=np.float32
        )
        
        self.reset()

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        
        self.balance = self.initial_balance
        self.equity = self.initial_balance
        self.current_step = 0
        self.position = 0  # 0: None, 1: Long, -1: Short
        self.entry_price = 0
        self.history = []
        self.max_equity = self.initial_balance
        self.max_drawdown = 0
        
        return self._get_observation(), {}

    def _get_observation(self):
        # Return the current row of the dataframe as observation
        obs = self.df.iloc[self.current_step][['Open', 'High', 'Low', 'Close', 'Volume', 'RSI', 'ATR']].values
        return obs.astype(np.float32)

    def step(self, action):
        current_price = self.df.iloc[self.current_step]['Close']
        reward = 0
        done = False
        truncated = False
        
        # 1. Execute Action
        if action == 1: # Buy
            if self.position == 0:
                self.position = 1
                self.entry_price = current_price + self.spread + self.slippage
                self.balance -= self.initial_balance * self.commission
            elif self.position == -1: # Close Short and Buy
                pnl = (self.entry_price - current_price) * self.initial_balance # Simplified PnL
                self.balance += pnl - (self.initial_balance * self.commission)
                self.position = 1
                self.entry_price = current_price + self.spread + self.slippage
                
        elif action == 2: # Sell
            if self.position == 0:
                self.position = -1
                self.entry_price = current_price - self.spread - self.slippage
                self.balance -= self.initial_balance * self.commission
            elif self.position == 1: # Close Long and Sell
                pnl = (current_price - self.entry_price) * self.initial_balance
                self.balance += pnl - (self.initial_balance * self.commission)
                self.position = -1
                self.entry_price = current_price - self.spread - self.slippage

        # 2. Update Equity and Drawdown
        if self.position == 1:
            self.equity = self.balance + (current_price - self.entry_price) * self.initial_balance
        elif self.position == -1:
            self.equity = self.balance + (self.entry_price - current_price) * self.initial_balance
        else:
            self.equity = self.balance
            
        self.max_equity = max(self.max_equity, self.equity)
        drawdown = (self.max_equity - self.equity) / self.max_equity
        self.max_drawdown = max(self.max_drawdown, drawdown)
        
        # 3. Calculate Reward
        reward = self._calculate_reward(drawdown)
        
        # 4. Advance Step
        self.current_step += 1
        if self.current_step >= len(self.df) - 1:
            done = True
            
        if self.equity <= self.initial_balance * 0.5: # 50% loss stop
            done = True
            reward -= 10 # Heavy penalty for blowing account
            
        return self._get_observation(), reward, done, truncated, {"equity": self.equity, "drawdown": self.max_drawdown}

    def _calculate_reward(self, current_drawdown):
        # Reward = Change in Equity - Penalty for Drawdown
        # For Sortino, we would need a window of returns, but for step-wise RL:
        # We use a simple proxy: profit minus a scaled drawdown penalty
        step_reward = (self.equity - self.initial_balance) / self.initial_balance
        
        # Penalty for drawdown
        drawdown_penalty = current_drawdown * 2.0
        
        return step_reward - drawdown_penalty
