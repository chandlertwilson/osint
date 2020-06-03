#!/usr/bin/env python
# coding: utf-8

# In[1]:


#packages
import numpy as np
import pandas as pd
import quandl
import json
get_ipython().run_line_magic('matplotlib', 'inline')
import scipy
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from scipy import stats
quandl.ApiConfig.api_key = 'YOUR_API_KEY'
import requests
from fbprophet import Prophet
import plotly
from fbprophet.plot import plot_plotly
import plotly.offline as py


# In[2]:


shiller=quandl.get('MULTPL/SHILLER_PE_RATIO_MONTH',collapse="monthly", start_date="2010-03-20", end_date="2020-05-10") 
df=pd.DataFrame(shiller)
df.reset_index(level=0, inplace = True)


# In[3]:


df


# In[4]:


sns.lineplot(x="Date", y="Value", data=df)
plt.xticks(rotation=15)
plt.title('Shiller Index')
plt.show()


# In[5]:


df.rename(columns={'Date':'ds', 'Value':'y'}, inplace=True)


# In[13]:


df.to_csv("shiller.csv")


# In[6]:


m = Prophet()
m.fit(df)


# In[8]:


future = m.make_future_dataframe(periods=300)
future.tail()


# In[9]:


forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()


# In[10]:


fig1 = m.plot(forecast)
fig2 = m.plot_components(forecast)


# In[11]:


fig = plot_plotly(m, forecast) 
py.iplot(fig)


# In[ ]:





# In[ ]:




