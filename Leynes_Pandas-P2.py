#!/usr/bin/env python
# coding: utf-8

# # Programming Experiment 3.2

# # Python Data Analysis (PANDAS)
# #### This jupyter notebook contains (1) problem that utilizes Pyhton3 - PANDAS library
# Github Repository: https://github.com/ramongerix/ECE2112-EX3

# #### --------------------------------------------------------------------------------------------------------------

# ### Problem (2) 

# In[195]:


#to have an access to the pandas library 
import pandas as pd


# In[13]:


#Load the cars.csv csv file into a data frame using pandas.
cars = pd.read_csv('cars.csv')
cars


# #### Utilizing the dataframe provided in Problem 1, this problem will extract the following information through a combination of subsetting, slicing, and indexing operations.
# ### (Problem 2A) Display the first five rows with odd-numbered (columns 1, 3, 5, 7...) of cars.

# In[44]:


#this function displays the initial five rows of the resulting cars and selects only the odd columns of columns 1, 3, 5, and 7 using position slicing.
#using variable "cars" followed by a (.) dot "iloc" to select variables by rows/column and at the code ":5 means it will display only first 5 rows".
#, "while 1::2, "1" indicates it will start at column 1 which is an odd number, "::2" skips even numbered columns, effectively selected odd-column numbers.
cars.iloc[:5, 1::2]
cars


# ### (Problem 2B) Display the row that contains the ‘Model’ of ‘Mazda RX4’.

# #### v1 of (2B)

# In[192]:


#using ".head" will display a more concise and minimal output by using datframe ui. 
cars.head(1)


# #### v2 of (2B)

# In[190]:


#using subsetting function to slice and index the first row

#using "cars1" as a seperate function to use as a data in subsetting
cars1 = pd.DataFrame(cars)

#subsetting the first row using slicing and indexing
first_row = cars1.iloc [0:1] 
print(first_row)


# ### (2C) How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

# #### [V1 of 2C] in this code it will display only the "cyl" column using "by position" selecting
# 

# In[304]:


cars.iloc[[23],[2]]


# #### [V2 of 2C] in this code it will display only the "cyl" column using "by label" selecting

# In[315]:


cars.loc[[23],['cyl']]


# #### [V3 of 2C] a more detailed way of showing how many cylinders does the car model Camaro ZS8 have

# In[312]:


cars.loc[[23],['Model', 'cyl']]


# ### (Problem 2D) Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

# #### [V1 of 2D] in this code it will display  the "cyl" and "gear" column using "by position" selecting

# In[289]:


#in this code it will display the "cyl" and "gear" column using "by position" selecting
cars.iloc[[1,28,18],[2, 10]]


# #### [V2 of 2D] a more detailed way of showing how many cylinders and gear does the car models: "Mazda RX4 Wag", "Ford Pantera L" and "Honda Civic" have

# In[329]:


#in this code it will display the "cyl" and "gear" column using "by position" selecting
cars.iloc[[1,28,18],[0, 2, 10]]


# #### --------------------------------------------------------------------------------------------------------------
# #### End of Problem 2, to access Problem 1 click this link to be redirected:
# https://github.com/ramongerix/ECE2112-EX3/blob/main/Leynes_Pandas-P1.py.ipynb
