import pandas as pd
import numpy as np


series = pd.Series(5)
print(repr(series))

series = pd.Series([1, 2, 3])
print(repr(series))

series = pd.Series([1, 2, 3], dtype=np.float32)
print(repr(series))

series = pd.Series([[1, 2], [3, 4]])
print(repr(series))

series = pd.Series({'a': 1, 'b': 2, 'c':3})
print(repr(series))

series = pd.Series([1, 3, 5])
series1 = series * [0.5, 0.5, 0.2]
print(repr(series1))
series2 = series * series1
print(repr(series2))
