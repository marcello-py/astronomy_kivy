# %%
# modelo será usado para prever o número de suicídios 
# com base no ano e no sexo dos indivíduos
import pandas as pd

from sklearn import model_selection
from sklearn import metrics
from sklearn import tree
from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor

from feature_engine import encoding

# %%
df = pd.read_csv('.\data\suicide_rates.csv')
df_brazil = df[df['CountryCode'] == 'BRA']
df_brazil = df_brazil.drop(columns=['RegionCode', 'RegionName'])
df_suicide = df_brazil[['Sex', 'SuicideCount', 'Year']]
df_suicide = df_suicide[df_suicide['Sex'] != 'Unknown']
df_suicide
# %%
# Transformando as variáveis categóricas
features = ["Sex", "Year"]
X = df_suicide[features]
y = df_suicide["SuicideCount"].astype(int)

onehot = encoding.OneHotEncoder(variables=["Sex"])
X = onehot.fit_transform(X)
# %%
# Separando em base de treino e base de testes
# Stratify: Garante que a proporção das classes ou valores
x_train, x_test, y_train, y_test = model_selection.train_test_split(X, y, 
                                                                    test_size=0.2, 
                                                                    random_state=42, 
)
#                                                              stratify=X)
# %%
# Treinamento do modelo de regressão linear
#model = linear_model.LinearRegression()
model_rf = RandomForestRegressor(random_state=42)
model_rf.fit(x_train, y_train)

print('Base de treino', y_train.mean())
print('Base de teste', y_test.mean())

# Predição do modelo
y_pred = model_rf.predict(x_test)
mae = metrics.mean_absolute_error(y_test, y_pred)
mse = metrics.mean_squared_error(y_test, y_pred)
r2 = metrics.r2_score(y_test, y_pred)

print('Desempenho do Modelo de Regressão Linear:')
# (Erro Médio Absoluto) mede a média das diferenças absolutas entre as previsões e os valores reais.
# Quanto menor o MAE, melhor o desempenho do modelo.
print('mae:',mae)
# (Erro Quadrático Médio) mede a média dos quadrados das diferenças entre as previsões e os valores reais
# Quanto menor o MSE, melhor o desempenho do modelo
print('mse:',mse)
#  R² Score mede a proporção da variabilidade dos dados que é explicada pelo modelo.
# Se o R2=1: O modelo explica toda a variabilidade dos dados (previsões perfeitas).
print('r2:',r2)
#MAE: Se o MAE for 1.9, significa que, em média, as previsões estão erradas por 1.9 unidades.
#MSE: Se o MSE for 5.3, significa que a média dos quadrados dos erros é 5.3, indicando a penalização maior para erros maiores.
#R²: Se o R² for 0.92, significa que 92% da variabilidade dos dados é explicada pelo modelo, indicando um bom ajuste.
