import pandas as pd

# read csv to df
# name is used as a row index id
df = pd.read_csv('data.csv', index_col='name')
print(repr(df))

# integer row index id
df = pd.read_csv('data.csv')
print(repr(df))


# add new row
df2 = pd.DataFrame([['alli', 22, '1B']], columns=['name', 'HR', 'pos'])
df = df.append(df2, ignore_index=True)
print(repr(df))

# write df to csv, if index=False, no index (e.g. 0, 1, 2) added
df.to_csv('added_data.csv', index=False)


