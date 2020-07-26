#!/usr/bin/env python
# coding: utf-8

# # Assignment 5 Day 5

# Q.1. Sort below list in increasing order with all zeros should be at right side
#      of list.
#      
#      Given list: [0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]

# In[1]:


lst1= [0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]


# In[2]:


lst1


# In[11]:


# Python3 code to move all zeroes 
# at the end of array 

# Function which pushes all 
# zeros to end of an array. 
def pushZerosToEnd(arr, n): 
	count = 0 # Count of non-zero elements 
	
	# Traverse the array. If element 
	# encountered is non-zero, then 
	# replace the element at index 
	# 'count' with this element 
	for i in range(n): 
		if arr[i] != 0: 
			
			# here count is incremented 
			arr[count] = arr[i] 
			count+=1
	
	# Now all non-zero elements have been 
	# shifted to front and 'count' is set 
	# as index of first 0. Make all 
	# elements 0 from count to end. 
	while count < n: 
		arr[count] = 0
		count += 1
		
# Driver code 
arr = [0, 1, 2, 10, 4, 1, 0, 56, 2, 0, 1, 3, 0, 56, 0, 4]
print('given array is',arr)
arr.sort()
n = len(arr) 
pushZerosToEnd(arr, n) 
print("Array after pushing all zeros to end of array:") 
print(arr) 



# Q.2: Merge two given sorted list in one sorted list, but only either using while 
#     or for loop at one time
#     
#     Given sorted lists:
#         list1 = [10,20,40,60,70,80]
#         list2 = [5,15,25,35,45,60]
# 

# In[13]:


list1 = [10,20,40,60,70,80]
list2 = [5,15,25,35,45,60]
# printing original lists  
print ("The original list 1 is : " + str(list1)) 
print ("The original list 2 is : " + str(list2)) 
  
# using naive method  
# to combine two sorted lists 
size_1 = len(list1) 
size_2 = len(list2) 
  
res = [] 
i, j = 0, 0
  
while i < size_1 and j < size_2: 
    if list1[i] < list2[j]: 
      res.append(list1[i]) 
      i += 1
  
    else: 
      res.append(list2[j]) 
      j += 1
  
res = res + list1[i:] + list2[j:] 
  
# printing result 
print ("The combined sorted list is : " + str(res)) 


# In[ ]:




