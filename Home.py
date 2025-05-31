import streamlit as st
import pandas as pd

st.set_page_config(
   page_title="Settle Wise - Home",
   page_icon="image.png",
   layout="wide",
   initial_sidebar_state="expanded",
)

st.title("Communtiy Project")
st.header("Settle Wise")
st.text("Settle Wise is a data-driven project that helps individuals identify the most suitable localities to live in within Delhi based on their personal requirements. By analyzing key factors such as housing prices, distance to the nearest metro station, air quality (AQI), crime rates, and restaurant availability, the project visualizes and compares different areas of the city. The goal is to provide clear and insightful visual data to support smarter, safer, and more sustainable living decisions.")

Housing = pd.read_csv("Housing.csv")
areas = Housing['Address'].unique()
selected_area = st.selectbox("Choose your desired area:",areas,index=None,
    placeholder="Select area...")

if(selected_area):
   st.session_state['selected_area'] = selected_area
   Data_Selected_Area = Housing[Housing['Address'] == selected_area]

   st.markdown("### Summary Stats:")
   st.markdown(f"##### Average House Price in {selected_area}: ₹{int(Data_Selected_Area['Price'].mean()):,}")
   st.markdown(f"##### Median House Price in {selected_area}: ₹{int(Data_Selected_Area['Price'].median()):,}")
   st.markdown(f"##### Highest Pricing in {selected_area}: ₹{int(Data_Selected_Area['Price'].max()):,}")
   st.markdown(f"##### Lowest Pricing in {selected_area}: ₹{int(Data_Selected_Area['Price'].min()):,}")
   st.markdown(f"##### Total Areas listed: 53")