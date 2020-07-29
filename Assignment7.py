#!/usr/bin/env python
# coding: utf-8

# # Assignment 7 Day 7 LU Python FCS

# Q.1: Use the dictionary,
#  port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"},
#  
# and make a new dictionary in which keys become values and values become keys,
#  as shown: 
#  Port2 = {“FTP":21, "SSH":22, “telnet":23,"http": 80}

# In[3]:


port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}
print(port1)

port2 = {value:key for key, value in port1.items()}
print(port2)

Q.2: Take a list of tuple as shown below.
 [(1,2), (3,4), (5,6),(4,5)]

Make a new list which contains the sum of the number of tuples.
For example

Input :
[(1,2), (3,4), (5,6)]

Output :
[3, 7, 11]
# In[4]:


list1 = [(1,2), (3,4), (5,6)]
  
print("The original list : " + str(list1)) 
  
res = sum(map(sum, list1)) 
  
print("The summation of all tuple elements are : " + str(res)) 

Q.3: Take a list as shown below-
[(1,2,3), [1,2], ['a','hit','less']]

The List contains tuple and lists.

Make the elements of inner lists and tuples to outer list
# In[2]:


listA = [(1,2,3), [1,2], ['a','hit','less']]
# Given list
print("Given list : \n", listA)
res = [item for t in listA for item in t]
# Result
print("Final list: \n",res)


# In[ ]:




