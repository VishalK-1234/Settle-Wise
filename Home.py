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
st.text("Settle Wise is a data-driven project that helps individuals identify the most suitable localities to live in within Delhi based on their personal requirements. By analyzing key factors such as housing prices, distance to the nearest metro station, air quality (AQI), crimes, and restaurant availability, the project visualizes and compares different areas of the city. The goal is to provide clear and insightful visual data to support smarter, safer, and more sustainable living decisions.")

Housing = pd.read_csv("Housing.csv")
Crimes = pd.read_csv("Crimes.csv")
Metro = pd.read_csv("Metro.csv")
Restaurant = pd.read_csv("Restaurants.csv")
AQI = pd.read_csv("AQI.csv")

areas = Housing['Address'].unique()
selected_area = st.selectbox("Choose your desired area:",areas,index=None,
    placeholder="Select an area...")

if(selected_area):
   st.session_state['selected_area'] = selected_area
   Data_Selected_Area = Housing[Housing['Address'] == selected_area]
   Crime_Selected_Area = Crimes[Crimes['Address'] == selected_area]
   Metro_Selected_Area = Metro[Metro['Address'] == selected_area]
   Restaurant_Selected_Area = Restaurant[Restaurant['Address'] == selected_area]
   AQI_Selected_Area = AQI[AQI['Address'] == selected_area]


   st.markdown(f"### Summary Stats of {selected_area}:")
   st.markdown(f"##### Average House Price in {selected_area}: ₹{int(Data_Selected_Area['Price'].mean())}")
   st.markdown(f"##### Median House Price in {selected_area}: ₹{int(Data_Selected_Area['Price'].median())}")
   st.markdown(f"##### Highest Pricing in {selected_area}: ₹{int(Data_Selected_Area['Price'].max())}")
   st.markdown(f"##### Lowest Pricing in {selected_area}: ₹{int(Data_Selected_Area['Price'].min())}")
   st.markdown(f"##### Average AQI in {selected_area}: {AQI_Selected_Area['AQI'].values[0]}")
   st.markdown(f"##### Total Crimes Reported in {selected_area}: {Crime_Selected_Area['Total Crimes'].values[0]}")
   st.markdown(f"##### Average Distance to Metro Station in {selected_area}: {int(Metro_Selected_Area['Distance'].mean()*1000)} meters")
   st.markdown(f"##### Average Restaurant Rating (out of 5) in {selected_area}: {Restaurant_Selected_Area['Rating'].mean():.2f}")
   st.markdown(f"##### Average Restaurant Pricing for 2 in {selected_area}: ₹{int(Restaurant_Selected_Area['Price for 2'].mean())}")
   st.markdown(f"##### Total Areas Listed: 54")