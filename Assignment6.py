#!/usr/bin/env python
# coding: utf-8

# # Assignment 6 Day 6 LU Python FCS

# Q.1: Covert following two list into dictionary in one line code using list 
#     comprehension (Without using zip method)
#     
#     list1 = [1,2,3,4,5,6,7,8]
#     list2 = ["a","b","c","d","e","f","g","h"]

# In[5]:


list1 = [1,2,3,4,5,6,7,8]
list2 = ["a","b","c","d","e","f","g","h"]
print ("Original key list1 is : " + str(list1)) 
print ("Original value list2 is : " + str(list2)) 
  
# using dictionary comprehension 
# to convert lists to dictionary 
res = {list1[i]: list2[i] for i in range(len(list1))} 
  
# Printing resultant dictionary  
print ("Resultant dictionary is : " +  str(res)) 


# In[ ]:





# In[ ]:




