# Zomato Data Analysis and Visualization

## Introduction
This project explores Zomato's restaurant data through preprocessing, exploratory data analysis (EDA), and visualization. The aim is to uncover insights into customer behavior, preferences, and industry trends.

## Data Preprocessing
### Importing Necessary Packages
Essential libraries like Plotly, Dash, Pandas, Seaborn, and Matplotlib are imported for analysis and visualization.

### Reading and Merging Data
Zomato's main dataset and country information dataset are loaded and merged based on the 'Country Code'.

### Feature Engineering
A new column, 'Converted Cost (INR),' is created by converting the 'Average Cost for two' to Indian currency. The 'Cuisines' column is split, and the data is exploded for further analysis.

### Save Processed Data
The processed data is saved to a new CSV file.

## Exploratory Data Analysis (EDA)
### Loading Processed Data
The processed data is loaded for analysis.

### Basic Statistics and Visualization
Basic statistics and visualizations (histograms, count plots, scatter plots, and box plots) are created to explore the data.

## Country-Based Analysis Dashboard
### Dashboard Layout
A Dash app is created with a dropdown for country selection. Graphs display cuisine analysis, ratings, delivery services, and cost analysis. The most costly cuisine is dynamically displayed based on user selection.

### Dashboard Callbacks
Callbacks are implemented to update graphs and display dynamic information based on user input.
The Dashboard can be viewed here in the Streamlit app https://zomato-data-visualization-01.streamlit.app/

## City-Based Analysis Dashboard
### Dashboard Layout
A Dash app is created with dropdowns for country and city selection. Graphs display famous cuisine, costlier cuisine, rating count, and delivery mode.

### Dashboard Callbacks
Callbacks are implemented to update city dropdown options and update graphs based on user input.
The Dashboard can be viewed here in the Streamlit app https://zomato-data-visualization-02.streamlit.app/

## City Comparison within India
### Analysis
Data is filtered for India, and various reports are generated, including the number of restaurants per city, online delivery expenses, dine-in expenses, and average cost for two.

### Dashboard
The figures are displayed to compare cities within India.
The Dashboard can be viewed here in the Streamlit app https://zomato-data-visualization-03.streamlit.app/
