# analysis.py
# Project: research the dataset, su[poprted by documentation and code. 
# Author: Sharon Curley


# 2. Import Libraries

import pandas as pd                     # for data analysis

import matplotlib.pyplot as plt         # functionality for multidimensional arrays

import numpy as np                      # Essential for creating static, animated, and interactive visualizations in Python

import seaborn as sns                   # Provides a high-level interface for drawing attractive statistical graphics

import io                               # Provides the Python interfaces to stream handling.


# 3. Load data

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")             # Reading the dataset “Irisdata.csv”.

with open("summary.txt", "w") as f:
    print(df.head(), file=f)                        # Displays the top 5 rows of the dataset with their columns.                                        

    print("\n", file=f) 

    print(df, file=f)                               # Displays the dataset

    print("\n", file=f) 

    print(df["species"].value_counts(),file=f)      # Counts the number of times a particular species has occurred

    print("\n", file=f) 

# 4. Data Exploration

    # print(df.info(), file=f)                      # Displays basic info about the dataset but did not work - research another way.

buffer = io.StringIO()                              # This line creates an in-memory buffer using StringIO. This buffer will be used to store the output of df.info()
df.info(buf=buffer)                                 # Pipe output of DataFrame.info to buffer instead of sys.stdout
s = buffer.getvalue()                               # Retrieves the contents of the buffer and stores them in the variable s.
with open("summary.txt", "a",                       # get buffer content and append to a text file:
            encoding="utf-8") as f:                 # This line opens a file named "df_info.txt" in write mode ("w"), specifying UTF-8 encoding.
    f.write(s)                                      # This line writes the contents of the variable s (which holds the DataFrame information) into the opened file.

    print("\n",file=f) 

    print(df.iloc[0], file=f)                      # Filtering: use the index integer of the row, which gives complete information about the row. 

    print("\n", file=f) 

    print(df.describe(include="all"), file=f)      # Displays stats about the dataset.   

    print("\n", file=f)