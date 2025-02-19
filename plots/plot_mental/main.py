# %%
import pandas as pd
import matplotlib.pyplot as plt
# %%
df  = pd.read_csv('..\plot_mental\mentalhealth.csv')
df.head()
# %%
df_location = df['Country'] == 'Italy'
df_eua= df[df_location].reset_index()
df_eua
# %%
df_new = df_eua.drop(columns='index').replace(True)
df_new
# %%
df_group = df_new[['Timestamp','Gender','Occupation','self_employed',
                   'family_history','treatment','Days_Indoors', 'Growing_Stress', 
                   'Changes_Habits','Mental_Health_History','Mood_Swings', 
                   'Coping_Struggles','Work_Interest', 'Social_Weakness', 
                   'mental_health_interview','care_options']]
#pd.set_option('display.max_rows', None)
df_group
# %% 
plt.figure(dpi=600)
plt.figure(figsize=(10, 5))
plt.scatter(df_group['Gender'], df_group['Mental_Health_History'])
plt.xlabel('Timestamp')
plt.ylabel('treatment')

# %%
df_new.head()