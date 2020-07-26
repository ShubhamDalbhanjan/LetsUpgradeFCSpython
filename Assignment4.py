#!/usr/bin/env python
# coding: utf-8

# # Assignment 4 Day 4 

# Q.1 Find all occurences of substring in given string and print index.
# 
# Input String: " what we think we become; we are python programmer"

# In[10]:


mainStr = 'what we think we become; we are python programmer'

substring = 'we'
print('substring is:',substring)
count = mainStr.count(substring)
print("'we' sub string frequency / occurrence count : " , count)
index = mainStr.find(substring)
print('first index of substring is',index)

------------------------------------------------------------------------------------------------------
# Q.2. Check diffrent strings with following functions:
#     
#     - islower()
#     
#     - isupper()
#     
#     

# In[11]:


st1='goodMorning'


# In[12]:


st1


# In[13]:


st1.islower()


# In[14]:


st1.isupper()


# In[15]:


st1='goodmorning'


# In[16]:


st1.islower()


# In[17]:


st1.isupper()


# In[18]:


st1='goodmorning2'


# In[19]:


st1.islower()


# In[20]:


st1.isupper()


# In[21]:


st1='gOOodmorning2'


# In[22]:


st1.islower()


# In[23]:


st1.isupper()


# In[24]:


st1='25682G##'


# In[25]:


st1.islower()


# In[26]:


st1.isupper()


# In[27]:


st1='GOODMORNING'


# In[28]:


st1.islower()


# In[29]:


st1.isupper()


# In[ ]:




