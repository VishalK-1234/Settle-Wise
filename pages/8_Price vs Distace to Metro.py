import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
   page_title="Settle Wise - Nearest Metro Station",
   page_icon="image.png",
   layout="wide",
   initial_sidebar_state="expanded",
)

st.title("Distance From Nearest Metro Station")

Housing = pd.read_csv("Housing.csv")
MetroDist = pd.read_csv("Metro.csv")

selected_area = st.session_state.get('selected_area', None)

if selected_area:
    st.subheader(selected_area)
    st.markdown("###### (Scatter Plot)")

    housing_area = Housing[Housing['Address'] == selected_area].reset_index(drop=True)
    metro_area = MetroDist[MetroDist['Address'] == selected_area].reset_index(drop=True)
    combined = pd.DataFrame({'Price': housing_area['Price'],'Distance': metro_area['Distance']})
    plt.figure(figsize=(10,6))
    sns.scatterplot(data=combined, x='Distance', y='Price')
    plt.title(f"Price Vs. Distance from Metro Station in {selected_area}", fontsize=18)
    plt.xlabel("Distance to Metro (km)")
    plt.ylabel("House Price (₹)")
    st.pyplot(plt.gcf())
else:
    st.warning("Please select an area on the Home page first.")
