import simfin as sf

# Set your API-key for downloading data.
# If the API-key is 'free' then you will get the free data,
# otherwise you will get the data you have paid for.
# See www.simfin.com for what data is free and how to buy more.
sf.set_api_key('free')

# Set the local directory where data-files are stored.
# The dir will be created if it does not already exist.
sf.set_data_dir('~/simfin_data/')

# Load the annual Income Statements for all companies in USA.
# The data is automatically downloaded if you don't have it already.
df_income = sf.load_income(variant='quarterly', market='us')
df_balance = sf.load_balance(variant='quarterly', market='us')
df_cashflow = sf.load_cashflow(variant='quarterly', market='us')

print(df_income.shape)
print(df_balance.shape)
print(df_cashflow.shape)

df_income['Ticker'] = df_income.index.get_level_values(0)
df_income['Report_Date'] = df_income.index.get_level_values(1)
df_income.reset_index(drop=True, inplace=True)
print(df_income.shape)

df_balance['Ticker'] = df_balance.index.get_level_values(0)
df_balance['Report_Date'] = df_balance.index.get_level_values(1)
df_balance.reset_index(drop=True, inplace=True)
print(df_balance.shape)

df_cashflow['Ticker'] = df_cashflow.index.get_level_values(0)
df_cashflow['Report_Date'] = df_cashflow.index.get_level_values(1)
df_cashflow.reset_index(drop=True, inplace=True)
print(df_cashflow.shape)

df_income.to_csv("./df_income_extract_index.csv", index=False)
df_balance.to_csv("./df_balance_extract_index.csv", index=False)
df_cashflow.to_csv("./df_cashflow_extract_index.csv", index=False)