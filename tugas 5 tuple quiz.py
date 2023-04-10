#!/usr/bin/env python
# coding: utf-8

# In[1]:


# question 1


# In[2]:


init_tuple = ()
print (init_tuple.__len__())


# In[3]:


# question 2


# In[4]:


init_tuple_a = 'a', 'b'
init_tuple_b = ('a', 'b')

print (init_tuple_a == init_tuple_b)


# In[5]:


# question 3


# In[6]:


init_tuple_a = '1', '2'
init_tuple_b = ('3', '4')

print (init_tuple_a + init_tuple_b)


# In[7]:


# question 4


# In[8]:


init_tuple_a = 1, 2
init_tuple_b = (3, 4)

[print(sum(x)) for x in [init_tuple_a + init_tuple_b]]


# In[9]:


# question 5


# In[10]:


init_tuple = [(0, 1), (1, 2), (2, 3)]
result = sum(n for _, n in init_tuple)

print(result)


# In[11]:


# question 7


# In[12]:


l = [1, 2, 3]
init_tuple = ('Python',) * (l.__len__() - l[::-1][0])

print(init_tuple)


# In[13]:


# question 8


# In[14]:


init_tuple = ('Python') * 3

print(type(init_tuple))


# In[15]:


# question 9


# In[16]:


init_tuple = (1,) * 3
init_tuple[0] = 2
print(init_tuple)


# In[17]:


# question 10


# In[18]:


init_tuple = ((1, 2),) * 7
print(len(init_tuple[3:8]))


# In[ ]:




