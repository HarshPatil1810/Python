#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# In[2]:


x=np.array([1,2,3,4,5]).reshape(-1,1)
y=np.array([50,55,65,70,75])


# In[3]:


model=LinearRegression()
model.fit(x,y)


# In[4]:


beta_0=model.intercept_
beta_1=model.coef_[0]


# In[5]:


y_pred=model.predict(x)


# In[6]:


plt.scatter(x,y,color='blue')
plt.plot(x,y_pred,color='red')
plt.xlabel('Hours studied')
plt.ylabel('Exam Score')
plt.show()


# In[ ]:




