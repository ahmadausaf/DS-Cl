#!/usr/bin/env python
# coding: utf-8

# In[2]:


# To open a file for reading it is enough to specify the name of the file:
f = open("demofile.txt")


# In[3]:


# The open() function returns a file object,
# read() method for reading the content of the file:
f = open("demofile.txt", "r")
print(f.read())


# In[5]:


# Read Only Parts of the File
# Return the 10 first characters of the file:
f = open("demofile.txt", "r")
print(f.read(10))


# In[6]:


# Read one line of the file:
f = open("demofile.txt", "r")
print(f.readline())


# In[7]:


# Read two lines of the file:
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())


# In[9]:


# Loop through the file line by line:
f = open("demofile.txt", "r")
for x in f.readlines():
   print(x)


# In[10]:


# Close the file when you are finish with it:
# Note: You should always close your files, in some cases, due to buffering,
# changes made to a file may not show until you close the file.
f = open("demofile.txt", "r")
print(f.readline())
f.close()


# In[11]:


# Write to an Existing File
f = open("demofile.txt", "a")
f.write("\n Now the file has more content!")
f.close()
#open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())


# In[12]:


# Open the file "demofile1.txt" and overwrite the content:
f = open("demofile1.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
#open and read the file after the appending:
f = open("demofile1.txt", "r")
print(f.read())


# In[13]:


f = open("myfile.txt", "w")
f.close()


# In[14]:


import os
os.remove("myfile.txt")


# In[17]:


# Check if file exists, then delete it:
if os.path.exists("myfile.txt"):
  os.remove("myfile.txt")
else:
  print("The file does not exist")


# In[ ]:




