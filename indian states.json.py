#!/usr/bin/env python
# coding: utf-8

# In[2]:


indian_states={
    "Andhra Pradesh": "Amaravati",
    "Bihar": "Patna",
    "Gujarat": "Gandhinagar",
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai",
    "Rajasthan": "Jaipur",
    "Tamil Nadu": "Chennai"
}


# In[4]:


import json


# In[5]:


file=open('indian_states.json', 'w')
json.dump(indian_states, file)

