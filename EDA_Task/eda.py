import pandas as pd

# Sample Dataset
data = {
    "Name": ["John", "Ravi", "Priya", "Kumar"],
    "Age": [18, 19, 18, 20],
    "Marks": [85, 92, 78, 88]
}

df = pd.DataFrame(data)

print("="*50)
print("      EXPLORATORY DATA ANALYSIS (EDA)")
print("="*50)

print("\n1. Dataset")
print(df)

print("\n" + "="*50)
print("2. Rows and Columns")
print("="*50)
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n" + "="*50)
print("3. Data Types")
print("="*50)
print(df.dtypes)

print("\n" + "="*50)
print("4. Missing Values")
print("="*50)
print(df.isnull().sum())

print("\n" + "="*50)
print("5. Statistics")
print("="*50)
print(df.describe())

print("\n" + "="*50)
print("6. Analysis")
print("="*50)
print("Highest Mark:", df["Marks"].max())
print("Lowest Mark:", df["Marks"].min())
print("Average Mark:", round(df["Marks"].mean(),2))

print("\n" + "="*50)
print("EDA Completed Successfully")
print("="*50)