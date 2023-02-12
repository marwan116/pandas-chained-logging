"""pandas_chained_logging: A pandas extension to log chained operations."""
import logging
from typing import Optional

from .types import LoggerProtocol
from .accessor import PandasDataFrameLoggingAccessor, PandasSeriesLoggingAccessor

def configure_logging(logger: Optional[LoggerProtocol] = None) -> None:
    """Configure pandas_chained_logging to use the given logger.

    Args:
        logger: The logger to use. If None, the root logger will be used.

    """
    if logger is None:
        logger = logging.getLogger()

    PandasDataFrameLoggingAccessor.logger = logger
    PandasSeriesLoggingAccessor.logger = logger