import numpy as np
import pandas as pd

#Task 1: Create a Series with a list of values
s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)

#Task 2:  Create a DataFrame with a NumPy array and a datetime index
dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
# print(df)
#Task 3: Create a DataFrame from a dictionary
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)

# View the top and bottom rows of the DataFrame
df.head()
df.tail(3)

# Display the DataFrame's index and columns
df.index
df.columns

# Convert DataFrame to NumPy array
df.to_numpy()

# Describe statistics of the DataFrame
df.describe()

# Transpose the DataFrame
df.T

# Sort the DataFrame by index and values
df.sort_index(axis=1, ascending=False)
df.sort_values(by="B")

# Select rows and columns from the DataFrame
df["A"]
df[0:3]
df["20130102":"20130104"]
df.loc[dates[0]]
df.loc[:, ["A", "B"]]
df.loc["20130102":"20130104", ["A", "B"]]
df.loc[dates[0], "A"]
df.at[dates[0], "A"]
df.iloc[3]
df.iloc[3:5, 0:2]
df.iloc[[1, 2, 4], [0, 2]]
df.iloc[1:3, :]
df.iloc[:, 1:3]
df.iloc[1, 1]
df.iat[1, 1]
df[df["A"] > 0]
df[df > 0]
df2 = df.copy()
df2["E"] = ["one", "one", "two", "three", "four", "three"]
df2[df2["E"].isin(["two", "four"])]

# Set values in the DataFrame
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))
df["F"] = s1
df.at[dates[0], "A"] = 0
df.iat[0, 1] = 0
# df.loc[:, "D"] = np.array([5] * len(df)

#Task 4 : Operations with DataFrames
df2 = df.copy()
df2[df2 > 0] = -df2

# Handling missing data
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
df1.loc[dates[0]:dates[1], "E"] = 1
df1.dropna(how="any")
df1.fillna(value=5)
pd.isna(df1)

#Task 5: Basic operations and statistics
df.mean()
df.mean(axis=1)

#Task 6: Applying user-defined functions to DataFrames
df.agg(lambda x: np.mean(x) * 5.6)
df.transform(lambda x: x * 101.2)

# Value counts
s = pd.Series(np.random.randint(0, 7, size=10))
s.value_counts()

#Task 7: String methods for Series
s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
s.str.lower()
df.plot()