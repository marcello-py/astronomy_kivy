# %%
import pandas as pd


# %%

df = pd.read_csv("../data/products.csv", sep=';',
                 names=(['indice', 'chat', 'mensagem']))
df
# %%
df.sort_values(by='mensagem')