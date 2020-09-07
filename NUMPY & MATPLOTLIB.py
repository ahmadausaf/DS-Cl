#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


# Single Dimensional Array
np.array([10,20,30,40])


# In[3]:


# Multi Dimensional Array
np.array([[10,20,30,40],[30,40,60,90]])


# In[4]:


# Initializing NumPy Array with zeros
np.zeros((1,3))


# In[5]:


np.zeros((5,4))


# In[6]:


# Initializing NumPy Array with ones
np.ones((3,4))


# **Exercise 1**

# In[26]:


# Initializing NumPy Array with same number 
np.ones((3,3))*8


# In[27]:


# Initializing NumPy Array within range
np.arange(10,18)


# In[28]:


np.arange(10,20,3)


# **Exercise 2**

# In[30]:


# Generate all the even numbers between 101 to 114
np.arange(100,115,2)


# In[31]:


# Initializing NumPy Array with random numbers
np.random.randint(1,100,5)


# In[32]:


# NumPy array addition
n1 = np.array([10,30,80])
n2 = np.array([40,30,10])
# Overall Sum
np.sum([n1,n2])


# In[33]:


# Row Sum
np.sum([n1,n2],axis=1)


# In[34]:


# Column Sum
np.sum([n1,n2],axis=0)


# # 2. MATPLOTLIB

# In[35]:


# Ploting
import matplotlib.pyplot as plt


# **2.1 SCATTER PLOT**

# In[36]:


Year = [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010]
UR = [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
# Scatter Plot
plt.scatter(Year,UR)


# In[37]:


# Scatter Plot
plt.scatter(Year,UR)
plt.title('Unemployment Rate Vs Year')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate')
plt.grid(True)


# **2.2 LINE CHART**

# In[38]:


plt.plot(Year,UR,marker='o')
plt.title('Unemployment Rate Vs Year')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate')
plt.grid(True)
plt.show


# **2.3 BAR CHART**

# In[39]:


# BAR CHART
plt.bar(Year,UR)
plt.title('Unemployment Rate Vs Year')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate')
plt.show()


# In[40]:


# Bar Chart
xAxis = [x for x, _ in enumerate(Year)]
plt.bar(xAxis,UR)
plt.title('Unemployment Rate Vs Year')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate')
plt.xticks(xAxis,Year)


# **Exercise 3**

# In[41]:


# Draw the bar Chart for given data
x = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec']
y = [5,4,8,10,3,2,9,5,11,2,6,9]
plt.bar(x,y)


# In[ ]:




