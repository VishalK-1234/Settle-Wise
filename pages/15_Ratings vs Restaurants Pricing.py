import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
   page_title="Settle Wise - Restaurants Pricing",
   page_icon="image.png",
   layout="wide",
   initial_sidebar_state="expanded",
)

st.title("Restaurants by Pricing")

selected_area = st.session_state.get('selected_area', None)
Restaurant = pd.read_csv("Restaurants.csv")

if(selected_area):
    st.subheader(selected_area)
    st.markdown("###### (Scatter Plot)")
    Data_Selected_Area = Restaurant[Restaurant['Address'] == selected_area]

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=Data_Selected_Area, x='Rating', y='Price for 2', color='green')
    plt.title(f'Rating Vs. Price for 2 in {selected_area}', fontsize=18)
    plt.xlabel('Rating')
    plt.ylabel('Price for 2 (₹)')
    st.pyplot(plt.gcf())

else:
   st.warning("Please select an area on the Home page first.")



    