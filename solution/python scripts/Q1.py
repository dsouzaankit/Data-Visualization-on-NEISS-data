
# coding: utf-8

# # Analysis 1
#  
# 1. What are the top three body parts most frequently represented in this dataset?
# 2. What are the top three body parts that are least frequently represented?

# In[46]:


#Importing required packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


# In[58]:


#Reading the required files
df1=pd.read_csv(r"NEISS data/NEISS2014.csv")
df2=pd.read_csv(r"NEISS data/BodyParts.csv")
print(df1.head())
print(df2.head())


# In[59]:


#Performing a left join to combine the body part code of df1 with the body part name in df2
df3=pd.merge(df1,df2, how="left", left_on="body_part",right_on="Code")


# In[60]:


#Filtering data which has the value 'Not Recorded' since that is data which does not have recorded data
df3=df3[(df3['BodyPart']!='Not Recorded')]


# In[61]:


#Calculating frequency of occurence of each body part
df4=df3.groupby("BodyPart")['BodyPart'].agg(['count'])
print(df4.head())
df4=df4.reset_index().rename(columns={'count': 'Frequency'})
print(df4.head())


# In[62]:


#Sorting the values based on frequency
df5=df4.sort_values(['Frequency'],ascending=False)
print(df5.head())
df5=df5.reset_index(drop=True)
print(df5.head())


# In[63]:


#Selecting top three body parts based on frequency
df6=df5.head(3)
print("Top three body parts most frequently represented in this dataset")
print(df6)


# In[64]:


#Selecting bottom three body parts based on frequency
df7=df5.tail(3)
print("Top three body parts least frequently represented in this dataset")
print(df7)


# In[65]:


#Selecting top three and botton three in a single statement
df7 = df5.iloc[np.r_[0:3, -3:0]]
print(df7)


# In[66]:


# Visualizing frequency of occurence of body parts represented in this dataset
v1=df5.head()
v2=df5.tail()


# In[67]:


g=sb.factorplot(x="BodyPart", y="Frequency",
                               data=v1, kind="bar",
                               size=9, palette="muted")

plt.title('Body Parts Occurence Frequency (Top 10)')
plt.xlabel('Body Part Name')
plt.ylabel('Frequency of Occurence')
plt.show()


# In[68]:


g=sb.factorplot("BodyPart", "Frequency",
                               data=v2, kind="bar",
                               size=9, palette="muted")

plt.title('Body Parts Occurence Frequency (Bottom 10)')
plt.xlabel('Body Part Name')
plt.ylabel('Frequency of Occurence')
plt.show()

