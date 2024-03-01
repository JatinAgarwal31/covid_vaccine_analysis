#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("D:/resume projects/DSBDA covid vaccine/archive/covid_vaccine_statewise.csv")
print(df.shape)


# In[3]:


# Describing the dataset
print("\nThe dataset can be described as\n")
print(df.describe())


# In[4]:


# Printing mean of columns
print("\nThe mean of columns of dataset is\n")
print(df.mean(skipna=True, numeric_only=True))


# In[5]:


# Printing count of columns
print("\nThe count of columns of dataset is\n")
print(df.count())


# In[6]:


print("\nThe head of dataset is\n")
print(df.head())


# In[8]:


# Grouping dataset state wise
# Take user input as state from user
state = input("Enter the state name you want to search for first dose: ")
print("\n")
df1 = df.groupby('State').get_group(state)
print(df1)


# In[9]:


if (state in df['State'].values):
 # Printing total first doses in user entered state
 firstSum = df1['First Dose Administered'].sum()
 print("Total first doses in state " + state + " are", firstSum, "\n")
 # Printing total second doses in user entered state
 secondSum = df1['Second Dose Administered'].sum()
 print("Total second doses in state " + state + " are", secondSum, "\n")
else:
 print("Invalid State Name")


# In[10]:


# Printing total male doses administered
malesDoses = df1['Male (Doses Administered)'].sum()
print("Total male doses are:", malesDoses, "\n")
# Printing total female doses administered
femaleDoses = df1['Female (Doses Administered)'].sum()
print("Total female doses are:", femaleDoses)


# In[ ]:




