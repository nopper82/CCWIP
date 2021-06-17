#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("CCRC/6-11Current In-Process Totals.csv")
df.head(5)


# In[3]:


df.drop(df.columns[[1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 13, 14]], axis = 1, inplace = True)  
df


# In[4]:


df = df.rename(columns={"Parts Sales": "Sale", "Parts Cost": "Cost"})
df


# In[5]:


index_names = df[ df['Cost'] == 0 ].index
df.head()


# In[6]:


df.drop(index_names, inplace = True)


# In[7]:


df['Gross'] = df['Sale'] - df['Cost']
df


# In[8]:


df.sum(axis=0)


# In[ ]:




