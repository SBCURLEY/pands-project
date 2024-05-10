# analysis.py
# Project: research the dataset, supported by documentation and code. 
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
    
    print("Top 5 rows of the dataset with their columns using df.head(): \n",file=f)
    
    print(df.head(), file=f)                        # Displays the top 5 rows of the dataset with their columns.                                        

    print("\n", file=f) 

    print("The following displays the dataset using df(): \n",file=f)

    print(df, file=f)                               # Displays the dataset

    print("\n", file=f) 

    print("Below is the three class or species types of iris in the data set: \n",file=f)

    print(df["species"].value_counts(),file=f)      # Counts the number of times a particular species has occurred

    print("\n", file=f) 

# 4. Data Exploration

    # print(df.info(), file=f)                      # Displays basic info about the dataset but did not work - research another way.

    print(f"A concise summary of the iris DataFrame using df.info(): \n",file=f)

buffer = io.StringIO()                              # This line creates an in-memory buffer using StringIO. This buffer will be used to store the output of df.info()
df.info(buf=buffer)                                 # Pipe output of DataFrame.info to buffer instead of sys.stdout
s = buffer.getvalue()                               # Retrieves the contents of the buffer and stores them in the variable s.
with open("summary.txt", "a",                       # get buffer content and append to a text file:
            encoding="utf-8") as f:                 # This line opens a file named "df_info.txt" in write mode ("w"), specifying UTF-8 encoding.
    f.write(s)                                      # This line writes the contents of the variable s (which holds the DataFrame information) into the opened file.

    print("\n",file=f) 

    print("Filter the data by row for detailed information using df.iloc(): \n ",file=f)
    
    print(df.iloc[0], file=f)                      # Filtering: use the index integer of the row, which gives complete information about the row. 

    print("\n", file=f) 

    print("Here are some summary statistics for the iris DataFrame using df.describe(): \n ",file=f)

    print(df.describe(include="all"), file=f)      # Displays stats about the dataset.   

    print("\n", file=f)

    print("The number of null or missing values in the iris DataFrame for each column using df.isnull(): ",file=f)

    print("\n", file=f)

    print(df.isnull().sum().sum(), file=f)
    
    print("\n", file=f)
    
    print(df.isnull().sum(),file=f)
    
    
    
# iris_histogram_sepal_length.png    
df.hist("sepal_length",                         # Creating a Histogram only of Sepal Length "iris_histogram_sepal_length.png"             
ec = "black",                                   # The ec (edge color) parameter define an edge on each bar with black outline.
lw = 1.0,                                       # The lw (line width) can be increased
color ="blueviolet",                             # The color parameter sets the color of the bars in the histogram.
alpha = 0.9,                                    # The alpha parameter sets the transparency of the bars.
label="Sepal Length")                           # Creating a Histogram only of Sepal Length

plt.title ("Histogram of Sepal Length",         # Sets the title name
fontsize=18,                                    # font size = controls the size of the font and sets it to 18.
loc="center",                                   # loc = The location of the title can be ‘center’, ‘left’, ‘right’.
horizontalalignment="center",                   # You can adjust with horizontal alignment ('center', 'right', 'left').
verticalalignment="bottom",                     # the vertical alignment ('top', 'bottom', 'center', 'baseline')
fontweight="bold",                              # font weight = controls the weight of the font - bold                      
family="monospace")                             # family = controls the font family of the font - monospace


plt.xlabel("Sepal Length in cm",                # Sets the label for the x-axis
fontsize=13,                                    # font size = controls the size of the font and sets it to 15
style="italic",                                 # style = controls the style of the font - italic
family="monospace")                             # family = controls the font family of the font - monospace                       

plt.ylabel("Count",                             # Sets the label for the y-axis
fontsize=13,                                    # font size = controls the size of the font and sets it to 15
style="italic",                                 # style = controls the style of the font - italic
family="monospace")                             # family = controls the font family of the font - monospace.

plt.grid(alpha=0.75)                            # Set a grid with transparency of 0.75

# plt.legend(loc="best")                        # show one attribute, comment out

plt.savefig("iris_histogram_sepal_length.png")  



# iris_histogram_sepal_width.png
df.hist("sepal_width",                          # Creating a Histogram only of Sepal Width = "iris_histogram_sepal_width.png"         
ec = "black",                                   # The ec (edge color) parameter define an edge on each bar with black outline.
lw = 1.0,                                       # The lw (line width) can be increased
color ="fuchsia",                                # The color parameter sets the color of the bars in the histogram.
alpha = 0.9,                                    # The alpha parameter sets the transparency of the bars.
label="Sepal Width")                            # Creating a Histogram only of Sepal Width

plt.title ("Histogram of Sepal Width",          # Sets the title name
fontsize=18,                                    # font size = controls the size of the font and sets it to 18.
loc="center",                                   # loc = The location of the title can be ‘center’, ‘left’, ‘right’.
horizontalalignment="center",                   # You can adjust with horizontal alignment ('center', 'right', 'left').
verticalalignment="bottom",                     # the vertical alignment ('top', 'bottom', 'center', 'baseline')
fontweight="bold",                              # font weight = controls the weight of the font - bold                      
family="monospace")                             # family = controls the font family of the font - monospace


plt.xlabel("Sepal Width in cm",                 # Sets the label for the x-axis
fontsize=13,                                    # font size = controls the size of the font and sets it to 15
style="italic",                                 # style = controls the style of the font - italic
family="monospace")                             # family = controls the font family of the font - monospace                       

plt.ylabel("Count",                             # Sets the label for the y-axis
fontsize=13,                                    # font size = controls the size of the font and sets it to 15
style="italic",                                 # style = controls the style of the font - italic
family="monospace")                             # family = controls the font family of the font - monospace.

plt.grid(alpha=0.75)                            # Set a grid with transparency of 0.75

# plt.legend(loc="best")                        # show one attribute, comment out

plt.savefig("iris_histogram_sepal_width.png")  



# iris_histogram_petal_length.png    
df.hist("petal_length",                         # Creating a Histogram only of Petal Length "iris_histogram_petal_length.png"             
ec = "black",                                   # The ec (edge color) parameter define an edge on each bar with black outline.
lw = 1.0,                                       # The lw (line width) can be increased
color ="rebeccapurple",                                  # The color parameter sets the color of the bars in the histogram.
alpha = 0.9,                                    # The alpha parameter sets the transparency of the bars.
label="Sepal Length")                           # Creating a Histogram only of Sepal Length

plt.title ("Histogram of Petal Length",         # Sets the title name
fontsize=18,                                    # font size = controls the size of the font and sets it to 18.
loc="center",                                   # loc = The location of the title can be ‘center’, ‘left’, ‘right’.
horizontalalignment="center",                   # You can adjust with horizontal alignment ('center', 'right', 'left').
verticalalignment="bottom",                     # the vertical alignment ('top', 'bottom', 'center', 'baseline')
fontweight="bold",                              # font weight = controls the weight of the font - bold                      
family="monospace")                             # family = controls the font family of the font - monospace


plt.xlabel("Petal Length in cm",                # Sets the label for the x-axis
fontsize=13,                                    # font size = controls the size of the font and sets it to 15
style="italic",                                 # style = controls the style of the font - italic
family="monospace")                             # family = controls the font family of the font - monospace                       

plt.ylabel("Count",                             # Sets the label for the y-axis
fontsize=13,                                    # font size = controls the size of the font and sets it to 15
style="italic",                                 # style = controls the style of the font - italic
family="monospace")                             # family = controls the font family of the font - monospace.

plt.grid(alpha=0.75)                            # Set a grid with transparency of 0.75

# plt.legend(loc="best")                        # show one attribute, comment out

plt.savefig("iris_histogram_petal_length.png")  



# iris_histogram_petal_width.png
df.hist("petal_width",                          # Creating a Histogram only of Petal Width = "iris_histogram_petal_width.png"         
ec = "black",                                   # The ec (edge color) parameter define an edge on each bar with black outline.
lw = 1.0,                                      # The lw (line width) can be increased
color ="palevioletred",                             # The color parameter sets the color of the bars in the histogram.
alpha = 0.9,                                    # The alpha parameter sets the transparency of the bars.
label="Petal Width")                            # Creating a Histogram only of Sepal Width

plt.title ("Histogram of Petal Width",          # Sets the title name
fontsize=18,                                    # font size = controls the size of the font and sets it to 18.
loc="center",                                   # loc = The location of the title can be ‘center’, ‘left’, ‘right’.
horizontalalignment="center",                   # You can adjust with horizontal alignment ('center', 'right', 'left').
verticalalignment="bottom",                     # the vertical alignment ('top', 'bottom', 'center', 'baseline')
fontweight="bold",                              # font weight = controls the weight of the font - bold                      
family="monospace")                             # family = controls the font family of the font - monospace


plt.xlabel("Sepal Width in cm",                 # Sets the label for the x-axis
fontsize=13,                                    # font size = controls the size of the font and sets it to 15
style="italic",                                 # style = controls the style of the font - italic
family="monospace")                             # family = controls the font family of the font - monospace                       

plt.ylabel("Count",                             # Sets the label for the y-axis
fontsize=13,                                    # font size = controls the size of the font and sets it to 15
style="italic",                                 # style = controls the style of the font - italic
family="monospace")                             # family = controls the font family of the font - monospace.

plt.grid(alpha=0.75)                            # Set a grid with transparency of 0.75

# plt.legend(loc="best")                        # show one attribute, comment out

plt.savefig("iris_histogram_petal_width.png")  

plt.close("all")                                # closing all previous open plots. 


# Plot a boxplot
palette = {"setosa": "darkturquoise",           # defining the colours for each species
        "versicolor": "blue", 
        "virginica": "darkviolet"
        }

f, axes = plt.subplots(2, 2,                    # sets four plots are being plotted on a 2 by 2 grid.
            sharey=False,                       # y-axis scales will not be shared among the subplots, default is true
            figsize=(12, 8)                     # set figure size
            )   

sns.boxplot(x="species",                        # create boxplot for species       
            y="petal_length",                   # and petal_length
            palette=palette,                    # palette as per species above
            data=df,                            # data source is the dataframe
            ax = axes[0,0])                     # ax parameter specifies the subplot where each boxplot will be drawn.                      

sns.boxplot(x="species",                        # create boxplot for species   
            y="sepal_length",                   # and sepal_length
            palette=palette,                    # palette as per species above
            data=df,                            # data source is the dataframe
            ax=axes[0,1])                       # ax parameter specifies the subplot where each boxplot will be drawn.

sns.boxplot(x="species",                        # create boxplot for species
            y="petal_width",                    # and petal_width 
            palette=palette,                    # palette as per species above
            data=df,                            # data source is the dataframe
            ax=axes[1,0])                       # ax parameter specifies the subplot where each boxplot will be drawn.

sns.boxplot(x="species",                        # create boxplot for species
            y="sepal_width",                    # and sepal_width
            palette=palette,                    # palette as per species above
            data=df,                            # data source is the dataframe
            ax=axes[1,1])                       # ax parameter specifies the subplot where each boxplot will be drawn.

f.suptitle("Boxplot of the Iris Petal and Sepal measurements", # set title
        fontsize=18,                            # font size = controls the size of the font and sets it to 18.
        fontweight="bold",                      # font weight = controls the weight of the font - bold                      
        family="monospace")                     # family = controls the font family of the font - monospace)

plt.savefig("iris_boxplot")                     # save to png.

plt.close("all")                                # closing all previous open plots. 


# PCC (Pearson correlation coefficient)

with open("summary.txt", "a") as f:             # open the summary.txt for amend
    f.write(s)                                  # write to f

    print("\n", file=f)                         # space line
    
    print("The following displays the Pearson correlation coefficient: \n", file=f)

    print(df[["petal_length", "petal_width", "sepal_length", "sepal_width"]].corr(),file=f)  # Correlation

    print("\n", file=f)


# Heatmap using Seaborn

correlation_df = df[["petal_length", "petal_width", "sepal_length", "sepal_width"]].corr()

axis_corr = sns.heatmap(        # create a heatmap using Seaborn's heatmap function
    correlation_df,             # define what data to use
    vmin=-1,                    # set variable min to -1
    vmax=1,                     # set variable max to 1
    center=0,                   # specifies the center value for the colormap
    cmap=sns.diverging_palette(50, 500, n=500),     # sets the colour pallette
    square=True,                # all cells are square
    annot=True,                 # Display correlation values in each box
    )

plt.savefig("iris_heatmap")                     # save to png.
plt.show()







#plen = df ["petal_length"]
#pwidth = df ["petal_width"]
#slen = df ["sepal_length"]
#swidth = ["sepal_width"]