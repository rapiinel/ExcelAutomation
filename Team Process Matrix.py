#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


link = "C:/Users/Raffie/OneDrive - Legalmatch/Personal/13 Team Process Metrics/"


# Read All CSV raw files from salesforce

# In[3]:


crs = pd.read_csv(link+"CR Sets.csv")
crc = pd.read_csv(link+"CR Completed.csv")
ems = pd.read_csv(link+"EM Set.csv")
deals = pd.read_csv(link+"Deals.csv")


# Remove Timestamp from raw files

# In[4]:


crs_clean = crs.dropna(subset=['Opportunity Name'])
crc_clean = crc.dropna(subset=['Opportunity Name'])
ems_clean = ems.dropna(subset=['Opportunity Name'])
deals_clean = deals.dropna(subset=['Sales Team'])


# Getting needed columns from raw files

# In[5]:


crs_combined = crs_clean[['Process Tracking For','Opportunity Name','Case Review Set']]
crc_combined = crc_clean[['Process Tracking For','Opportunity Name','Case Review Completed']]
ems_combined = ems_clean[['Process Tracking For','Opportunity Name','Enrollment Meeting Set']]
deals_combined = deals_clean[['Allocation Manager','Deal: Deal Name','Order Date','Membership Fee (After Discount)']]


# In[6]:


#Renaming deals header to match other raw files
deals_combined = deals_combined.rename(columns={'Allocation Manager':'Process Tracking For',
                                               'Deal: Deal Name':'Opportunity Name'})


# Concatinating all the raw files

# In[7]:


frames= [crs_combined,crc_combined,ems_combined,deals_combined]
final_combined = pd.concat(frames,axis = 0,join='outer',sort=False)


# In[8]:


#dropping the index after concat since this will keep the previous index of the merged dataframes
final_combined.reset_index(drop=True, inplace=True)


# Removing entries with "Test" keywords"

# In[9]:


#converting all entries in oppty. col to lower case to get test keyword
final_combined['Opportunity Name'] = final_combined['Opportunity Name'].str.lower()
final_combined = final_combined[~final_combined['Opportunity Name'].str.contains('test')]


# In[10]:


#Reading master teamlist for checking sales team
teamList = pd.read_csv(link+'Team List.csv')
teamList = teamList[['Full Name','Team']]


# In[11]:


#Reseting index to be used later for the resorting of the data, since if DF is joined with another DF it will be automatically
# sorted
final_combined.reset_index(inplace=True)
final_combined.sort_values(by=['index'],ascending = True,inplace=True)
final_combined = final_combined.rename(columns={'index':'id'})


# In[12]:


#Joining the combined raw file to the teamlist to imitate the lookup function in excel to get updated teamlist's sales team
combined_wTeamList = final_combined.set_index('Process Tracking For').join(teamList.set_index('Full Name'),how='left')
#resorting the entries to make the DF entries return to previous sequence
combined_wTeamList.sort_values(by=['id'],ascending=True,inplace=True)


# In[13]:


#During the join process, the process tracking for was used as an index, this part will reset the process tracking for
combined_wTeamList.reset_index(inplace=True)
combined_wTeamList.set_index('id',inplace=True)
combined_wTeamList.rename(columns={'index':'Process Tracking For'}, inplace=True)


# In[14]:


#Rearrange the columns then save as csv in link provided above
combined_wTeamList = combined_wTeamList[['Process Tracking For','Team','Opportunity Name','Case Review Set',
                    'Case Review Completed','Enrollment Meeting Set',
                   'Order Date','Membership Fee (After Discount)']]
combined_wTeamList.to_csv(link+'final_combined.csv',index = False, header = True)


# In[15]:


#Will check if there is a sales rep that is not included in master list then save the list as csv name "Sales Teamlist Update"
sales_update = combined_wTeamList[combined_wTeamList['Team'].isna()]
sales_update = sales_update['Process Tracking For']
sales_update = set(sales_update)
sales_update = list(sales_update)
df_sales_update = pd.DataFrame({'Sales Rep For Update': sales_update})
df_sales_update.to_csv(link+'Sales Teamlist Update.csv', index = False)


# In[ ]:




