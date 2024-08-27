#!/usr/bin/env python
# coding: utf-8

# ___
# Mr. Yogesh P Murumkar (965708095)
# 
# www.youtube.com/yogeshmurumkar
# ___
# # Ecommerce Purchases Exercise
# 
# In this Exercise you will be given some Fake Data about some purchases done through Amazon! Just go ahead and follow the directions and try your best to answer the questions and complete the tasks. Feel free to reference the solutions. Most of the tasks can be solved in different ways. For the most part, the questions get progressively harder.
# 
# Please excuse anything that doesn't make "Real-World" sense in the dataframe, all the data is fake and made-up.
# 
# Also note that all of these questions can be answered with one line of code.
# ____
# ** Import pandas and read in the Ecommerce Purchases csv file and set it to a DataFrame called ecom. **

# In[1]:


import pandas as pd


# In[4]:


df=pd.read_csv("C:/Users/anujd/Downloads/Ecommerce Purchases")
df


# **Check the head of the DataFrame.**

# In[5]:


df.head()


# ** How many rows and columns are there? **

# In[6]:


df.shape


# ** What is the average Purchase Price? **

# In[8]:


df['Purchase Price'].mean()


# ** What were the highest and lowest purchase prices? **

# In[10]:


df['Purchase Price'].max()


# In[11]:


df['Purchase Price'].min()


# ** How many people have English 'en' as their Language of choice on the website? **

# In[12]:


df[df['Language']=='en'].count()


# ** How many people have the job title of "Lawyer" ? **
# 

# In[13]:


df[df['Job'] == 'Lawyer'].info()


# ** How many people made the purchase during the AM and how many people made the purchase during PM ? **
# 
# **(Hint: Check out [value_counts()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html) ) **

# In[14]:


df['AM or PM'].value_counts()


# ** What are the 5 most common Job Titles? **

# In[28]:


df['Job'].value_counts().head()


# ** Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction? **

# In[16]:


df[df['Lot']=='90 WT']['Purchase Price']


# ** What is the email of the person with the following Credit Card Number: 4926535242672853 **

# In[22]:


df[df["Credit Card"] == 4926535242672853 ]['Email']


# ** How many people have American Express as their Credit Card Provider *and* made a purchase above $95 ?**

# In[23]:


df[(df['CC Provider']=='American Express') & (df['Purchase Price']>95)].count()


# ** Hard: How many people have a credit card that expires in 2025? **

# In[24]:


sum(df['CC Exp Date'].apply(lambda x: x[3:]) == '25')


# ** Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...) **

# In[27]:


df['Email'].apply(lambda x: x.split('@')[1]).value_counts().head()


# # Great Job!
