#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


link = "C:/Users/Raffie/OneDrive - Legalmatch/Personal/13 Team Process Metrics/"


# In[3]:


crs = pd.read_csv(link+"CR Sets.csv")
crc = pd.read_csv(link+"CR Completed.csv")
ems = pd.read_csv(link+"EM Set.csv")
deals = pd.read_csv(link+"Deals.csv")


# In[4]:


crs_clean = crs.dropna(subset=['Opportunity Name'])
crs_clean.tail(10)


# In[5]:


crc_clean = crc.dropna(subset=['Opportunity Name'])
crc_clean.tail(10)


# In[6]:


ems_clean = ems.dropna(subset=['Opportunity Name'])
ems_clean.tail(10)


# In[7]:


deals_clean = deals.dropna(subset=['Sales Team'])
deals_clean.tail(10)


# In[8]:


combined = pd.DataFrame(columns=['Process Tracking For','Sales Team','Opportunity Name',
                                'Case Review Set', 'Case Review Completed', 'Enrollment Meeting Set',
                                'Order Date','Membership Fee (After Discount)'])


# In[10]:


crs_combined = crs_clean[['Process Tracking For','Opportunity Name','Case Review Set']]
crs_combined.head(10)


# In[12]:


crc_combined = crc_clean[['Process Tracking For','Opportunity Name','Case Review Completed']]
crc_combined.head(10)


# In[13]:


ems_combined = ems_clean[['Process Tracking For','Opportunity Name','Enrollment Meeting Set']]
ems_combined.head(5)


# In[ ]:




