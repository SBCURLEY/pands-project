# analysis.py
#
# Author: Sharon Curley

# Data Frames
import pandas as pd

# Plot data
import matplotlib.pyplot as plt

# Numerical arrays
import numpy as np



df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")             # Reading the dataset “Irisdata.csv”.

#print(df.head())                                                   # Displays the top rows of the dataset with their columns.    

#print(df.sample(10))                                               # Displays the number of rows randomly. 

#print(df.columns)                                                  # Displays the number of columns and names of the columns. 

#print(df)                                                          # Displays the dataset.

#print(df.shape)                                                    # Displays the shape of the dataset.

#print(df.describe())                                               # Displays stats about the dataset.              

#print(df.dtypes)

#df.info()                                                          # Displays basic info about the dataset   

# Filtering: Displaying the specific rows using “iloc” and “loc” functions. 
# The “loc” functions use the index name of the row to display the particular row of the dataset.
# The “iloc” functions use the index integer of the row, which gives complete information about the row. 

print(df.iloc[5])                                                   # prints row 5 which is row 7 in my data csv