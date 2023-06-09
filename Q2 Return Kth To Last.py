#!/usr/bin/env python
# coding: utf-8

# # QUESTION 2 Return Kth To Last 

# In[8]:


from LinkedList import LinkedList

def nthToLast(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head

    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print(nthToLast(customLL, 3))


# In[ ]:




