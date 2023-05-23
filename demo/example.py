"""Example of using pandas_chained_logging."""
# NOTE: pandas_chained_logging needs to be imported to register the accessor
# place this import in your main __init__.py file
import pandas_chained_logging 
import logging
import pandas as pd

# ----------------------------------------------------------------  
# Example 1: Introducing print statements in a chain of operations
# ----------------------------------------------------------------
df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})

(
    df.log("Adding a `c` column")
    .assign(c=lambda x: x.a + x.b)
    .log(lambda df: f"Done!\n{df.shape=}\n{df.dtypes=}")
)

# ----------------------------------------------------------------
### Example 2: Using a logger
# ----------------------------------------------------------------

# Create your logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# delegate your logger to chained logging
(
    df.log.info("Adding a `c` column", logger=logger)
    .assign(c=lambda x: x.a + x.b)
    .log.debug(lambda df: f"Done!\n{df.shape=}\n{df.dtypes=}", logger=logger)
)


# ----------------------------------------------------------------
### Example 3: Configuring a logger once for all chained logging
# ----------------------------------------------------------------

pandas_chained_logging.configure_logger(logger=logger)

(
    df.log.info("Adding a `c` column")
    .assign(c=lambda x: x.a + x.b)
    .log.debug(lambda df: f"Done!\n{df.shape=}\n{df.dtypes=}")
)
