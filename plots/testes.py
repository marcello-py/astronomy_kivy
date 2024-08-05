# %%
import matplotlib.pyplot as plt
import statistics  as s
# %%


data = {'id': 6,
        'is':2,
        'idade': 27,
}
# %% 

# Extrair as chaves e os valores do dicionário
eixo_x = list(data.keys())
eixo_y = list(data.values())


# Criar o plot
plt.bar(eixo_x, eixo_y)
plt.xlabel('Chaves')
plt.ylabel('Valores')
plt.title('Plot a partir de um Dicionário')
plt.show()
# %%

