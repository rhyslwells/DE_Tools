import pandas as pd

# Merge
df1 = pd.DataFrame({'key': ['A', 'B'], 'value': [1, 2]})
df1
df2 = pd.DataFrame({'key': ['A', 'B'], 'value': [3, 4]})
merged_df = pd.merge(df1, df2, on='key')
merged_df

# Concat
concat_df = pd.concat([df1, df2])
concat_df

# Join
df1.set_index('key', inplace=True)
df2.set_index('key', inplace=True)
joined_df = df1.join(df2, lsuffix='_left', rsuffix='_right')
joined_df

df = pd.DataFrame({'category': ['A', 'B', 'A'], 'value': [10, 20, 30]})
df
grouped_df = df.groupby('category').sum()
grouped_df

df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['first', 'second'])
df
stacked_df = df.stack()
stacked_df

unstacked_df = stacked_df.unstack()
unstacked_df

df = pd.DataFrame({'A': ['foo', 'foo', 'bar'], 'B': ['one', 'two', 'one'], 'C': [1, 2, 3]})
df
pivot_table = df.pivot_table(values='C', index='A', columns='B', aggfunc='sum')
pivot_table

date_rng = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')
time_series_df = pd.DataFrame(date_rng, columns=['date'])
time_series_df['data'] = range(len(time_series_df))

df = pd.DataFrame({'A': [3, 1, 2]})
sorted_df = df.sort_values(by='A')