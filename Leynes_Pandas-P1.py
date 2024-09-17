#!/usr/bin/env python
# coding: utf-8

# # Programming Experiment 3.1

# # Python Data Analysis (PANDAS)
# #### This jupyter notebook contains (1) problem that utilizes Pyhton3 - PANDAS library
# Github Repository: https://github.com/ramongerix/ECE2112-EX3
# 

# #### --------------------------------------------------------------------------------------------------------------

# ## Problem (1) 

# In[52]:


#to have an access to the pandas library 
import pandas as pd


# ### (Problem 1A) Load the cars.csv csv file into a data frame using pandas.

# In[94]:


#read & load the "cars.csv" csv file into a data frame using pandas
cars = pd.read_csv('cars.csv')
cars


# ### (Problem 1B.1) Displays the first five rows of the resulting cars.

# In[97]:


#displays the first five resulting cars
#using variable "cars" followed by a (.) dot "head" to return the first 5 rows of the given/loaded csv data
cars.head()


# ### (Problem 1B.2) Displays the last five rows of the resulting cars.

# In[69]:


#displays the last five resulting cars
#using variable "cars" followed by a (.) dot "tail" to return the last 5 rows of the given/loaded csv data
cars.tail()


# #### --------------------------------------------------------------------------------------------------------------
# #### End of Problem 1, to access Problem 2 click this link to be redirected:
# https://github.com/ramongerix/ECE2112-EX3/blob/main/Leynes_Pandas-P2.py
