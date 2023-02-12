"""Type definitions for pandas-chained-logging."""
from typing import Protocol


class LoggerProtocol(Protocol):
    """Protocol for a logger."""

    def log(self, level: int, msg: str) -> None:
        """Log a message at the given level."""
