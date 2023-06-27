#!/usr/bin/env python
# coding: utf-8

# # Activity Selection

# In[1]:


activities = [["A1", 0, 6],
              ["A2", 3, 4],
              ["A3", 1, 2],
              ["A4", 5, 8],
              ["A5", 5, 7],
              ["A6", 8, 9]
                ]


def printMaxActivities(activities):
    activities.sort(key=lambda x: x[2])
    i = 0
    firstA = activities[i][0]
    print(firstA)
    for j in range(len(activities)):
        if activities[j][1] > activities[i][2]:
            print(activities[j][0])
            i = j

printMaxActivities(activities)


# # Coin Change

# In[2]:



def coinChange(totalNumber, coins):
    N = totalNumber
    coins.sort()
    index = len(coins)-1
    while True:
        coinValue = coins[index]
        if N >= coinValue:
            print(coinValue)
            N = N - coinValue
        if N < coinValue:
            index -= 1
        
        if N == 0:
            break

coins = [1,2,5,20,50,100]
coinChange(201, coins)


# # Fractional Knapsack

# In[3]:


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

def knapsackMethod(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse = True)
    usedCapacity = 0
    totalValue = 0
    for i in items:
        if usedCapacity + i.weight <= capacity:
            usedCapacity += i.weight
            totalValue += i.value
        else:
            unusedWeight = capacity - usedCapacity
            value = i.ratio * unusedWeight
            usedCapacity += unusedWeight
            totalValue += value
        
        if usedCapacity == capacity:
            break
    print("Total value obtained: "+str(totalValue))

item1 = Item(20,100)
item2 = Item(30,120)
item3 = Item(10,60)
cList = [item1, item2, item3]

knapsackMethod(cList, 50)


# # Convert String

# In[4]:


def findMinOperation(s1, s2, index1, index2):
    if index1 == len(s1):
        return len(s2)-index2
    if index2 == len(s2):
        return len(s1)-index1
    if s1[index1] == s2[index2]:
        return findMinOperation(s1, s2, index1+1, index2+1)
    else:
        deleteOp = 1 + findMinOperation(s1, s2, index1, index2+1)
        insertOp = 1 + findMinOperation(s1, s2, index1+1, index2)
        replaceOp = 1 + findMinOperation(s1, s2, index1+1, index2+1)
        return min (deleteOp, insertOp, replaceOp)

print(findMinOperation("table", "tbrltt", 0, 0))


# # House Robber

# In[5]:


def houseRobber(houses, currentIndex):
    if currentIndex >= len(houses):
        return 0
    else:
        stealFirstHouse = houses[currentIndex] + houseRobber(houses, currentIndex + 2)
        skipFirstHouse = houseRobber(houses, currentIndex+1)
        return max(stealFirstHouse, skipFirstHouse)

houses = [6,7,1,30,8,2,4]
print(houseRobber(houses, 0))


# # Longest Common

# In[6]:


def findLCS(s1, s2, index1, index2):
    if index1 == len(s1) or index2 == len(s2):
        return 0
    if s1[index1] == s2[index2]:
        return 1 + findLCS(s1, s2, index1+1, index2+1)
    else:
        op1 = findLCS(s1,s2, index1, index2+1)
        op2 = findLCS(s1,s2, index1+1, index2)
        return max(op1, op2)

print(findLCS("elephant", "eretpat", 0, 0))


# # Longest Polindormic

# In[7]:


def findLPS(s, startIndex, endIndex):
    if startIndex > endIndex:
        return 0
    elif startIndex == endIndex:
        return 1
    elif s[startIndex] == s[endIndex]:
        return 2 + findLPS(s, startIndex+1, endIndex-1)
    else:
        op1 = findLPS(s, startIndex, endIndex-1)
        op2 = findLPS(s, startIndex+1, endIndex)
        return max(op1, op2)

print(findLPS("ELRMENMET", 0, 8))


# # Min Cost 2D

# In[8]:


def findMinCost(twoDArray, row, col):
    if row == -1 or col == -1:
        return float('inf')
    elif row == 0 and col == 0:
        return twoDArray[0][0]
    else:
        op1 = findMinCost(twoDArray, row-1, col)
        op2 = findMinCost(twoDArray, row, col-1)
        return twoDArray[row][col] + min(op1,op2)

TwoDList = [[4,7,8,6,4],
           [6,7,3,9,2],
           [3,8,1,2,4],
           [7,1,7,3,7],
           [2,9,8,9,3]
           ]

print(findMinCost(TwoDList, 4,4))


# # Number Factor

# In[9]:


def numberFactor(n):
    if n in (0,1,2):
        return 1
    elif n == 3:
        return 2
    else:
        subP1 = numberFactor(n-1)
        subP2 = numberFactor(n-3)
        subP3 = numberFactor(n-4)
        return subP1+subP2+subP3

print(numberFactor(5))


# # Number of Paths

# In[10]:


def numberOfPaths(twoDArray, row, col, cost):
    if cost < 0:
        return 0
    elif row == 0 and col == 0:
        if twoDArray[0][0] - cost == 0:
            return 1
        else:
            return 0
    elif row == 0:
        return numberOfPaths(twoDArray, 0, col-1, cost - twoDArray[row][col] )
    elif col == 0:
        return numberOfPaths(twoDArray, row-1, 0, cost - twoDArray[row][col] )
    else:
        op1 = numberOfPaths(twoDArray, row -1, col, cost - twoDArray[row][col] )
        op2 = numberOfPaths(twoDArray, row, col-1, cost - twoDArray[row][col] )
        return op1 + op2


TwoDList = [[4,7,1,6],
           [5,7,3,9],
           [3,2,1,2],
           [7,1,6,3]
           ]

print(numberOfPaths(TwoDList, 3,3, 25))


# # Zero One Knapsack

# In[11]:


class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def zoKnapsack(items, capacity, currentIndex):
    if capacity <=0 or currentIndex < 0 or currentIndex >= len(items):
        return 0
    elif items[currentIndex].weight <= capacity:
        profit1 = items[currentIndex].profit + zoKnapsack(items, capacity-items[currentIndex].weight, currentIndex+1)
        profit2 = zoKnapsack(items, capacity, currentIndex+1)
        return max(profit1, profit2)
    else:
        return 0

mango = Item(31, 3)
apple = Item(26, 1)
orange = Item(17, 2)
banana = Item(72, 5)

items = [mango, apple, orange, banana]

print(zoKnapsack(items, 7, 0))


# In[ ]:




