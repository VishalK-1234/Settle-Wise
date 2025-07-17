import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
   page_title="Settle Wise - Restaurants Ratings",
   page_icon="image.png",
   layout="wide",
   initial_sidebar_state="expanded",
)

st.title("No. of Restaurants by Ratings")

selected_area = st.session_state.get('selected_area', None)
Restaurant = pd.read_csv("Restaurants.csv")

if(selected_area):
    st.subheader(selected_area)
    st.markdown("###### (Histogram + KDE Plot)")
    Data_Selected_Area = Restaurant[Restaurant['Address'] == selected_area]

    plt.figure(figsize=(10, 5))
    sns.histplot(data=Data_Selected_Area, x='Rating', bins=10, kde=True, color='orange')
    plt.title(f'Restaurant Rating Distribution in {selected_area}', fontsize=18)
    plt.xlabel('Rating')
    plt.ylabel('Number of Restaurants')
    st.pyplot(plt.gcf())
else:
   st.warning("Please select an area on the Home page first.")



    