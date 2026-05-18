import pandas as pd
import numpy as np

data = {
    "Name": ["Asha", "Rahul", "Meera", "Arjun", "Diya"],
    "Age": [20, np.nan, 19, 22, np.nan],
    "Marks": [85, 90, np.nan, 92, 65]
}

df = pd.DataFrame(data)

print("Missing Values:")
print(df.isnull())

filled_df = df.fillna({
    "Age": df["Age"].mean(),
    "Marks": df["Marks"].mean()
})

print("After Filling Missing Values:")
print(filled_df)

dropped_df = df.dropna()

print("After Removing Rows with Missing Data:")
print(dropped_df)