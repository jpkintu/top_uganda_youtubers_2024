import pandas as pd
# IMPORT CSV FILE
df_influencers=pd.DataFrame()
df=pd.read_csv('TOP 100 YOUTUBERS IN UGANDA SORTED BY SB RANK.csv')

# drop rows with null values
df.dropna(inplace=True)

# # Conversion Function (convert_abbreviated_to_float):
# We define a function called convert_abbreviated_to_float that takes an abbreviated value (e.g., “400k”, “2.11m”) as input.
# Inside the function:
# We remove any spaces and convert the input value to lowercase for consistent handling.
# If the value ends with “k,” we multiply the numeric part by 1000 (to convert thousands to the full numeric value).
# If it ends with “m,” we multiply by 1,000,000 (to convert millions to the full numeric value).
# Otherwise, we assume it’s already a numeric value and return it as is.
# Applying the Conversion to the ‘subs’ Column:
# We use the .apply() method on the “subs” column of the DataFrame (df).
# For each value in the “subs” column, the convert_abbreviated_to_float function is called, and the result is assigned back to the same column.
# This effectively replaces the abbreviated values with their corresponding full numeric representations.
# Printing the Modified DataFrame:
# Finally, we print the modified DataFrame (df) to see the updated values in the “subs” column.

# Function to convert abbreviated values to full numeric values
def convert_abbreviated_to_float(abbreviated_value):
    cleaned_value = abbreviated_value.replace(" ", "").lower()
    if cleaned_value.endswith("k"):
        return float(cleaned_value[:-1]) * 1000
    elif cleaned_value.endswith("m"):
        return float(cleaned_value[:-1]) * 1_000_000
    else:
        return float(cleaned_value)
        
# Apply the conversion to the 'subs' column
df["Subs"] = df["Subs"].apply(convert_abbreviated_to_float)        

# convert video vies column to float from int64
df["Video Views"] = df["Video Views"].astype(float)

# df.shape
df.info()
df.head()