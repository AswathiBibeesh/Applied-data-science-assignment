"""importing the required python packages"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""" Reading data set using pandas"""
london_public_transports_name={'bus journey','underground journey','overground journey','DLR journey'}

def read_dataset(file_path):
    return pd.read_csv(file_path)

def select_rows(tabular_data, num_rows=10):
    return tabular_data.head(num_rows)

# Read dataset
df = read_dataset('C:\\Users\\DELL\\Desktop\\tfl-journeys-type.csv')

# Select first 10 rows
journeys_data = select_rows(df, 10)

# Extracting relevant columns for the graph
x = journeys_data['Period and Financial year']
y1 = journeys_data['Bus journeys (m)']
y2 = journeys_data['Underground journeys (m)']
y3 = journeys_data['Overground Journeys (m)']
y4 = journeys_data['DLR Journeys (m)']

"""function to plot line graph"""

def line_graph(x, y1, y2, title, x_label, y_label):
    """
    plotting the line graph using the given data.
    
    Arguments:
    data: pandas tabular_data - contains data to be plotted
    x: str - column name for the x axis
    y1: str - column name for the y axis
    y2: str - column name for the y axis
    title: str -title for the line graph
    
    Returns:
    None
    """
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label='Bus Journeys (m)', marker='o')
    plt.plot(x, y2, label='Underground Journeys (m)', marker='o')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 20:27:48 2023

@author: DELL
"""

"""importing the required python packages"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""" Reading data set using pandas"""
london_public_transports_name={'bus journey','underground journey','overground journey','DLR journey'}

def read_dataset(file_path):
    return pd.read_csv(file_path)

def select_rows(tabular_data, num_rows=10):
    return tabular_data.head(num_rows)

# Read dataset
df = read_dataset('C:\\Users\\DELL\\Desktop\\tfl-journeys-type.csv')

# Select first 10 rows
journeys_data = select_rows(df, 10)

# Extracting relevant columns for the graph
x = journeys_data['Period and Financial year']
y1 = journeys_data['Bus journeys (m)']
y2 = journeys_data['Underground journeys (m)']
y3 = journeys_data['Overground Journeys (m)']
y4 = journeys_data['DLR Journeys (m)']

"""function to plot line graph"""

def line_graph(x, y1, y2, title, x_label, y_label):
    """
    plotting the line graph using the given data.
    
    Arguments:
    data: pandas tabular_data - contains data to be plotted
    x: str - column name for the x axis
    y1: str - column name for the y axis
    y2: str - column name for the y axis
    title: str -title for the line graph
    
    Returns:
    None
    """
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label='Bus Journeys (m)', marker='o')
    plt.plot(x, y2, label='Underground Journeys (m)', marker='o')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()

"""function to plot bar graph"""

def bar_graph(x, y, title, x_label, y_label):
 
    plt.figure(figsize=(10, 6))
    plt.bar(x, y, label='Overground Journeys (m)', alpha=0.5, color='b')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.show()


"""function to plot scatter plot"""

def scatter_plot(x, y, title, x_label, y_label):
    
   
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, label='DLR journey (m)', c='b', alpha=0.5)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid()
    plt.show()



"""function calls"""

# Create line graph
line_graph(x, y1, y2, 'Bus and Underground Journeys Over Time', 'Period and Financial year', 'Journeys (millions)')

# Create bar graph
bar_graph(x, y3, 'Overground Journeys Over Time', 'Period and Financial year', 'Journeys (millions)')

# Create scatter plot
scatter_plot(x, y4, 'DLR Journeys Over Time (m)', 'Period and Financial year', 'Journeys (millions)')
def bar_graph(x, y, title, x_label, y_label):
 
    plt.figure(figsize=(10, 6))
    plt.bar(x, y, label='Overground Journeys (m)', alpha=0.5, color='b')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.show()


def scatter_plot(x, y, title, x_label, y_label):
    
   
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, label='DLR journey (m)', c='b', alpha=0.5)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid()
    plt.show()



"""function calls"""

# Create line graph
line_graph(x, y1, y2, 'Bus and Underground Journeys Over Time', 'Period and Financial year', 'Journeys (millions)')

# Create bar graph
bar_graph(x, y3, 'Overground Journeys Over Time', 'Period and Financial year', 'Journeys (millions)')

# Create scatter plot
scatter_plot(x, y4, 'DLR Journeys Over Time (m)', 'Period and Financial year', 'Journeys (millions)')
