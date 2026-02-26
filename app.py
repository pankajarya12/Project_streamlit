import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(page_title="E-Challan Dashboard", layout="wide")

st.title("🚦 E-Challan Daily Data Dashboard")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("echallan_daily_data.csv")
    return df

df = load_data()

# Show raw data
if st.checkbox("Show Raw Data"):
    st.dataframe(df)

st.sidebar.header("Filter Options")

# Select column for filtering (Example: State or District if available)
column_list = df.columns.tolist()
selected_column = st.sidebar.selectbox("Select Column to Filter", column_list)

unique_values = df[selected_column].unique()
selected_value = st.sidebar.selectbox("Select Value", unique_values)

filtered_df = df[df[selected_column] == selected_value]

st.subheader("Filtered Data")
st.dataframe(filtered_df)

# Summary statistics
st.subheader("Summary Statistics")
st.write(filtered_df.describe())

# Visualization Section
st.subheader("Data Visualization")

numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

if numeric_columns:
    selected_numeric = st.selectbox("Select Numeric Column for Plot", numeric_columns)

    fig, ax = plt.subplots()
    sns.histplot(filtered_df[selected_numeric], kde=True, ax=ax)
    st.pyplot(fig)

else:
    st.warning("No numeric columns available for plotting.")

st.success("Dashboard Loaded Successfully 🚀")
