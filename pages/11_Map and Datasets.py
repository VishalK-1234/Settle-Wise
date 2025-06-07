import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(
   page_title="Settle Wise - Map and Datasets",
   page_icon="image.png",
   layout="wide",
   initial_sidebar_state="expanded",
)

st.title("Map and Datasets Used in Settle Wise")

st.markdown("## Delhi NCR Map")
m = folium.Map(location=[28.6129, 77.2295], tiles="CartoDB positron")
st_folium(m, width=900, height=520)

st.markdown("## Datasets")

st.markdown("### Housing Dataset")
Housing = pd.read_csv("Housing.csv")
st.dataframe(Housing)

st.markdown("### Metro Dataset")
Metro = pd.read_csv("Metro.csv")
st.dataframe(Metro)

st.markdown("### Crimes Dataset")
Crimes = pd.read_csv("Crimes.csv")
st.dataframe(Crimes)

st.markdown("### Restaurants Dataset")
Restaurants = pd.read_csv("Restaurants.csv")
st.dataframe(Restaurants)

st.markdown("### AQI Dataset")
AQI = pd.read_csv("AQI.csv")
st.dataframe(AQI)