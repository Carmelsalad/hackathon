import pandas as pd

threshold = 10

df_income = pd.read_csv("./df_income_extract_index.csv")
df_balance = pd.read_csv("./df_balance_extract_index.csv")
df_cashflow = pd.read_csv("./df_cashflow_extract_index.csv")

print(df_income.shape)
print(df_balance.shape)
print(df_cashflow.shape)

df_income = df_income.groupby('Ticker').filter(lambda x: len(x) >= threshold)
df_balance = df_balance.groupby('Ticker').filter(lambda x: len(x) >= threshold)
df_cashflow = df_cashflow.groupby('Ticker').filter(lambda x: len(x) >= threshold)

print(df_income.shape)
print(df_balance.shape)
print(df_cashflow.shape)

df_income.to_csv("./df_income_filtered.csv", index=False)
df_balance.to_csv("./df_balance_filtered.csv", index=False)
df_cashflow.to_csv("./df_cashflow_filtered.csv", index=False)
