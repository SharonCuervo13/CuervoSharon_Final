# In[1]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


n_puntos=10**5
xk = np.loadtxt('valores.txt')
sigma=1.0


# In[3]:


def probabilidad(xk,sigma):
    prob=(1.0/sigma*np.sqrt(2.0*np.pi()))*np.exp((-1.0/2.0)*((xk**2.0)/(sigma**2)))
    return prob
    


# In[ ]:





# In[15]:


plt.figure()
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("valor medio= y desviación estandar=")
plt.savefig("sigma.png")


# In[ ]:




