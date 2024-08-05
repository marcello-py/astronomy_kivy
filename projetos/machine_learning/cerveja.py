# %%
import pandas as pd

from feature_engine import encoding

from sklearn import ensemble
from sklearn import model_selection
from sklearn import tree
# %%
df = pd.read_excel("data\dados_cerveja.xlsx")
df
# %%
features = ["classe", "espuma"]

target = "cor"
# %%

onehot = encoding.OneHotEncoder(variables=features)
# %%
X = df[features]
y = df[target]
X_transformed = onehot.fit_transform(X)
# %%
X_train, X_test, y_train, y_test = model_selection.train_test_split(X_transformed,y,
                                                                    test_size=0.3,
                                                                    random_state=42)
# %%
arvore = tree.DecisionTreeClassifier(max_depth=6, 
                                    random_state=42)
arvore.fit(X_train, y_train)


# %%
# classe / espuma
arvore.predict([[1,0,1,0,1]])

# %%
X_transformed

# %%
