import sys
import os
import pandas as pd
import numpy as np

# Add src to path
sys.path.append(os.path.join(os.getcwd(), 'src'))

from env.forex_env import ForexEnv
from data_utils.preprocessing import DataPreprocessor
from stable_baselines3.common.env_checker import check_env

def run_env_verification():
    print("=== Starting Forex RL Environment Verification ===\n")
    
    # 1. Create dummy data
    data = {
        'Open': np.linspace(1.1000, 1.1100, 100),
        'High': np.linspace(1.1010, 1.1110, 100),
        'Low': np.linspace(1.0990, 1.1090, 100),
        'Close': np.linspace(1.1005, 1.1105, 100),
        'Volume': np.random.randint(100, 1000, 100)
    }
    df = pd.DataFrame(data)
    
    # 2. Preprocess
    preprocessor = DataPreprocessor()
    df = preprocessor.add_indicators(df)
    
    # 3. Initialize Env
    env = ForexEnv(df)
    
    # 4. Check compatibility with Stable Baselines3
    print("Checking environment compatibility...")
    try:
        check_env(env)
        print("Result: Environment is compatible with Stable Baselines3!\n")
    except Exception as e:
        print(f"Result: Compatibility check failed: {e}\n")
        return

    # 5. Run a few steps with random actions
    print("Running random agent simulation...")
    obs, _ = env.reset()
    for i in range(5):
        action = env.action_space.sample()
        obs, reward, done, truncated, info = env.step(action)
        print(f"Step {i+1}: Action={action}, Reward={reward:.4f}, Equity={info['equity']:.2f}, Drawdown={info['drawdown']:.4f}")
        if done:
            break
            
    print("\n=== Verification Complete ===")

if __name__ == "__main__":
    run_env_verification()
