import numpy as np
import pandas as pd
df = pd.DataFrame({
   "id": [100, 100, 101, 102, 103, 104, 105, 106],
   "A": [1, 2, 3, 4, 5, 2, np.nan, 5],
   "B": [45, 56, 48, 47, 62, 112, 54, 49],
   "C": [1.2, 1.4, 1.1, 1.8, np.nan, 1.4, 1.6, 1.5]
})
df
def fill_missing_values(df):
   for col in df.select_dtypes(include= ["int","float"]).columns:
      val = df[col].mean()
      df[col].fillna(val, inplace=True)
   return df
def drop_duplicates(df, column_name):
   df = df.drop_duplicates(subset=column_name)
   return df
def remove_outliers(df, column_list):
   for col in column_list:
      avg = df[col].mean()
      std = df[col].std()
      low = avg - 2 * std
      high = avg + 2 * std
      df = df[df[col].between(low, high, inclusive=True)]
   return df

df_processed = (df.
                pipe(fill_missing_values).
                pipe(drop_duplicates, "id").
                pipe(remove_outliers, ["A","B"]))
print(df_processed)