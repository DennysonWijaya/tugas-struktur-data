#!/usr/bin/env python
# coding: utf-8

# In[11]:


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


# In[2]:


node1 = BinaryTreeNode(50)
node2 = BinaryTreeNode(20)
node3 = BinaryTreeNode(45)
node4 = BinaryTreeNode(11)
node5 = BinaryTreeNode(15)
node6 = BinaryTreeNode(30)
node7 = BinaryTreeNode(78)


# In[3]:


node1.leftChild = node2
node1.rightChild = node3
node2.leftChild = node4
node2.rightChild = node5
node3.leftChild = node6
node3.rightChild = node7


# In[4]:


print("Root Node is:")
print(node1.data)


# In[5]:


print("left child of the node is:")
print(node1.leftChild.data)


# In[6]:


print("right child of the node is:")
print(node1.rightChild.data)


# In[7]:


print("Node is:")
print(node2.data)


# In[8]:


print("left child of the node is:")
print(node2.leftChild.data)


# In[9]:


print("right child of the node is:")
print(node2.rightChild.data)


# In[10]:


print("Node is:")
print(node3.data)


# In[12]:


print("left child of the node is:")
print(node3.leftChild.data)


# In[13]:


print("right child of the node is:")
print(node3.rightChild.data)


# In[25]:


print("Node is:")
print(node4.data)


# In[26]:


print("left child of the node is:")
print(node4.leftChild)


# In[15]:


print("right child of the node is:")
print(node4.rightChild)


# In[16]:


print("Node is:")
print(node5.data)


# In[17]:


print("left child of the node is:")
print(node5.leftChild)


# In[18]:


print("right child of the node is:")
print(node5.rightChild)


# In[19]:


print("Node is:")
print(node6.data)


# In[20]:


print("left child of the node is:")
print(node6.leftChild)


# In[21]:


print("right child of the node is:")
print(node6.rightChild)


# In[22]:


print("Node is:")
print(node7.data)


# In[23]:


print("left child of the node is:")
print(node7.leftChild)


# In[24]:


print("right child of the node is:")
print(node7.rightChild)

