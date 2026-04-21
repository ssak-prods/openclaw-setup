"""Demo client for PyZData - works without Zerodha authentication."""

from __future__ import annotations

import logging
from datetime import datetime
from typing import List, Optional

import pandas as pd

from .demo_data import DemoDataGenerator
from .models import Interval

logger = logging.getLogger(__name__)


class DemoPyZData:
    """Demo version of PyZData that generates realistic sample data without authentication.
    
    This client provides all the same methods as the real PyZData client but generates
    realistic demo data instead of fetching from Zerodha's API.
    """
    
    def __init__(self, demo_mode: bool = True):
        """Initialize the demo client.
        
        Parameters
        ----------
        demo_mode : bool, default True
            Always True for demo client. Included for API compatibility.
        """
        self.demo_mode = True
        logger.info("DemoPyZData initialized - no authentication required")
    
    def get_instruments(
        self,
        exchange: Optional[str] = None,
        search: Optional[str] = None,
    ) -> pd.DataFrame:
        """Get list of available demo instruments.
        
        Parameters
        ----------
        exchange : str, optional
            Filter by exchange (NSE, BSE, etc.)
        search : str, optional
            Search term to filter instruments
            
        Returns
        -------
        pd.DataFrame
            DataFrame with instrument information
        """
        instruments = DemoDataGenerator.get_available_instruments()
        
        # Apply filters
        if exchange:
            instruments = [inst for inst in instruments if inst["exchange"] == exchange]
        
        if search:
            search_lower = search.lower()
            instruments = [
                inst for inst in instruments 
                if search_lower in inst["tradingsymbol"].lower() 
                or search_lower in inst["name"].lower()
            ]
        
        df = pd.DataFrame(instruments)
        return df
    
    def historical_data(
        self,
        instrument_token: str,
        from_date: datetime,
        to_date: datetime,
        interval: Interval,
        continuous: bool = False,
        oi: bool = False,
    ) -> pd.DataFrame:
        """Get historical OHLCV data for the given instrument.
        
        Parameters
        ----------
        instrument_token : str
            Instrument token (e.g., "DEMO_RELIANCE_NSE")
        from_date : datetime
            Start date for data
        to_date : datetime
            End date for data
        interval : Interval
            Time interval for data
        continuous : bool, default False
            Whether to include continuous data (ignored in demo mode)
        oi : bool, default False
            Whether to include open interest (ignored in demo mode)
            
        Returns
        -------
        pd.DataFrame
            Historical OHLCV data
        """
        # Extract symbol from instrument token
        if "DEMO_" in instrument_token:
            parts = instrument_token.split("_")
            if len(parts) >= 3:
                symbol = "_".join(parts[1:-1])  # Join all parts except DEMO_ and exchange
            else:
                symbol = parts[1] if len(parts) > 1 else "UNKNOWN"
        else:
            symbol = instrument_token
        
        logger.info(f"Generating demo data for {symbol} from {from_date} to {to_date}")
        
        # Generate demo data
        data = DemoDataGenerator.generate_data(symbol, from_date, to_date, interval)
        
        return data
    
    def download_historical_data(
        self,
        symbol: str,
        exchange: str,
        from_date: datetime,
        to_date: datetime,
        interval: Interval,
    ) -> pd.DataFrame:
        """Download historical data for a symbol (convenience method).
        
        Parameters
        ----------
        symbol : str
            Trading symbol (e.g., "RELIANCE")
        exchange : str
            Exchange code (e.g., "NSE")
        from_date : datetime
            Start date
        to_date : datetime
            End date
        interval : Interval
            Time interval
            
        Returns
        -------
        pd.DataFrame
            Historical OHLCV data
        """
        # Construct demo instrument token
        instrument_token = f"DEMO_{symbol}_{exchange}"
        
        return self.historical_data(
            instrument_token=instrument_token,
            from_date=from_date,
            to_date=to_date,
            interval=interval,
        )
    
    def search_instruments(self, query: str) -> pd.DataFrame:
        """Search for instruments by name or symbol.
        
        Parameters
        ----------
        query : str
            Search query
            
        Returns
        -------
        pd.DataFrame
            Matching instruments
        """
        return self.get_instruments(search=query)
    
    def get_popular_stocks(self) -> pd.DataFrame:
        """Get list of popular demo stocks.
        
        Returns
        -------
        pd.DataFrame
            Popular stocks with their details
        """
        popular_symbols = [
            "NIFTY 50", "NIFTY BANK", "RELIANCE", "TCS", "HDFCBANK",
            "INFY", "ICICIBANK", "SBIN", "ITC", "WIPRO"
        ]
        
        instruments = DemoDataGenerator.get_available_instruments()
        popular = [inst for inst in instruments if inst["tradingsymbol"] in popular_symbols]
        
        return pd.DataFrame(popular)
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        # No cleanup needed for demo client
        pass
