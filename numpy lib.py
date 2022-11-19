#!/usr/bin/env python
# coding: utf-8

# # Numpy

# NumPy is a scientific computing package (library) for python programming language.
# Numpy is a powerful Python programming language library to solve numerical problems.
# Num stands for numerical and Py stands for Python programming language.

# In[2]:


import numpy as np


# In[3]:


b=np.array([[1,2,3],[2,3,5],[4,9,9]])
b


# In[4]:


r=np.array([[1,2,3],[2,3,4],[7,7,9]],ndmin=3,dtype=complex)
r


# In[5]:


r.ndim #to check the dimension


# In[6]:


r.shape 


# In[7]:


r.reshape(9,1)


# In[8]:


n=np.ones([20],dtype=int)
n


# In[9]:


w=np.empty(3)
w


# In[10]:


a=np.zeros(2)
a


# In[11]:


a=np.linspace(1,10,3,endpoint=True,retstep=True)
a


# In[12]:


a=np.arange(9).reshape(3,3)
b=np.arange(9).reshape(3,3)
a


# In[13]:


b


# In[14]:


np.add(a,b)


# In[15]:


np.subtract(b,a)


# In[16]:


np.divide(a,b)


# In[17]:


np.multiply(a,b)


# # Matrix Product of Two NumPy Array (matrix)

# In[18]:


a


# In[19]:


b


# In[20]:


r=a.dot(b)
r


# In[21]:


r.max()


# In[22]:


r.min()


# In[23]:


r.max(axis=0)  


# In[24]:


r.argmax()


# In[25]:


np.sum(r, axis = 0) # return sum of each column


# In[26]:


np.mean(r)


# In[27]:


np.median(r)


# In[28]:


np.modf(r)


# In[29]:


np.sqrt(r) #Return square root of each element of NumPy array.


# In[30]:


np.std(r) #Return standard deviation  of  array.


# In[31]:


np.log(r)#Return log value of each element of NumPy array.


# In[32]:


np.exp(r) #Return exponent of each element of NumPy array.


# #  Trigonometric Function

# degree

# In[33]:


sin=np.sin(90) #tri. value of angle in degrees
print(sin)
cos=np.cos(90)
print(cos)
tan=np.tan(90)
print(tan)


# In[34]:


#tri value of angle in radian
sin=np.sin(90*np.pi/180)
print(sin)
cos=np.cos(90*np.pi/180)
print(cos)
tan=np.tan(90*np.pi/180)
print(tan)


# # Python NumPy String Operations Methods

# In[35]:


a='InDian'
b='Boys'


# In[36]:


r=np.char.add(a,b,)
r


# In[37]:


m=np.char.multiply(b,3)
m


# In[38]:


m=np.char.capitalize(a)
m


# In[39]:


m=np.char.lower(a)
m


# In[40]:


m=np.char.upper(a)
m


# In[41]:


import numpy as np


# In[42]:


a=np.array([[1,2],[3,4],[5,6]])


# In[43]:


a


# In[44]:


a[[0,1,1],[0,1,0]]


# In[45]:


m=np.array([[1,2,1],[3,4,3],[5,6,6]])


# In[46]:


m


# In[47]:


a


# In[48]:


a[0:,[0,1,0]]


# In[49]:


a[:2,[0,1,0]]


# # Broadcasting

# In[53]:


a


# In[55]:


a[2][1]


# In[73]:


r=a[0:,[1,0,1]]


# In[74]:


r


# In[79]:


r[2][1]


# In[ ]:




