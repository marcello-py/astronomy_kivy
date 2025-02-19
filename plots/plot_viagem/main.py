# %%
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

# %%

df = pd.read_excel(r'C:\Users\marce\OneDrive\Área de Trabalho\main\projetos_testes\plot_viagem\Viagens.xlsx',
                   names=['cidade', 'estado', 'UF', 'custo']).reset_index()
df
# %%
df = df.drop('index', axis=1)
df
# %%
df.columns.name = 'index'
df
# %%
plt.figure(figsize=(10, 5))
plt.style.use('fivethirtyeight')
plt.title('Custo por UF')
norm = Normalize(vmin=df['custo'].min(), vmax=df['custo'].max())
colors = [str(0.2 + 0.5 * (1 - norm(value))) for value in df['custo']]
bars = plt.bar(df['UF'],df['custo'], color=colors)
sm = ScalarMappable(cmap='viridis', norm=norm)
sm.set_array([])
plt.colorbar(sm, label='Intensidade')
plt.xlabel('UF')
plt.ylabel('custo')
plt.savefig('graphic_bar.jpg', format='jpg')

# %% 
plt.figure(figsize=(10, 5))
plt.style.use('classic')
plt.scatter(df['UF'], df['custo'], color='gray', s=45)
plt.grid()
plt.xlabel('UF')
plt.ylabel('Custo R$')
plt.title('Custo por UF')
plt.savefig('graphic_scatter.jpg', format='jpg')