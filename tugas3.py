#!/usr/bin/env python
# coding: utf-8

# # Interview question 1

# In[10]:


def sum_of_digits(n):
    assert n >= 0 and int(n) == n
    if n in [0]:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)
n = 56
print(sum_of_digits(n))


# # Interview question 2

# In[13]:


def power(x, n):
    assert type(x) == int and x >= 0
    assert type(n) == int and n >= 0
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(x*x, n//2)
    else:
        return x * power(x*x, (n-1)//2)
x = 2
n = 3
print(power(x, n))


# # Interview question 3

# In[15]:


def gcd(a, b):
    assert isinstance(a, int) and a >= 0
    assert isinstance(b, int) and b >= 0
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
a = 24
b = 8
print(gcd(a, b))


# # Interview question 4

# In[18]:


def decimal_to_binary(n):
    assert isinstance (n, int) and n >= 0
    if n == 0:
        return 0
    else:
        return (n % 2) + 10 * decimal_to_binary(n // 2)
n = 164
print(decimal_to_binary(n))


# In[ ]:




