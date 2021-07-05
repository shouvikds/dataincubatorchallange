#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import io
import requests
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
import seaborn as sns


# In[2]:


vaccination_url="https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv"
vacdf =pd.read_csv(vaccination_url)
vacdf = vacdf.rename(columns={"location": "Country Name"})


# In[3]:


vacdf.fillna(0)


# In[4]:


vacdf.head()


# In[5]:



vacdf_agg = vacdf.groupby('Country Name').agg({'daily_vaccinations': 'sum', 'people_fully_vaccinated': 'max'})


# In[6]:


vacdf_agg.fillna(0)
vacdf_agg.head()


# In[7]:


population_url="https://raw.githubusercontent.com/shouvikds/dataincubatorchallange/main/API_SP.POP.TOTL_DS2_en_csv_v2_2593013/API_SP.POP.TOTL_DS2_en_csv_v2_2593013.csv"
popdf =pd.read_csv(population_url, skiprows = 3)
popdf = popdf[['Country Name', '2020']]
popdf = popdf.rename(columns={"2020": "Population"})
popdf.fillna(0)


# In[8]:


popdf.head()


# In[9]:


vac_merged_df = pd.merge(vacdf, popdf, how = 'left', on = 'Country Name')
vac_agg_merged_df = pd.merge(vacdf_agg, popdf, how = 'left', on = 'Country Name')


# In[ ]:


vac_merged_df.fillna(0)
vac_agg_merged_df.fillna(0)
vac_merged_df.head()


# In[ ]:


vac_agg_merged_df.head()


# In[ ]:


sns.set(rc={'figure.figsize':(8.7,8.27)})
sns.scatterplot(data = vac_agg_merged_df, x = "Population", y = "people_fully_vaccinated", 
                 hue = 'Country Name', alpha=.9, palette="muted",)


# In[ ]:


vac_agg_merged_df = vac_agg_merged_df.fillna(0)
vac_agg_merged_df.head()
vac_agg_merged_df['Vaccinated_percentage']= vac_agg_merged_df['people_fully_vaccinated']/vac_agg_merged_df['Population']*100
vac_agg_merged_df.head()


# In[ ]:


sns.barplot(data = vac_agg_merged_df, x='Country Name', y='Vaccinated_percentage')


# In[ ]:


vac_agg_merged_df.sort_values(by='Vaccinated_percentage')


# In[ ]:


vac_agg_merged_df_top_10_unvaccinated = vac_agg_merged_df[1:10]


# In[ ]:


vac_agg_merged_df_top_10_vaccinated = vac_agg_merged_df[-10:]


# In[ ]:




