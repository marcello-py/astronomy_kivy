# %% 
import pandas as pd
# %%


df_customor = pd.read_csv('../data/customers.csv')
df_customor

# %%
df_transaction = pd.read_excel('../data/transactions.xlsx')
df_transaction

# %%
df_transaction.merge(df_customor,
                    how='inner',
                    left_on='IdCustomer',
                    right_on='UUID')
