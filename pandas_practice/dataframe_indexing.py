import pandas as pd

# when indexing into a dataframe, dataframe can be treated as a dictionary of series objects.
# each column is a series object
df = pd.DataFrame({'c1': [1, 2], 'c2': [3, 4],
                   'c3': [5, 6]}, index=['r1', 'r2'])
col1 = df['c1']
print(repr(col1))

col13 = df[['c1', 'c3']]
print(repr(col13))

df1 = pd.DataFrame([[7, 8, 9]], columns=['c1','c2','c3'], index=['r3'])
df = df.append(df1)

# 0~1 rows
first_two_rows = df[0:2]
print(repr(first_two_rows))

# 1~2 rows
last_two_rows = df['r2':'r3']
print(repr(last_two_rows))

# 0 row
first_row = df[0:1]
print(repr(first_row))

# error, only column id can be directly accessed
# df['r1']

# iloc - access single row as a series, using integer idx
first_row_as_series = df.iloc[0]
print(repr(first_row_as_series))

first_two_rows = df.iloc[[0,1]]
print(repr(first_two_rows))

# loc - access single rows using index (not integer)
first_row_as_series = df.loc['r1']
print(repr(first_row_as_series))

bool_list = [False, True, True]
last_two_rows = df.loc[bool_list]
print(repr(last_two_rows))

# change value
df.loc[['r1', 'r2'], ['c1', 'c3']] = 0
print(repr(df))
