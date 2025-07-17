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

st.markdown("### Restaurants Dataset")
Restaurants = pd.read_csv("Restaurants.csv")
st.dataframe(Restaurants)

st.markdown("### All Others Dataset")
Others = pd.read_csv("Others.csv")
st.dataframe(Others)