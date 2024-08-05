# %% 
import pandas as pd

data_01 = { 
    "id": [1,2,3,4], 
    "nome":["Teo", "Mat", "Nah", "Mah"], 
    "idade": [31,31,32,32] 
}
df_01 = pd.DataFrame(data_01)
df_01
# %%
data_02 = { 
    "id": [1,2,3,4], 
    "nome":["Teo", "Mat", "Nah", "Mah"], 
    "idade": [31,31,32,32] 
}
df_02 = pd.DataFrame(data_02)

df_02
# %%

pd.concat([df_01, df_02])
