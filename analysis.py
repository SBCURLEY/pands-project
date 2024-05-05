# analysis.py
# Project: research the dataset, su[poprted by documentation and code. 
# Author: Sharon Curley


# 2. Import Libraries

import pandas as pd                     # for data analysis

import matplotlib.pyplot as plt         # functionality for multidimensional arrays

import numpy as np                      # Essential for creating static, animated, and interactive visualizations in Python

import seaborn as sns                   # Provides a high-level interface for drawing attractive statistical graphics


# 3. Load data

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")             # Reading the dataset “Irisdata.csv”.

print(df.head())                        # Displays the top 5 rows of the dataset with their columns.                                        

print("\n") 

print (df)                              # Displays the dataset

print("\n") 

print (df["species"].value_counts())    # Counts the number of times a particular species has occurred

print("\n") 

# 4. Data Exploration

print (df.info())                       # Displays basic info about the dataset   

print("\n") 

print (df.iloc[0])                      # Filtering: use the index integer of the row, which gives complete information about the row. 

print("\n") 

print (df.describe(include="all"))      # Displays stats about the dataset.   

print("\n")