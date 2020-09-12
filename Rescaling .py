#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import the package "Pandas" into Jupyter Notebook
import pandas as pd


# In[3]:


person = pd.read_csv('person.csv', index_col="Person")
person.head()


# **CASE 1: Height in Inches**

# In[5]:


# Distance beteen the point(Height,Weight)
import math
def distance(x,y):
    return math.sqrt( ((x[0]-y[0])**2)+((x[1]-y[1])**2) )
a_to_b = distance([63, 150], [67, 160]) # 10.77
a_to_c = distance([63, 150], [70, 171]) # 22.14
b_to_c = distance([67, 160], [70, 171]) # 11.40


# In[6]:


print(a_to_b, a_to_c, b_to_c)


# **CASE 2: Height in CM**

# In[7]:


a_to_b = distance([160, 150], [170.2, 160]) # 14.28
a_to_c = distance([160, 150], [177.8, 171]) # 27.53
b_to_c = distance([170.2, 160], [177.8, 171]) # 13.37
print(a_to_b, a_to_c, b_to_c)


# **3. Scaling the data [a,b] to [0,1]**
# 

# In[8]:


# • (x-min)/length_of_interval = (x-a)/(b-a)
tmp_height_inch = person["Height_inch"] - person["Height_inch"].min()
scaled_height_inch = tmp_height_inch / tmp_height_inch.max()
person["scaled_height_inch"] = scaled_height_inch


# In[9]:


person.head()


# **4. SCIKIT LEARN**

# • Classification (Spam detection, image recognition)
# • Regression (Drug response, Stock prices)
# • Clustering (Customer segmentation, Grouping experiment outcomes)
# • Dimensionality reduction (Visualization, Increased efficiency)
# • Model selection (Improved accuracy via parameter tuning)
# • Preprocessing (Transforming input data such as text for use with machine learning algorithms)
• MinMax Scaler
• Standard Scaler
• MaxAbs scaler
# In[11]:


# Data processing before using Scikit-learn
person_data = pd.read_csv('person1.csv')
print(person_data.head())
x = person_data['ages'].values.reshape(-1, 1) #returns a numpy array
y = person_data['heights'].values.reshape(-1,1) #returns a numpy array


# In[12]:


# MinMax scaler
from sklearn.preprocessing import MinMaxScaler
scaler1 = MinMaxScaler()
x_scaled1 = scaler1.fit_transform(x)
y_scaled1 = scaler1.fit_transform(y)
person_data['ages_scaled_min_max'] = x_scaled1
person_data['heights_scaled_min_max'] = y_scaled1
person_data.head()


# In[13]:


# Standard scaler
from sklearn.preprocessing import StandardScaler
scaler2 = StandardScaler()
x_scaled2 = scaler2.fit_transform(x)
y_scaled2 = scaler2.fit_transform(y)
person_data['ages_scaled_standard'] = x_scaled2
person_data['heights_scaled_standard'] = y_scaled2
person_data.head()


# In[14]:


# Max abs scaler
from sklearn.preprocessing import MaxAbsScaler
scaler3 = MaxAbsScaler()
x_scaled3 = scaler3.fit_transform(x)
y_scaled3 = scaler3.fit_transform(y)
person_data['ages_scaled_max_Abs'] = x_scaled3
person_data['heights_scaled_max_Abs'] = y_scaled3
person_data.head()


# In[15]:


# RobustScaler
from sklearn.preprocessing import RobustScaler
scaler4 = RobustScaler()
x_scaled4 = scaler4.fit_transform(x)
y_scaled4 = scaler4.fit_transform(y)
person_data['ages_scaled_max_Abs'] = x_scaled4
person_data['heights_scaled_max_Abs'] = y_scaled4
person_data.head()


# In[ ]:




