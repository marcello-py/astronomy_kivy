# %% 
import pandas as pd

# %%

df = pd.read_csv('../data/products.csv',
                 sep=";",
                 names=["n", 'i', 'g'])

df