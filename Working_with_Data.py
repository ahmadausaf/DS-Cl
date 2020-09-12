#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import the package "Pandas" into Jupyter Notebook
import pandas as pd


# In[30]:


#We import the stock data of TCS into Jupyter Notebook. The CSV file is located␣

# We then name the DataFrame name as 'tcs'
TCS = pd.read_csv('TCS.csv' ,index_col='Date')


# In[31]:


print(TCS.head())


# In[32]:


# show the size of dataframe using shape 
TCS.shape


# In[33]:


#printing summary statistics of TCS 
print(TCS.describe())


# In[34]:


# select all the price information of TCS in 2019.
TCS_2019 = TCS.loc['2019-01-01':'2019-12-30']


# In[35]:


# print the price of TCS on '2019-01-02'
print(TCS_2019.loc['2019-01-02'])


# In[36]:


# print the opening price of the first row
print(TCS.iloc[0, 0])


# In[37]:


# print the opening price of the last row
print(TCS.iloc[135,0])


# In[38]:


import matplotlib.pyplot as plt
plt.figure(figsize=(12, 10))
TCS['Close'].plot()
plt.show()


# In[39]:


#Create a new column PriceDiff in the DataFrame TCS
TCS['PriceDiff'] = TCS['Close'].shift(-1) - TCS['Close']


# In[40]:


TCS.head()


# In[41]:


#Create a new column Return in the DataFrame TCS
TCS['Return'] = TCS['PriceDiff'] /TCS['Close']
TCS.head()


# In[42]:


# Create a new column in the DataFrame using Rolling Window calculation
#(.rolling()) - Moving average

TCS['ma50'] = TCS['Close'].rolling(50).mean()
#plot the moving average
plt.figure(figsize=(12, 8))
TCS['ma50'].plot(label='MA50')
TCS['Close'].plot(label='Close')
plt.legend()
plt.show()


# **BUILDING A SIMPLE TRADING STRATEGY**

# In[43]:


import pandas as pd
import matplotlib.pyplot as plt


# In[ ]:


# Munging the stock data and add two columns - MA10 and MA50 


# In[44]:


#import Reliance stock data, add two columns - MA10 and MA50
#use dropna to remove any "Not a Number" data
rel = pd.read_csv('reliance.csv',index_col="Date")
rel['MA10'] = rel['Close'].rolling(10).mean()
rel['MA50'] = rel['Close'].rolling(50).mean()
rel = rel.dropna()
rel.head()


# In[54]:


#plot the moving average
plt.figure(figsize=(12, 10))
rel['MA10'].plot(label='MA10')
rel['MA50'].plot(label='MA50')
rel['Close'].plot(label='Close')
plt.legend()
plt.show()


# In[55]:


# Add a new column "Shares",
# if MA10 > MA50, denote as 1 (long one share of stock),
# otherwise, denote as 0 (do nothing)

rel['Shares'] = [1 if rel.loc[x, 'MA10'] > rel.loc[x, 'MA50'] else 0 for x in rel.index]


# In[57]:


rel['Close1'] = rel['Close'].shift(-1)
rel['Profit'] = [rel.loc[x, 'Close1'] - rel.loc[x, 'Close'] if rel.loc[x, 'Shares']==1 else 0 for x in rel.index]


# In[58]:


rel['wealth'] = rel['Profit'].cumsum()
rel.tail()


# In[59]:


#plot the wealth to show the growth of profit over the period
rel['wealth'].plot()
plt.title('Total money you gain is {}'.format(rel.loc[rel.index[-2],'wealth']))


# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




