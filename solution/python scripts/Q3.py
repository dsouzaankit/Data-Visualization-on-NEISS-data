
# coding: utf-8

# ## Analysis 3
# 1. What diagnosis had the highest hospitalization rate? 
# 2. What diagnosis most often concluded with the individual leaving without being seen?

# Assumptions:
# 
# 1. For part 1, disposition/diagnosis code = 4 (Considered as the patient is hospitalized)
# 2. For part 2, disposition/diagnosis code = 6 (Left without being seen)

# In[2]:


#Importing required packages
import pandas as pd


# In[3]:


#Reading the required files
df1=pd.read_csv(r"NEISS data/NEISS2014.csv")
df2=pd.read_csv(r"NEISS data/DiagnosisCodes.csv")


# In[7]:


df3=pd.merge(df1,df2,how="left", left_on="diag",right_on="Code")


# In[8]:


#Filtering only cases people have been hospitalized
df4=df3[(df3['disposition']==4)]


# In[24]:


#Calculating count of people hospitalized for every diagnosis
df5=df4.groupby('Diagnosis')['Diagnosis'].agg(['count']).reset_index()
df5=df5.rename(columns={'count':'Count - Hospitalized'})
#Calculating count of total people  for every diagnosis 
df6=df3.groupby('Diagnosis')['Diagnosis'].agg(['count']).reset_index()
df6=df6.rename(columns={'count':'Total Count'})


# In[38]:


df7=pd.merge(df5,df6,how="left", on="Diagnosis")
print(df7.head())


# In[39]:


#Calculating rate
df7['Rate (%)']=(df7['Count - Hospitalized']/df7['Total Count'])*100


# In[40]:


#Sorting based on rate
df8=df7.sort_values('Rate (%)',ascending=False).reset_index(drop=True)
df8.head()


# In[41]:


#Filtering only cases people have left without being seen
df9=df3[(df3['disposition']==6)]


# In[42]:


#Calculating  count of people leaving without being seen for every diagnosis
df10=df9.groupby('Diagnosis')['Diagnosis'].agg(['count']).reset_index()
df10=df10.rename(columns={'count':'Count - Left without being seen'})
#Calculating  count of total people  for every diagnosis 
df11=df3.groupby('Diagnosis')['Diagnosis'].agg(['count']).reset_index()
df11=df11.rename(columns={'count':'Total Count'})


# In[43]:


df12=pd.merge(df10,df11,how="left", on="Diagnosis")


# In[44]:


df12['Rate (%)']=(df12['Count - Left without being seen']/df12['Total Count'])*100


# In[45]:


df13=df12.sort_values('Rate (%)',ascending=False).reset_index(drop=True)
df13.head()


# ### Conclusion

# * People who drowned and those with fractures get admitted since their injuries can't be easily self-treated or cured quickly. 
# * People with poisoning and foreign objects may leave without being seen if their injury is not serious enough for admission or they are unhappy with suggested treatment cost.
# * For some radiation or chemical burns, people may believe they can be cured without professional medical attention.
# 
# 
