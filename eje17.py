#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


data = np.loadtxt("eje17.dat")
plt.figure()
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig("resultado.png")


# In[ ]:




