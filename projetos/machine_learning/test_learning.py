# Identificar indivíduos que podem precisar de uma intervenção
# %%

import pandas as pd

from feature_engine import encoding

from sklearn import model_selection
from sklearn import ensemble
from sklearn import metrics
from sklearn import linear_model
from sklearn import tree

# %%
df = pd.read_csv("data/dados_saude.csv")

# Agrupando por localidade e pelas varíaveis preferíveis 
df_brazil = df[df["Country"] == "Brazil"]
df_group = df_brazil[['Gender', 'self_employed', 
                      'family_history','treatment',
                      'Growing_Stress', 'Mental_Health_History', 
                      'Coping_Struggles', 'Work_Interest',]]
if df_group.isnull().any().any():
    print("Há valores nulos nas colunas selecionadas. Considere tratar os valores nulos antes da transformação.")
    df_group = df_group.dropna()

# %%
# Transformando varíveis categóricas em númericas/binárias
features = ['Gender', 'self_employed', 'family_history', 
            'treatment', 'Growing_Stress', 'Mental_Health_History', 
            'Coping_Struggles', 'Work_Interest',]

target = 'treatment'

onehot = encoding.OneHotEncoder(variables=features, drop_last=True)
X =df_group[features]
y = df_group[target].astype('category')

X_transformed = onehot.fit_transform(X)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X_transformed,y,
                                                                    test_size=0.3,
                                                                    random_state=42)

clf = ensemble.RandomForestClassifier(max_depth=3,
                                           random_state=42)
clf.fit(X_train, y_train)

# %%
y_pred_tree = clf.predict(X_test)
recall_s = metrics.recall_score(y_test, y_pred_tree, pos_label='Yes')
print(f'Acurácia do modelo de Árvore de Decisão: {recall_s:.2f}')
# %% 
tree.plot_tree(clf)