"""Test the logging accessor."""
import logging
from unittest.mock import MagicMock
import pandas as pd
import pandas_chained_logging

def test_dataframe_logging_accessor_does_not_mutate_dataframe():
    """Test the dataframe logging accessor."""
    df = pd.DataFrame({"a": [1, 2, 3]})

    def add_column(df):
        df["b"] = df["a"] + 1
        return df

    out = (
        df.log("Hello")
        .pipe(add_column)
        .log(lambda df: f"{df.shape}")
        .log.info("Hello")
        .log.info(lambda df: f"{df.shape}")
        .log.debug("Hello")
        .log.debug(lambda df: f"{df.shape}")
        .log.warning("Hello")
        .log.warning(lambda df: f"{df.shape}")
        .log.error("Hello")
        .log.error(lambda df: f"{df.shape}")
    )
    df_target = pd.DataFrame({"a": [1, 2, 3], "b": [2, 3, 4]})
    pd.testing.assert_frame_equal(out, df_target)



def test_series_logging_accessor_does_not_mutate_series():
    """Test the series logging accessor."""
    s = pd.Series([1, 2, 3])

    def add_one(s):
        return s + 1

    out = (
        s.log("Hello")
        .pipe(add_one)
        .log(lambda s: f"{s.shape}")
        .log.info("Hello")
        .log.info(lambda s: f"{s.shape}")
        .log.debug("Hello")
        .log.debug(lambda s: f"{s.shape}")
        .log.warning("Hello")
        .log.warning(lambda s: f"{s.shape}")
        .log.error("Hello")
        .log.error(lambda s: f"{s.shape}")
    )
    s_target = pd.Series([2, 3, 4])
    pd.testing.assert_series_equal(out, s_target)


def test_dataframe_logging_accessor_prints_to_stdout_by_default(capsys):
    """Test the logging accessor prints to stdout."""
    df = pd.DataFrame({"a": [1, 2, 3]})
    df.log("Hello")
    captured = capsys.readouterr()
    assert captured.out == "Hello\n"

def test_series_logging_accessor_prints_to_stdout_by_default(capsys):
    s = pd.Series([1, 2, 3])
    s.log("Hello")
    captured = capsys.readouterr()
    assert captured.out == "Hello\n"

def test_dataframe_logging_accessor_prints_to_logger_if_specified():
    """Test the logging accessor prints to a logger."""
    df = pd.DataFrame({"a": [1, 2, 3]})
    logger = MagicMock()
    df.log("Hello", logger=logger)
    assert logger.log.call_count == 1
    assert logger.log.call_args[1]["msg"] == "Hello"
    assert logger.log.call_args[1]["level"] == logging.INFO

    df.log.info("Hello", logger=logger)
    assert logger.log.call_count == 2
    assert logger.log.call_args[1]["msg"] == "Hello"
    assert logger.log.call_args[1]["level"] == logging.INFO

    df.log.debug("Hello", logger=logger)
    assert logger.log.call_count == 3
    assert logger.log.call_args[1]["msg"] == "Hello"
    assert logger.log.call_args[1]["level"] == logging.DEBUG

    df.log.warning("Hello", logger=logger)
    assert logger.log.call_count == 4
    assert logger.log.call_args[1]["msg"] == "Hello"
    assert logger.log.call_args[1]["level"] == logging.WARNING

    df.log.error("Hello", logger=logger)
    assert logger.log.call_count == 5
    assert logger.log.call_args[1]["msg"] == "Hello"
    assert logger.log.call_args[1]["level"] == logging.ERROR


def test_series_logging_accessor_prints_to_logger_if_specified():
    s = pd.Series([1, 2, 3])
    logger = MagicMock()
    
    s.log("Hello", logger=logger)
    assert logger.log.call_count == 1
    assert logger.log.call_args[1]["msg"] == "Hello"
    assert logger.log.call_args[1]["level"] == logging.INFO

    s.log.info("Hello", logger=logger)
    assert logger.log.call_count == 2
    assert logger.log.call_args[1]["msg"] == "Hello"
    assert logger.log.call_args[1]["level"] == logging.INFO

    s.log.debug("Hello", logger=logger)
    assert logger.log.call_count == 3
    assert logger.log.call_args[1]["msg"] == "Hello"
    assert logger.log.call_args[1]["level"] == logging.DEBUG

    s.log.warning("Hello", logger=logger)
    assert logger.log.call_count == 4
    assert logger.log.call_args[1]["msg"] == "Hello"

    s.log.error("Hello", logger=logger)
    assert logger.log.call_count == 5
    assert logger.log.call_args[1]["msg"] == "Hello"
    assert logger.log.call_args[1]["level"] == logging.ERROR



def test_can_configure_logger_with_logging_config_dict():
    """Test the logging accessor prints to a logger."""
    df = pd.DataFrame({"a": [1, 2, 3]})
    logger = MagicMock()

    pandas_chained_logging.configure_logging(logger)
    df.log("Hello")
    assert logger.log.call_count == 1
    assert logger.log.call_args[1]["msg"] == "Hello"
    assert logger.log.call_args[1]["level"] == logging.INFO

