# %% 
import pandas as pd
import numpy as np
# %%


data = { 
    "nome":["Téo", "Nah", "Lah", "Mah", "Jo"], 
    "idade":[31,32,34,12,np.nan],
    "renda":[np.nan,3245,357,12432,np.nan], 
}
df = pd.DataFrame(data)
df
# %%
df["idade"].isna().sum()

# %%

df.isna().mean()

# %%
df.fillna({'renda': df['renda'].mean()})


# %%
df