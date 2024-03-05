import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

# Load dataset
df = pd.read_csv("https://raw.githubusercontent.com/nazirasafwani/Dicoding/main/day.csv")

# Set the page title
st.title("Bike Sharing Dashboard")

# Sidebar with filters
st.sidebar.title("Filters")

# Filter by season
seasons = st.sidebar.multiselect("Select Seasons", sorted(df['season'].unique()))
if seasons:
    df = df[df['season'].isin(seasons)]

# Filter by day type
day_types = st.sidebar.multiselect("Select Day Types", sorted(df['weekday'].unique()))
if day_types:
    df = df[df['weekday'].isin(day_types)]

# Display dataset
st.subheader("Data Bike Sharing")
st.dataframe(df)

# Display basic statistics
st.subheader("Statistics Descriptive")
st.write(df.describe())


# Boxplot of rentals per season using Plotly
st.subheader("Rentals per Season")
fig = px.box(df, x='season', y='cnt', points="all")
st.plotly_chart(fig)


# Compute the correlation matrix for numeric columns
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
correlation_matrix = df[numeric_columns].corr()

# Display the correlation matrix
st.subheader("Correlation Matrix")
st.write(correlation_matrix)

# Display a heatmap of the correlation matrix using Plotly
fig_heatmap = px.imshow(correlation_matrix)
st.plotly_chart(fig_heatmap)

# Show the plot using Streamlit
st.pyplot(fig)

