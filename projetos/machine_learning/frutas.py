# %%
import pandas as pd

from sklearn import model_selection
from sklearn import ensemble
from sklearn import metrics
from sklearn import linear_model
import matplotlib.pyplot as plt


# %%
# Carregando os dados
df = pd.read_excel('data\dados_frutas.xlsx')

# Definição das features e target
features = ["Arredondada", "Suculenta", "Vermelha", "Doce"]
target = 'Fruta' 
X = df[features]
y = df[target]
# %%
X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y,
                                                                    test_size=0.30,
                                                                    random_state=42)

# %%
model_rf = ensemble.RandomForestClassifier(max_depth=3, 
                                           random_state=42)
model_rf.fit(X_train,y_train)
# %%
pred = model_rf.predict(X_test)
pred
# %%
reg = ensemble.RandomForestRegressor(penalty=None,fit_intercept=True)

reg.fit(df[features], df[target])

# Predição do modelo
reg_predict = reg.predict(df[features])
reg_predict
# %%
# Acuracia de regressão, quantos que o modelo está acertando? (output 0.8571428571428571)

reg_acc = metrics.accuracy_score(df[target], reg_predict)
reg_acc











# %%


'''# %%
import pandas as pd
from sklearn import tree
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn import ensemble
import matplotlib.pyplot as plt
from sklearn import linear_model
# %%
# Carregando os dados
df = pd.read_excel('data\dados_frutas.xlsx')

# Definição das features e target
features = ["Arredondada", "Suculenta", "Vermelha", "Doce"]
target = 'Fruta' 
X = df[features]
y = df[target]

# %%
# Criando e treinando a árvore de decisão
arvore = tree.DecisionTreeClassifier(max_depth=2, random_state=42) 
arvore.fit(X, y)
# %%
reg = ensemble.(penalty=None,
                                       fit_intercept=True)
reg.fit(df[features], df[target])

# Predição do modelo
reg_predict = reg.predict(df[features])
reg_predict
# %%
# Acuracia de regressão, quantos que o modelo está acertando? (output 0.8571428571428571)

reg_acc = metrics.accuracy_score(df[target], reg_predict)
reg_acc
# %%
df'''