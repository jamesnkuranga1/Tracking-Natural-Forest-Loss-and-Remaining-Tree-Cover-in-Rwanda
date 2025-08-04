import pandas as pd

# 1. Load the data (CSV version)
df = pd.read_csv("tropical_treecover_extent_2020__ha.csv")  

# (Alternative: For Excel files)
# df = pd.read_excel("file.xlsx", engine='openpyxl')  

# 2. Show first few rows to verify loading
print("\nFirst 5 rows of raw data:")
print(df.head())

# 3. Filter for Gicumbi District (adm1=1: Northern Province, adm2=3: Gicumbi)
gicumbi_df = df[(df["adm1"] == 1) & (df["adm2"] == 3)]

# 4. Show filtered results
print("\nFiltered data for Gicumbi:")
print(gicumbi_df)

# 5. (Optional) Save filtered data to new CSV
gicumbi_df.to_csv("gicumbi_filtered_data.csv", index=False)
print("\nFiltered data saved to 'gicumbi_filtered_data.csv'")