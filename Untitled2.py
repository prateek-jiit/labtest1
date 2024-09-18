#!/usr/bin/env python
# coding: utf-8

# In[33]:


import numpy as np
import matplotlib.pyplot as plt


# In[25]:


import numpy as np

data = np.array([
    [30,32,31,29,28,27,26],
    [35,34,36,33,32,31,30],
    [25,26,27,28,29,30,31],
    [22,23,24,25,26,27,28]
])
data.shape


# In[22]:


for i in range(4):
    print(f"Average temp of each City {i+1}: {np.sum(data[i][:])/7}")


# In[24]:


for i in range(4):
    print(f"Max temp of each City {i+1}: {np.max(data[i][:])}")


# In[26]:


for i in range(4):
    print(f"Min temp of each City {i+1}: {np.min(data[i][:])}")


# In[31]:


def Avg_Temp(x):
    n = x[1]
    for i in range(n):
        print(f"Avg temp of across cities on day {i+1}: {np.sum(data[:,i]/4)}")


# In[32]:


Avg_Temp(x)


# In[78]:


y = [1,2,3,4,5,6,7]
for i in range(4):
    X = data[i][:]
    plt.plot(y,X)
    plt.xlabel(f"City{i+1}")
    plt.ylabel("Day")
plt.show()
    


# In[68]:


X = data[i][:]
# X.resize(7)
X.shape
len(y)
var = [1,2,3,4]


# In[69]:


for i in range(4):
    max_t = np.max(data[i][:])
    min_t = np.min(data[i][:])
    print(f"Variance of Temp in City {i+1}: {max_t - min_t}")
    var[i] = max_t - min_t


# In[75]:


var[0]
n = [1,2,3,4]


# In[77]:


plt.bar(n,var)


# In[ ]:




