# %%
import pandas as pd
import matplotlib.pyplot as plt

 # %%
df = pd.read_csv('..\plot_suicide\suicide_rates.csv')

df_location = df['CountryCode'] == 'BRA'
df_brazil = df[df_location]

df_brazil.drop(columns=['RegionCode','RegionName'], inplace=True)

# %%
df_brazil_group = (df_brazil[['Year', 'Sex', 'AgeGroup','Generation',
                              'CauseSpecificDeathPercentage','SuicideCount', 
                              'Population']]).reset_index()

df_brazil_group.drop(columns=['Generation'], inplace=True)

# %%
df_brazil_group['avg_suicide(%)'] = (df_brazil_group['SuicideCount'] / df_brazil_group['Population'] * 100).round(4)
df_brazil_group
# %%
plt.figure(figsize=(10, 5))
plt.bar(df_brazil_group['Sex'], df_brazil_group['SuicideCount'], color='gray')
plt.grid(True)
plt.ylabel('SuicideCount')
plt.xlabel('Sex')
plt.title('1990 - 2015')
plt.savefig('suicide.jpeg', format='jpeg')

# %%
plt.figure(figsize=(10, 5))
plt.bar(df_brazil_group['Sex'], df_brazil_group['AgeGroup'])
plt.grid(True)
plt.ylabel('AgeGroup')
plt.xlabel('Sex')
plt.savefig('suicide_age.jpeg', format='jpeg')

# %%
df_brazil_group.head()
# %%
#pd.set_option('display.max_rows', None)
df_brazil_group['CauseSpecificDeathPercentage'] = df_brazil_group['CauseSpecificDeathPercentage'].round(2)
df_brazil_group.head()
 # %%
df_suicide = df_brazil_group[['Sex', 'SuicideCount','Year']]
df_suicide

# %%
# modelo será usado para prever o número de suicídios 
# com base no ano e no sexo dos indivíduos
# Transformando varíveis categóricas em binárias 
feature = ['Sex', 'SuicideCount', 'Year']
cat_features = ['Sex']
X = df_suicide[feature]

from feature_engine import encoding

onehot = encoding.OneHotEncoder(variables=cat_features)
onehot.fit(X)
X = onehot.transform(X)
X

# %%
from sklearn import tree

arvore = tree.DecisionTreeClassifier()
arvore.fit(X, df_suicide['SuicideCount'])