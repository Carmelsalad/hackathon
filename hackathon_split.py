import pandas as pd

df_income = pd.read_csv("./df_income_elim.csv")
df_balance = pd.read_csv("./df_balance_elim.csv")
df_cashflow = pd.read_csv("./df_cashflow_elim.csv")

print(df_income.shape)
print(df_balance.shape)
print(df_cashflow.shape)

df_income = df_income.groupby('Ticker').apply(lambda x: x[:-1])
df_balance = df_balance.groupby('Ticker').apply(lambda x: x[:-1])
df_cashflow = df_cashflow.groupby('Ticker').apply(lambda x: x[:-1])

print(df_income.shape)
print(df_balance.shape)
print(df_cashflow.shape)

df_income.to_csv("./combined_train_except_last/df_income_train_except_last.csv", index=False)
df_balance.to_csv("./combined_train_except_last/df_balance_train_except_last.csv", index=False)
df_cashflow.to_csv("./combined_train_except_last/df_cashflow_train_except_last.csv", index=False)

# tickers_income = df_income['Ticker']
# for ticker in tickers_income:
#     df = df_income.loc[df_income['Ticker'] == ticker].sort_values(by='Report_Date')
#     df.tail(1).to_csv("./hackathon_test/df_income_" + ticker + ".csv", index=False)
#     df.iloc[:-1].to_csv("./hackathon_train/df_income_" + ticker + ".csv", index=False)
#
# tickers_balance = df_balance['Ticker']
# for ticker in tickers_balance:
#     df = df_balance.loc[df_balance['Ticker'] == ticker].sort_values(by='Report_Date')
#     df.tail(1).to_csv("./hackathon_test/df_balance_" + ticker + ".csv", index=False)
#     df.iloc[:-1].to_csv("./hackathon_train/df_balance_" + ticker + ".csv", index=False)
#
# tickers_cashflow = df_cashflow['Ticker']
# for ticker in tickers_cashflow:
#     df = df_cashflow.loc[df_cashflow['Ticker'] == ticker].sort_values(by='Report_Date')
#     df.tail(1).to_csv("./hackathon_test/df_cashflow_" + ticker + ".csv", index=False)
#     df.iloc[:-1].to_csv("./hackathon_train/df_cashflow_" + ticker + ".csv", index=False)
