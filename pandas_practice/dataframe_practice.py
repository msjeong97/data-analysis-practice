import pandas as pd

df = pd.DataFrame([1, 2, 3])
print(repr(df))

df = pd.DataFrame([[1, 2, 3]])
print(repr(df))

# add row
df = pd.DataFrame([[5, 6, 7], [1, 3, 5]],
                  index=['r1', 'r2'],
                  columns=['c1', 'c2', 'c3'])
print(repr(df))

# add column
df = pd.DataFrame({'c1': [1, 2], 'c2': [3, 4]},
                  index=['r1', 'r2'])
print(repr(df))


# appending row, return row-appended dataframe, not change the original dataframe
df1 = pd.DataFrame([[5, 6], [1.2, 3]])
df2 = pd.DataFrame([[0,0],[9,9]])

df = df1.append(df2)
print(repr(df))

df = df1.append(df2, ignore_index=True)
print(repr(df))

# dropping row, column of dataframe
df = pd.DataFrame({'c1': [1, 2], 'c2': [3, 4],
                   'c3': [5, 6]},
                  index=['r1', 'r2'])
# Drop row r1, axis can be removed
df_drop = df.drop(labels=['r1'], axis=0)
print('{}\n'.format(df_drop))

# Drop columns c1, c3
df_drop = df.drop(labels=['c1', 'c3'], axis=1)
print('{}\n'.format(df_drop))



