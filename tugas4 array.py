#!/usr/bin/env python
# coding: utf-8

# # 1. Create an array and traverse. 
# 

# In[57]:


my_array = ([1,2,3,4,5])

for i in my_array:
    print(i)


# # 2. Access individual elements through indexes

# In[58]:


print("Step 2")
print(my_array[3])


# # 3. Append any value to the array using append() method

# In[59]:


print("Step 3")
my_array.append(6)
print(my_array)


# # 4. Insert value in an array using insert() method

# In[60]:


print("Step 4")
my_array = (3, 11)
print(my_array)


# # 5. Extend python array using extend() method

# In[61]:


print("Step 5")
my_array = ('i', [10,11,12])
my_array = (my_array)
print(my_array)


# # 6. Add items from list into array using fromlist() method

# In[62]:


print("Step 6")
tempList = [20,21,22]
(tempList)
print(my_array)


# # 7. Remove any array element using remove() method

# In[63]:


print("Step 7")
my_array.remove(11)
print(my_array)


# # 8. Remove last array element using pop() method

# In[64]:


print("Step 8")
my_array.pop()
print(my_array)


# # 9. Fetch any element through its index using index() method

# In[65]:


print("Step 9")
print(my_array.index(21))


# # 10. Reverse a python array using reverse() method

# In[66]:


print("Step 10")
my_array.reverse()
print(my_array)


# # 11. Get array buffer information through buffer_info() method

# In[67]:


print("Step 11")
print(my_array.buffer_info())


# # 12. Check for number of occurrences of an element using count() method

# In[68]:


print("Step 12")
my_array.append(11)
print(my_array.count(11))
print(my_array)


# # 13. Convert array to string using tostring() method

# In[69]:


print("Step 13")
strTemp = my_array.tostring()
print(strTemp)
ints = array('i')
ints.fromstring(strTemp)
print(ints)


# # 14. Convert array to a python list with same elements using tolist() method

# In[70]:


print("Step 14")
print(my_array.tolist())


# # 16. Slice Elements from an array

# In[71]:


print("Step 16")
print(my_array[:])


# In[ ]:




