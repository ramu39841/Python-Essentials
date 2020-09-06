#!/usr/bin/env python
# coding: utf-8

# In[6]:


# list
lst=['ramu',50,20.5,5258,[1,2,3]]


# In[8]:


lst


# In[9]:


lst[4]


# In[11]:


lst[3]


# In[12]:


lst[4][1]


# In[21]:


lst.append("chaitu")


# In[19]:


lst


# In[15]:


lst.index(50)


# In[16]:


lst[-3]


# In[17]:


lst.pop(-5)


# In[20]:


lst.count(5258)


# In[22]:


lst


# In[23]:


lst.count("chaitu")


# In[26]:


lst.insert( 3, 2020)


# In[27]:


lst


# # Dictionaries

# In[28]:


dit= {"name":"ramu", "age":"24","number":123456,'email':'ramu39841@gmail.com'}


# In[29]:


dit


# In[30]:


dit.get('name')


# In[31]:


dit.keys()


# In[32]:


dit.items()


# In[33]:


dit["gender"] = "male"


# In[34]:


dit


# In[35]:


dit.popitem()


# In[36]:


dit


# In[37]:


dit.fromkeys('email')


# In[38]:


dit.get('age')


# # Sets

# In[67]:


set={"ramu","letsupgrade",1,22,33,55,5,55,3}


# In[68]:


set


# In[69]:


set1={"ramu",3}


# In[70]:


set1.issubset(set)


# In[71]:


set()


# In[63]:





# In[65]:





# In[72]:


set.clear()


# In[73]:


set()


# In[74]:


set.clear()


# # tuple

# In[75]:


tpl=("ramu39841",'@','gmail.com')


# In[76]:


tpl


# In[81]:


tpl.index("gmail.com")


# In[79]:


tpl.count("@")


# # Strings

# In[82]:


str='Ramu Chowdary'


# In[83]:


str


# In[84]:


str1="""hello, welcome to the letsUpgrade"""


# In[85]:


str1


# In[86]:


str


# In[87]:


str[0]


# In[88]:


str[-5]


# In[89]:


str[1:-5]


# In[93]:


str.format(str)


# In[94]:


str.format_map(str)


# In[95]:


str.count(str)


# In[98]:


str.casefold()


# In[105]:


str.endswith("y")


# In[ ]:




