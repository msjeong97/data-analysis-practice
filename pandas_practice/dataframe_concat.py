import pandas as pd

df1 = pd.DataFrame({'c1':[1,2], 'c2':[3,4]}, index=['r1','r2'])
df2 = pd.DataFrame({'c1':[5,6], 'c2':[7,8]}, index=['r1','r2'])
df3 = pd.DataFrame({'c1':[5,6], 'c2':[7,8]})

# concat: outer join using all rows or all columns(axis=1)
# merge:  inner join using all common columns

# concat to new row
concat = pd.concat([df1, df2])
print(repr(concat))

#concat to new column
concat = pd.concat([df1, df2], axis=1)
print(repr(concat))

concat = pd.concat([df1, df3])
print(repr(concat))

# return 4X4 array, axis=1 -> concat to column, but no matched row index
concat = pd.concat([df1, df3], axis=1)
print(repr(concat))

# return 3X4 array, beacuse only 'r1' matched
df2 = pd.DataFrame({'c1':[5,6], 'c2':[7,8]}, index=['r1','r3'])
concat = pd.concat([df1, df2], axis=1)
print(repr(concat))

#merge dataframes
mlb_df1 = pd.DataFrame({'name': ['john doe', 'al smith', 'sam black', 'john doe'],
                        'pos': ['1B', 'C', 'P', '2B'],
                        'year': [2000, 2004, 2008, 2003]})
mlb_df2 = pd.DataFrame({'name': ['john doe', 'al smith', 'jack lee'],
                        'year': [2000, 2004, 2012],
                        'rbi': [80, 100, 12]})

# joins two dataframe using all common column labels
mlb_merged = pd.merge([mlb_df1, mlb_df2])
print(repr(mlb_merged))
