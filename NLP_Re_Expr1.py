#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
txt = "The rain in india"
x = re.search("^The.*india$", txt)
print(x)


# In[3]:


txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


# In[4]:


txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)


# In[5]:


txt = "The rain in Spain"
x = re.search("Spain", txt)
print(x)


# In[6]:



txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)


# In[7]:


import re

txt = "The rain in Spain"
x = re.findall("[a-m]", txt)
print(x)


# In[8]:


import re

txt = "hello planet"

x = re.findall("he..o", txt)
print(x)


# In[9]:


txt = "hello planet"

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")


# In[10]:



txt = "hello planet"

x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")


# In[11]:


txt = "hello planet"

x = re.findall("he.*o", txt)

print(x)


# In[12]:


txt = "The rain in Spain"

x = re.findall("\AThe", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")


# In[13]:



txt = "The rain in Spain"

x = re.findall("Spain\Z", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")


# In[14]:



txt = "The rain in Spain"

x = re.findall("\d", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# In[15]:



txt = "The rain in Spain 123"

#Check if the string contains any digits (numbers from 0-9):

x = re.findall("\d", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# In[ ]:




