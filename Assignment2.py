#!/usr/bin/env python
# coding: utf-8

# # Assignment 2

# - Back slash

# In[1]:


print("Hello python")


# In[2]:


print("Hello 
      python")


# In[3]:


print("Hello python")


# In[4]:


print(" back slash in python is used for continuation")


# - Triple Quote -----------------------------------

# In[5]:


print(""" hello python """)


# In[9]:


print (""" 
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█▄▄░▄▄█░▄▄█░█░█▄░▄████░▄▄▄█░▄▄▀█░▄▄▀█▀▄▀█░██░
███░███░▄▄█▀▄▀██░█████░▄▄██░▀▀░█░██░█░█▀█░▀▀░
███░███▄▄▄█▄█▄██▄█████░████▄██▄█▄██▄██▄██▀▀▀▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

  """)


# - Triple quoate is used for printing inputed text or anything as it as without error

# In[10]:


"""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█▄▄░▄▄█░▄▄█░█░█▄░▄████░▄▄▄█░▄▄▀█░▄▄▀█▀▄▀█░██░
███░███░▄▄█▀▄▀██░█████░▄▄██░▀▀░█░██░█░█▀█░▀▀░
███░███▄▄▄█▄█▄██▄█████░████▄██▄█▄██▄██▄██▀▀▀▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
"""


# - It creates for documentation not with print

# - String Inside the quotes ----------------------

# In[11]:


print('hello world')


# In[12]:


print('python's world)


# In[13]:


print("python's world")


# - statements should start and end with same quotes. not used in between statement like above error

# - Escape Sequence of String ----------------------------------------------
# 
# used for producing space(\t or tab)
# as below

# - \ used for continuation
# - \n used for line seperator
# - \t used for new tab

# - line sepeartor ------------------

# In[14]:


print('hi\n hello ')


# In[15]:


print('hii \t hello')


# In[18]:


print('python\'s world')


# - Formatted output------------------------------------

# In[19]:


name = "xyz"
marks =99.0
age=20
print(" the name of person is", name,"marks is ",marks,"age is", age)


# In[22]:


print(" the name of person is %s marks is %f age is %d"%(name,marks,age))


# - for spaces

# In[23]:


print(" the name of person is %10s marks is %10f age is %10d"%(name,marks,age))


# In[24]:


print(f" the name of person is {name} marks is {marks} age is {age}")


# # python variables and assignment statement

# - variables means linking data to name
# 
# - Keyword can not be used as variables like if for etc
# 
# - u can use lowercase , upperacase anything
# 
# - python is case sensitive 
# 
# - variable name can contain underscore
# 
# - cam not start with number

# In[31]:


a=10


# In[26]:


a


# In[27]:


A=10


# In[28]:


A


# In[29]:


A=20


# In[30]:


A


# In[32]:


a10= 20


# In[33]:


10a=20


# In[34]:


a_b= 60


# In[35]:


a_b


# In[39]:


id(a)


# In[43]:


print(" it is ram of a------id() function is used for ram")


# In[41]:


_10=50


# In[42]:


_10


# - assignement statement

# In[44]:


x=y=20


# In[45]:


x


# In[46]:


y


# #  python operators

# - Arithmatic
# 
# - Comparision
# 
# - Assignment
# 
# - Bitwise
# 
# - Logical
# 
# - Membaership
# 
# - identity
# 
# this all are types of operators in python

# - Arithmatic operators --------------------------------------------------

# In[47]:


5**5


# In[48]:


5*5


# In[49]:


5+5


# In[50]:


5-5


# In[51]:


5/5


# In[52]:


10/2


# In[53]:


10%2


# In[54]:


10%4


# In[55]:


10//3


# In[57]:


print("last one is used for floor division")


# - Comparision operator--------------------------------------

# In[58]:


a=10
b=20
a==b


# In[59]:


c=10
a==c


# In[60]:


a<=c


# In[61]:


c<= a


# In[62]:


a<=b


# In[63]:


b<=a


# In[64]:


a>=b


# In[66]:


a>=c


# In[67]:


a!=b


# In[68]:


a!=c


# - Assignment Opeartors ----------------------------------------------------

# - bitwise op

# - logical opearator-----------------------------------------------------------

# In[69]:


a=10
b=20


# In[70]:


a>20 or b>10


# In[71]:


a>20 and b>10


# In[72]:


not a<10


# In[73]:


not b<20


# In[74]:


not b>20


# - Membership opeartor-----------------------------------------------------------
# 
# 
# 
# - in 
# 
# - not in
# 
# 
# its output is true or false only

# In[77]:


str1= 'python'


# In[78]:


str1


# In[80]:


'p' in str1


# In[81]:


'x' in str1


# In[82]:


'p' not in str1


# In[83]:


"x" not in str1


# - Identity Operator-----------------------------------------------------------------
# 
# 
# - Is
# 
# 
# 
# - is not

# In[84]:


a=10
b=10
a==b


# In[85]:


a is b


# In[86]:


id(a)


# In[87]:


id(b)


# - opeartor precedence

# In[ ]:




