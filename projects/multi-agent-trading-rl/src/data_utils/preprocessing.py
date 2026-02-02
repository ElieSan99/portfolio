import pandas as pd
import numpy as np
import ta
from sklearn.preprocessing import StandardScaler

class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def add_indicators(self, df: pd.DataFrame) -> pd.DataFrame:
        """Adds RSI and ATR indicators to the dataframe."""
        df = df.copy()
        # RSI
        df['RSI'] = ta.momentum.RSIIndicator(df['Close'], window=14).rsi()
        # ATR
        df['ATR'] = ta.volatility.AverageTrueRange(df['High'], df['Low'], df['Close'], window=14).average_true_range()
        
        # Drop NaN values created by indicators
        df.dropna(inplace=True)
        return df

    def normalize_data(self, df: pd.DataFrame) -> np.ndarray:
        """Normalizes OHLCV and indicators."""
        features = ['Open', 'High', 'Low', 'Close', 'Volume', 'RSI', 'ATR']
        data = df[features].values
        # Simple normalization: log returns for prices, standard scaling for others
        # For simplicity in this version, we use standard scaling on all
        normalized_data = self.scaler.fit_transform(data)
        return normalized_data

    def get_observation_space_shape(self) -> int:
        return 7 # Open, High, Low, Close, Volume, RSI, ATR
