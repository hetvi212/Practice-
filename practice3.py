import pandas as pd 

df=pd.read_csv('Marriott_Vendor_Master_5000.csv')
new_df=df.dropna()
print(new_df.to_string())
print("Column name ")
print(df.columns)
df['Credit_Limit']=df["Credit_Limit"].fillna(df['Credit_Limit'].mean())
df['Tax_Percentage']=df['Tax_Percentage'].fillna(df['Tax_Percentage'].median())

print(df)