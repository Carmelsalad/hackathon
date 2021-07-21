import pandas as pd

threshold = 10

df_income = pd.read_csv("./df_income_elim.csv")
df_balance = pd.read_csv("./df_balance_elim.csv")
df_cashflow = pd.read_csv("./df_cashflow_elim.csv")

print(df_income.shape)
print(df_balance.shape)
print(df_cashflow.shape)

tickers_income = df_income['Ticker']
for ticker in tickers_income:
    df = df_income.loc[df_income['Ticker'] == ticker].sort_values(by='Report_Date')
    df.tail(1).to_csv("./hackathon_test/df_income_" + ticker + ".csv", index=False)
    df.iloc[:-1].to_csv("./hackathon_train/df_income_" + ticker + ".csv", index=False)

tickers_balance = df_balance['Ticker']
for ticker in tickers_balance:
    df = df_balance.loc[df_balance['Ticker'] == ticker].sort_values(by='Report_Date')
    df.tail(1).to_csv("./hackathon_test/df_balance_" + ticker + ".csv", index=False)
    df.iloc[:-1].to_csv("./hackathon_train/df_balance_" + ticker + ".csv", index=False)

tickers_cashflow = df_cashflow['Ticker']
for ticker in tickers_cashflow:
    df = df_cashflow.loc[df_cashflow['Ticker'] == ticker].sort_values(by='Report_Date')
    df.tail(1).to_csv("./hackathon_test/df_cashflow_" + ticker + ".csv", index=False)
    df.iloc[:-1].to_csv("./hackathon_train/df_cashflow_" + ticker + ".csv", index=False)
