"""Pandas logging accessor."""
from functools import partial
import logging
from typing import Any, Callable, Generic, Optional, Protocol, TypeVar, Union

import pandas as pd
from pandas_chained_logging.types import LoggerProtocol

PandasObjectType = TypeVar("PandasObjectType", bound=Union[pd.DataFrame, pd.Series])

class LoggerProtocol(Protocol):
    """Protocol for a logger."""

    def log(self, level: int, msg: str) -> None:
        """Log a message at the given level."""

class LoggingAccessor(Generic[PandasObjectType]):
    """Logging accessor base class."""
    
    logger: Optional[LoggerProtocol] = None

    def __init__(self, pandas_obj: PandasObjectType) -> None:
        """Initialize the accessor."""
        import pandas_chained_logging

        self._obj = pandas_obj

    def _resolve_message_to_log(self, msg: Union[str, Callable[[PandasObjectType], str]]) -> str:
        if isinstance(msg, str):
            resolved_message = msg
        elif callable(msg):
            resolved_message = msg(self._obj)
        else:
            raise TypeError(
                f"msg must be a string or a Callable[[PandasObjectType], str], "
                f" not {type(msg)}"
            )
        return resolved_message
    
    def _resolve_log_caller(self, logger: Optional[LoggerProtocol], msg: str, level: int) -> Callable:
        if logger is not None:
            return partial(logger.log, msg=msg, level=level)
        elif self.logger is not None:
            return partial(self.logger.log, msg=msg, level=level)
        else:
            return partial(print, msg)

    def __call__(
        self,
        msg: Union[str, Callable[[PandasObjectType], str]],
        level: int = logging.INFO,
        logger: Optional[LoggerProtocol] = None,
    ) -> Any:
        """Log a message at the given level."""
        message = self._resolve_message_to_log(msg)
        caller = self._resolve_log_caller(logger, level=level, msg=message)
        caller()
        return self._obj


    def info(self, msg: Union[str, Callable[[PandasObjectType], str]], logger: Optional[LoggerProtocol] = None) -> Any:
        """Log an info message."""
        return self(msg, level=logging.INFO, logger=logger)

    def debug(self, msg: Union[str, Callable[[PandasObjectType], str]], logger: Optional[LoggerProtocol] = None) -> Any:
        """Log a debug message."""
        return self(msg, level=logging.DEBUG, logger=logger)

    def warning(self, msg: Union[str, Callable[[PandasObjectType], str]], logger: Optional[LoggerProtocol] = None) -> Any:
        """Log a warning message."""
        return self(msg, level=logging.WARNING, logger=logger)

    def error(self, msg: Union[str, Callable[[PandasObjectType], str]], logger: Optional[LoggerProtocol] = None) -> Any:
        """Log an error message."""
        return self(msg, level=logging.ERROR, logger=logger)


@pd.api.extensions.register_dataframe_accessor("log")
class PandasDataFrameLoggingAccessor(LoggingAccessor[pd.DataFrame]):
    """A pandas dataframe logging accessor."""


@pd.api.extensions.register_series_accessor("log")
class PandasSeriesLoggingAccessor(LoggingAccessor[pd.Series]):
    """A pandas series logging accessor."""

