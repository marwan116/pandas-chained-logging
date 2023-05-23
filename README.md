# pandas-chained-logging
Stay true to pandas method chaining by using this logging accessor 

## Installation
```bash
pip install pandas-chained-logging
```

## Usage

To quickly get started use our `log` accessor with the message you want to log. This will print the message and return the dataframe.

```python
In [1]: import pandas as pd
   ...: import pandas_chained_logging
   ...: 
   ...: df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
   ...: 
   ...: (
   ...:     df
   ...:     .assign(c=lambda x: x.a + x.b)
   ...:     .log("We can log and chain!")
   ...:     .assign(d=lambda x: x.a * x.b)
   ...:     .log("We can log and chain again!")
   ...:     .log("We can get the new shape and dtypes by using a callable")
   ...:     .log(lambda df: f"!\n{df.shape=}\n{df.dtypes=}")
   ...: )
We can log and chain!
We can log and chain again!
We can get the new shape and dtypes by using a callable
!
df.shape=(3, 4)
df.dtypes=a    int64
b    int64
c    int64
d    int64
dtype: object
Out[1]: 
   a  b  c   d
0  1  4  5   4
1  2  5  7  10
2  3  6  9  18
```

To use a logger instead of `print` you can configure the logger with the `configure_logger` function.

```python
In [1]: import logging
   ...: import pandas as pd
   ...: import pandas_chained_logging
   ...: 
   ...: logger = logging.getLogger("my_logger")
   ...: sh = logging.StreamHandler()
   ...: formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
   ...: sh.setFormatter(formatter)
   ...: logger.addHandler(sh)
   ...: logger.setLevel("INFO")
   ...: pandas_chained_logging.configure_logger(logger)
   ...: 
   ...: df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
   ...: 
   ...: (
   ...:     df
   ...:     .assign(c=lambda x: x.a + x.b)
   ...:     .log("We can log and chain!")
   ...:     .assign(d=lambda x: x.a * x.b)
   ...:     .log("We can log and chain again!")
   ...:     .log("We can get the new shape and dtypes by using a callable")
   ...:     .log(lambda df: f"!\n{df.shape=}\n{df.dtypes=}")
   ...: )
2023-05-23 08:45:28,923 - my_logger - INFO - We can log and chain!
2023-05-23 08:45:28,925 - my_logger - INFO - We can log and chain again!
2023-05-23 08:45:28,925 - my_logger - INFO - We can get the new shape and dtypes by using a callable
2023-05-23 08:45:28,925 - my_logger - INFO - !
df.shape=(3, 4)
df.dtypes=a    int64
b    int64
c    int64
d    int64
dtype: object
Out[1]: 
   a  b  c   d
0  1  4  5   4
1  2  5  7  10
2  3  6  9  18
```

You can also pass your `logger` to the `log` accessor.

```python
In [1]: import logging
   ...: import pandas as pd
   ...: import pandas_chained_logging
   ...: 
   ...: logger = logging.getLogger("my_logger")
   ...: sh = logging.StreamHandler()
   ...: formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
   ...: sh.setFormatter(formatter)
   ...: logger.addHandler(sh)
   ...: logger.setLevel("INFO")
   ...: 
   ...: df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
   ...: 
   ...: (
   ...:     df
   ...:     .assign(c=lambda x: x.a + x.b)
   ...:     .log("We can log and chain!", logger=logger)
   ...:     .assign(d=lambda x: x.a * x.b)
   ...:     .log("We can log and chain again!", logger=logger)
   ...:     .log("We can get the new shape and dtypes by using a callable")
   ...:     .log(lambda df: f"!\n{df.shape=}\n{df.dtypes=}", logger=logger)
   ...: )
2023-05-23 08:46:46,391 - my_logger - INFO - We can log and chain!
2023-05-23 08:46:46,393 - my_logger - INFO - We can log and chain again!
We can get the new shape and dtypes by using a callable
2023-05-23 08:46:46,394 - my_logger - INFO - !
df.shape=(3, 4)
df.dtypes=a    int64
b    int64
c    int64
d    int64
dtype: object
Out[1]: 
   a  b  c   d
0  1  4  5   4
1  2  5  7  10
2  3  6  9  18
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

