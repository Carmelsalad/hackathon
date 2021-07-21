import pandas as pd
import matplotlib.pyplot as plt

# df_income = pd.read_csv("./df_income_extract_index.csv")
# df_balance = pd.read_csv("./df_balance_extract_index.csv")
# df_cashflow = pd.read_csv("./df_cashflow_extract_index.csv")

df_income = pd.read_csv("./df_income_filtered.csv")
df_balance = pd.read_csv("./df_balance_filtered.csv")
df_cashflow = pd.read_csv("./df_cashflow_filtered.csv")

df_income_grouped = df_income.groupby('Ticker').count()
df_balance_grouped = df_balance.groupby('Ticker').count()
df_cashflow_grouped = df_cashflow.groupby('Ticker').count()

plt.hist(df_income_grouped.iloc[:, 0], bins=50)
plt.title('distribution of companies income statements')
plt.ylabel('Number of companies')
plt.xlabel('Quarterly reports available')
plt.show()

plt.hist(df_balance_grouped.iloc[:, 0], bins=50)
plt.title('distribution of companies balance statements')
plt.ylabel('Number of companies')
plt.xlabel('Quarterly reports available')
plt.show()

plt.hist(df_cashflow_grouped.iloc[:, 0], bins=50)
plt.title('distribution of companies cashflow statements')
plt.ylabel('Number of companies')
plt.xlabel('Quarterly reports available')
plt.show()
