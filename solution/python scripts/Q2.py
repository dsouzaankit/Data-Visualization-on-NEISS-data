
# coding: utf-8

# ## Analysis 2
# 1. How many injuries in this dataset involve a skateboard?
# 2. Of those injuries, what percentage were male and what percentage were female?
# 3. What was the average age of someone injured in an incident involving a skateboard?

# In[1]:


#Importing required packages
import pandas as pd
import matplotlib.pyplot
import seaborn as sb
import numpy as np


# In[2]:


#Reading the required files
df1=pd.read_csv(r"NEISS data/NEISS2014.csv")


# In[3]:


#Filtering only the accidents involving skateboard
#From the documentation, product code for skateboard is 1333. Filtering data if prod1 or prod2 is a skateboard
df2=df1[(df1['prod1']==1333)|(df1['prod2']==1333)]
print(df2.head())


# In[4]:


print("Count of injuries involving a skateboard is "+str((df2.shape[0])))


# ##### Of those injuries, what percentage were male and what percentage were female?

# In[5]:


#Calculating percentage of male and female involved in skateboard accident
df3=df2.groupby(['sex'])['sex'].agg(['count']).reset_index()
print(df3.head())
df3=df3.rename(columns={'count': 'Frequency'})
print(df3.head())


# In[6]:


df3['Percentage']=round((df3['Frequency']/len(df2))*100,2)


# In[7]:


print(df3)


# ##### Alternate method to check skateboard related injuries

# In[8]:


df4=df1[(df1['narrative'].str.contains('SKATEBOARD'))]


# In[9]:


print('The number of injuries involving a skateboard by checking the narrative description is '+str((df4.shape[0])))


# In[10]:


#Calculating percentage of male and female involved in skateboard accident
df5=df4.groupby(['sex'])['sex'].agg(['count']).reset_index()
df5=df5.rename(columns={'count': 'Frequency'})
df5['Percentage']=round((df5['Frequency']/len(df4))*100,2)
print(df5)


# ##### For further analysis, we consider df2 (495 records)

# ##### What was the average age of someone injured in an incident involving a skateboard?

# In[11]:


d = df2['age'].describe()
print(d)


# In[12]:


print("Age ranges from "+str(d['min'])+" to "+str(d['max']))


# In[13]:


#Ages above 115 is coded as 114, lets check if age=114 exists
print('Count of ages over 115 is '+ str(len(np.where(df2['age']==114)[0])))


# In[14]:


#Ages less than 2 years are coded as 200 (2 followed by months) and above
#We can code values greater than 200 as 1 and retain other values 
#Creating a new column for this purpose
df2.loc[df2['age']>=200,'age_year'] = 1
df2.loc[df2['age']<200,'age_year'] = df2['age']


# In[15]:


avgage=round(df2['age_year'].mean(),0)
print('The average age of a person in a skateboard accident is '+str(avgage))

