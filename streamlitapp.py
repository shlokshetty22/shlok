#Edit the 8th to 12th line code before upload to gihub
# Import necessary libraries
import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd


# --- Title and Introduction ---
st.title("Interactive Visualizations with Plotly and Streamlit")


# --- Input for Author Information ---
st.sidebar.header("Visualization skill workshop - Plotly")
name = st.sidebar.text_input("shlok shetty")
usn = st.sidebar.text_input("section F betch")
instructor_name = st.sidebar.text_input("ashwin")

# --- Load Dataset ---
tips = sns.load_dataset('tips')  # Loading the tips dataset


# Display the first few rows of the dataset
st.write("## Dataset Overview")
st.write(tips.head())


# --- Task 2: Interactive Bar Chart ---
st.subheader("Task 2: Bar Chart - Average Tip by Day")
# Bar Chart: Average Tip by Day with color for each day
fig2 = px.bar(
    tips, x='day', y='tip', color='day',
    title='Average Tip by Day',
    labels={'tip': 'Average Tip ($)', 'day': 'Day of the Week'},
    template='plotly_white'
)
st.plotly_chart(fig2) 
# --- Task 3: Interactive box Chart ---
st.subheader("Task 3: Box Chart - total bill vs day")
fig5 = px.box(
    dataset,
    x='day',  # Day of the week
    y='total_bill',  # Total bill amount
    color='time',  # Color by time (Lunch or Dinner)
    title='Distribution of Total Bill by Day (Color by Time)',
    labels={'total_bill': 'Total Bill ($)', 'day': 'Day of the Week', 'time': 'Time of Day'},
    template='ggplot2'  # Use plotly template for a blue-themed design
)
st.plotly_chart(fig5)
# --- Task 4: Interactive bohistogram Chart ---
st.subheader("Task 4: histogram Chart - tip vs color")
fig6 = px.histogram(
    dataset,
    x='tip',  # Variable for the x-axis (Tip amounts)
    color='sex',  # Color the bars by 'sex' (Male/Female)
    title='Tip Distribution by Sex',
    labels={'tip': 'Tip ($)', 'sex': 'Gender'},
    nbins=50,  # Number of bins for the histogram
    template='plotly'  # Use the default plotly template for a clean design
)
st.plotly_chart(fig6)# Display the chart in Streamlit