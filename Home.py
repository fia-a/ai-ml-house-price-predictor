import streamlit as st
from utils.styling import load_css
from PIL import Image
import pandas as pd

# Set icon and title page
st.set_page_config(
    page_title="Price Prediction",
    page_icon="home-value.png.png",
    layout="wide"
)

# # Dark mode toggle
# dark_mode = st.sidebar.checkbox("Enable Dark Mode", value=False)

# # Apply dark/light mode styles
# if dark_mode:
#     st.markdown("""
#         <style>
#         body {
#             background-color: #1F1F28;
#             color: #F5F5F5;
#         }
#         .css-1rs6os.edgvbvh3 {
#             background-color: #2C2F38;
#             color: #F5F5F5;
#         }
#         .stButton>button {
#             background-color: #577BC1;
#             color: #FFFFFF;
#         }
#         </style>
#     """, unsafe_allow_html=True)
#     st.write("🌙 Dark mode is on!")
# else:
#     st.markdown("""
#         <style>
#         body {
#             background-color: #FFFFFF;
#             color: #000000;
#         }
#         .css-1rs6os.edgvbvh3 {
#             background-color: #D4F6FF;
#             color: #000000;
#         }
#         .stButton>button {
#             background-color: #C6E7FF;
#             color: #262730;
#         }
#         </style>
#     """, unsafe_allow_html=True)
#     st.write("☀️ Light mode is active!")

# Load and display dataset
@st.cache_data
def read_dataset(path):
    df = pd.read_csv(path)
    return df

data = read_dataset(r"artifacts/boston.csv")

# Load custom CSS
load_css()

# Make a landing page title
st.title("🏡 House Price Prediction \nby Fia")

# Make a description for the landing page
st.markdown("""
# Welcome to the Boston House Price Predictor!

Ready to predict house prices like a pro? This app helps you:

- **Explore** the Boston Housing Dataset (yes, it's as exciting as it sounds).
- **Discover** how features like crime rate and room size affect prices.
- **Predict** house prices using machine learning (I promise it works!).
- **Check out** model performance metrics (because I like numbers too).

Just use the menu on the left and let the magic happen. Happy predicting!
""")

# Overview dataset
st.markdown("### 💎 Overview Dataset")
col1, col2, col3 = st.columns(3)

# Metrics calculation
rows = data.shape[0]
mean_price = data["MEDV"].mean().round(2)
columns = data.shape[1]

with col1:
    st.metric("Rows:", rows)
with col2:
    st.metric("Avg.Price:", "$" + str(mean_price))
with col3:
    st.metric("Columns:", columns)

# Show sample
st.header("🔍 Sample Data")
st.dataframe(data.head(20))
