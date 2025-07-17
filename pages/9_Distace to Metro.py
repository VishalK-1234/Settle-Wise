import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
   page_title="Settle Wise - Metro",
   page_icon="image.png",
   layout="wide",
   initial_sidebar_state="expanded",
)

st.title("Price by Distance to Nearest Metro Station")

Housing = pd.read_csv("Housing.csv")

selected_area = st.session_state.get('selected_area', None)

if selected_area:
    st.subheader(selected_area)
    st.markdown("###### (Scatter Plot)")
    area_data = Housing[Housing['Address'] == selected_area].reset_index(drop=True)

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=area_data, x='Distance', y='Price')
    plt.title(f"Price Vs. Distance from Metro Station in {selected_area}", fontsize=18)
    plt.xlabel("Distance to Metro (km)")
    plt.ylabel("House Price (₹)")
    st.pyplot(plt.gcf())
else:
    st.warning("Please select an area on the Home page first.")
