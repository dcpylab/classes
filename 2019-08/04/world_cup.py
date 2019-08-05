import pandas as pd

path = "https://projects.fivethirtyeight.com/soccer-api/international/2018/wc_matches.csv"

# By convention DataFrames are named `df`
df = pd.read_csv(path)

# Explore
df.head()
df.tail()
df.info()
df.describe()

# Accessing columns
df.columns
columns = df.columns.tolist()

# Single column
df['score1']
df.score1

# Multiple columns
df[['score1','score2']]

# Accessing rows
df.loc[0]

# Creating a new column with single value
df['sport'] = "Soccer"

# Creating a new column from other column
df['sport_upper'] = df.sport.str.upper()
df['score_sum'] = df.score1 + df.score2

# Group by with aggregation function applied to entire dataset
df.groupby('date').mean().sort_values('date')

# Group by with aggregation function applied to single column
df.groupby('date')['score1'].sum().sort_values(ascending=False)