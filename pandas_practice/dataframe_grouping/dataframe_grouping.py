import pandas as pd

df = pd.read_csv('input.csv')
print(repr(df))

# group by year, as SQL
# return pandas.core.groupby.generic.DataFrameGroupBy object
groups = df.groupby('yearID')
# name: yearID, group: dataframe
for name, group in groups:
	print('Year: {}'.format(name))
	print(repr(group))

print(repr(groups.sum()))
print(repr(groups.mean()))
print(repr(groups.get_group(2016)))

# filter on group
no_2015 = groups.filter(lambda x: x.name != 2015)
print(repr(no_2015))

# multiple groupby
groups = df.groupby(['yearID', 'teamID'])

for name, group in groups:
  print('Year, Team: {}'.format(name))
  print('{}\n'.format(group))

groups_sum = groups.sum()
print(repr(groups_sum.loc[2017,'BOS']))
