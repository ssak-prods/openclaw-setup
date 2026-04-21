"""Demo data generator for PyZData - generates realistic sample stock data."""

from __future__ import annotations

import random
from datetime import datetime, timedelta
from typing import Dict, List

import numpy as np
import pandas as pd

from .models import Interval


class DemoDataGenerator:
    """Generates realistic demo stock data for popular Indian stocks."""
    
    # Base prices for popular stocks (approximate real values)
    BASE_PRICES: Dict[str, float] = {
        "NIFTY 50": 19500.0,
        "NIFTY BANK": 46000.0,
        "RELIANCE": 2800.0,
        "TCS": 3500.0,
        "HDFCBANK": 1650.0,
        "INFY": 1500.0,
        "ICICIBANK": 1100.0,
        "SBIN": 800.0,
        "ITC": 450.0,
        "WIPRO": 400.0,
        "BAJFINANCE": 7000.0,
        "TATAMOTORS": 1000.0,
        "HINDUNILVR": 2600.0,
        "AXISBANK": 1100.0,
        "MARUTI": 12000.0,
        "ONGC": 250.0,
        "SENSEX": 65000.0,
    }
    
    # Volatility factors for different stocks
    VOLATILITY: Dict[str, float] = {
        "NIFTY 50": 0.015,
        "NIFTY BANK": 0.020,
        "RELIANCE": 0.018,
        "TCS": 0.012,
        "HDFCBANK": 0.016,
        "INFY": 0.014,
        "ICICIBANK": 0.017,
        "SBIN": 0.022,
        "ITC": 0.015,
        "WIPRO": 0.016,
        "BAJFINANCE": 0.025,
        "TATAMOTORS": 0.028,
        "HINDUNILVR": 0.011,
        "AXISBANK": 0.018,
        "MARUTI": 0.020,
        "ONGC": 0.019,
        "SENSEX": 0.014,
    }
    
    @classmethod
    def generate_data(
        cls,
        symbol: str,
        start_date: datetime,
        end_date: datetime,
        interval: Interval,
    ) -> pd.DataFrame:
        """Generate realistic OHLCV data for the given symbol and date range."""
        
        # Get base price and volatility, or use defaults
        base_price = cls.BASE_PRICES.get(symbol, 1000.0)
        volatility = cls.VOLATILITY.get(symbol, 0.02)
        
        # Generate timestamps based on interval
        timestamps = cls._generate_timestamps(start_date, end_date, interval)
        
        # Generate price data using geometric Brownian motion
        prices = cls._generate_prices(base_price, volatility, len(timestamps))
        
        # Create OHLCV DataFrame
        data = []
        for i, (timestamp, close_price) in enumerate(zip(timestamps, prices)):
            # Generate realistic OHLC from close price
            high = close_price * (1 + random.uniform(0, volatility * 0.5))
            low = close_price * (1 - random.uniform(0, volatility * 0.5))
            open_price = close_price * (1 + random.uniform(-volatility * 0.3, volatility * 0.3))
            
            # Ensure OHLC relationships are correct
            high = max(high, open_price, close_price)
            low = min(low, open_price, close_price)
            
            # Generate volume (in millions for indices, thousands for stocks)
            if "NIFTY" in symbol or "SENSEX" in symbol:
                volume = random.randint(1000000, 5000000)  # High volume for indices
            else:
                volume = random.randint(10000, 500000)   # Regular volume for stocks
            
            data.append({
                'date': timestamp,
                'open': round(open_price, 2),
                'high': round(high, 2),
                'low': round(low, 2),
                'close': round(close_price, 2),
                'volume': volume,
            })
        
        df = pd.DataFrame(data)
        df.set_index('date', inplace=True)
        return df
    
    @classmethod
    def _generate_timestamps(
        cls, start_date: datetime, end_date: datetime, interval: Interval
    ) -> List[datetime]:
        """Generate timestamps for the given interval."""
        timestamps = []
        current = start_date
        
        # Market hours: 9:15 AM to 3:30 PM on weekdays
        market_open = current.replace(hour=9, minute=15, second=0, microsecond=0)
        market_close = current.replace(hour=15, minute=30, second=0, microsecond=0)
        
        while current <= end_date:
            # Skip weekends
            if current.weekday() >= 5:  # Saturday = 5, Sunday = 6
                current += timedelta(days=1)
                continue
            
            if interval == Interval.DAY:
                timestamps.append(current.replace(hour=15, minute=30, second=0, microsecond=0))
                current += timedelta(days=1)
            elif interval == Interval.HOUR_1:
                hour = market_open
                while hour <= market_close:
                    timestamps.append(hour)
                    hour += timedelta(hours=1)
                current += timedelta(days=1)
            elif interval == Interval.MINUTE_30:
                minute = market_open
                while minute <= market_close:
                    timestamps.append(minute)
                    minute += timedelta(minutes=30)
                current += timedelta(days=1)
            elif interval == Interval.MINUTE_15:
                minute = market_open
                while minute <= market_close:
                    timestamps.append(minute)
                    minute += timedelta(minutes=15)
                current += timedelta(days=1)
            elif interval == Interval.MINUTE_5:
                minute = market_open
                while minute <= market_close:
                    timestamps.append(minute)
                    minute += timedelta(minutes=5)
                current += timedelta(days=1)
            elif interval == Interval.MINUTE_1:
                minute = market_open
                while minute <= market_close:
                    timestamps.append(minute)
                    minute += timedelta(minutes=1)
                current += timedelta(days=1)
        
        return timestamps
    
    @classmethod
    def _generate_prices(cls, base_price: float, volatility: float, n_points: int) -> List[float]:
        """Generate price series using geometric Brownian motion."""
        prices = [base_price]
        
        for _ in range(n_points - 1):
            # Random walk with drift
            drift = 0.0001  # Small upward drift
            random_shock = np.random.normal(0, volatility)
            price_change = drift + random_shock
            
            new_price = prices[-1] * (1 + price_change)
            prices.append(max(new_price, 0.01))  # Ensure price doesn't go negative
        
        return prices
    
    @classmethod
    def get_available_instruments(cls) -> List[Dict[str, str]]:
        """Get list of available demo instruments."""
        instruments = []
        for symbol in cls.BASE_PRICES.keys():
            exchange = "NSE" if symbol != "SENSEX" else "BSE"
            instruments.append({
                "instrument_token": f"DEMO_{symbol}_{exchange}",
                "exchange_token": f"DEMO_{symbol}",
                "tradingsymbol": symbol,
                "name": symbol,
                "exchange": exchange,
                "segment": "INDICES" if "NIFTY" in symbol or "SENSEX" in symbol else "EQUITY",
            })
        return instruments
