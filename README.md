# pandas-chained-logging
Stay true to pandas method chaining by using this logging accessor 

## Installation
```bash
pip install pandas-chained-logging
```

## Usage

To quickly get started use our `log` accessor with the message you want to log. This will print the message and return the dataframe.

```python
import pandas as pd
import pandas_chained_logging

df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})

(
    df
    .assign(c=lambda x: x.a + x.b)
    .log("We can log and chain!")
    .assign(d=lambda x: x.a * x.b)
    .log("We can log and chain again!")
    .log("We can get the new shape and dtypes by using a callable")
    .log(lambda df: f"!\n{df.shape=}\n{df.dtypes=}")
)
```

To use a logger instead of `print` you can configure the logger with the `configure_logger` function.

```python
import logging
import pandas as pd
import pandas_chained_logging

logger = logging.getLogger("my_logger")
pandas_chained_logging.configure_logger(logger)

df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})

(
    df
    .assign(c=lambda x: x.a + x.b)
    .log("We can log and chain!")
    .assign(d=lambda x: x.a * x.b)
    .log("We can log and chain again!")
    .log("We can get the new shape and dtypes by using a callable")
    .log(lambda df: f"!\n{df.shape=}\n{df.dtypes=}")
)
```

You can also pass your `logger` to the `log` accessor.

```python
import logging
import pandas as pd
import pandas_chained_logging

logger = logging.getLogger("my_logger")

(
    df
    .assign(c=lambda x: x.a + x.b)
    .log("We can log and chain!", logger=logger)
    .assign(d=lambda x: x.a * x.b)
    .log("We can log and chain again!", logger=logger)
    .log("We can get the new shape and dtypes by using a callable", logger=logger)
    .log(lambda df: f"!\n{df.shape=}\n{df.dtypes=}", logger=logger)
)
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

