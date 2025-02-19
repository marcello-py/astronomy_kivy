# %% 
import pandas as pd
# %%

df = pd.read_excel('../data/transactions.xlsx')
df

# %%

df_sumary = df.groupby(['IdCustomer'])['Points'].mean()
df_sumary
# %%
df
# %%
df.groupby(['IdCustomer']).agg({'Points': 'sum',
                                'UUID': 'count',
                                'DtTransaction':'max'}).reset_index()
# %%

