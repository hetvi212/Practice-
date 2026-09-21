import pandas as pd 

df=pd.read_csv("house_price_5000_records.csv")

print(pd.options.display.max_rows)
print(df.to_string())
print("Head:")
print(df.head())
print("Tail:")
print(df.tail())
print("info:")
print(df.info())