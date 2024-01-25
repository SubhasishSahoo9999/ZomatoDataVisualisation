import streamlit as st
import pandas as pd
import plotly.express as px

# Reading the dataframe
df = pd.read_csv('zomato_data_updated.csv')

# Streamlit app
def main():
    st.title("City Comparison in India")

    # Report 1: Comparison Between Cities in India
    st.plotly_chart(px.bar(df.groupby('City').size().reset_index(), x='City', y=0, title='Number of Restaurants per City'))

    # Report 2: Online Delivery Expenses in Different Cities
    st.plotly_chart(px.bar(df.groupby(['City', 'Has Online delivery']).size().reset_index(),
                           x='City', y=0, color='Has Online delivery',
                           title='Online Delivery Expenses in Different Cities'))

    # Report 3: Dine-In Expenses in Different Cities
    st.plotly_chart(px.bar(df.groupby(['City', 'Has Table booking']).size().reset_index(),
                           x='City', y=0, color='Has Table booking',
                           title='Dine-In Expenses in Different Cities'))

    # Report 4: High Living Cost vs. Low Living Cost
    st.plotly_chart(px.bar(df.groupby('City')['Average Cost for two'].mean().reset_index(),
                           x='City', y='Average Cost for two',
                           title='Average Cost for Two in Different Cities'))

if __name__ == '__main__':
    main()
