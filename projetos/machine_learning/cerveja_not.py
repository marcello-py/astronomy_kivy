# %%
import pandas as pd
from sklearn import tree
from sklearn import metrics
from sklearn import linear_model

# %%

df = pd.read_excel('data\dados_cerveja_nota.xlsx')

# %%
df['Aprovado'] = df['nota'] >= 5
df
# %%
from sklearn import linear_model
reg = linear_model.LogisticRegression(penalty=None,
                                       fit_intercept=True)

features = ['cerveja']
target = 'Aprovado'

reg.fit(df[features], df[target])

# Predição do modelo
reg_predict = reg.predict(df[features])
reg_predict
# %%
# Acuracia de regressão, quantos que o modelo está acertando? (output 0.8666666666666667)
# Na métrica ele 'pega o dado real 'target' e o dado que o modelo está prevendo
# para que ter a acuracia do percentual do acerto é preciso preve antes
reg_agg = metrics.accuracy_score(df[target], reg_predict)
reg_agg