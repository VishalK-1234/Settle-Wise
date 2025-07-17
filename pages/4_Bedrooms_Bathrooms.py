import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
   page_title="Settle Wise - Bedrooms_Bathrooms",
   page_icon="image.png",
   layout="wide",
   initial_sidebar_state="expanded",
)

st.title("Price by Bedrooms / Bathrooms")

Housing = pd.read_csv("Housing.csv")

selected_area = st.session_state.get('selected_area', None)

if(selected_area):
    st.subheader(selected_area)
    st.markdown("###### (Box Plot)")
    Data_Selected_Area = Housing[Housing['Address'] == selected_area]
      
    plt.figure(figsize=(10,4))
    plt.clf() 
    sns.boxplot(data = Data_Selected_Area,x = 'Bedroom', y = 'Price',palette='pastel')
    plt.title(f'Price Vs. Number of Bedrooms in {selected_area}', fontsize=18)
    plt.xlabel('Number of Bedrooms')
    plt.ylabel('Price (₹ crores)')
    st.pyplot(plt.gcf())

    st.text("")
    st.text("")
    st.text("")

    plt.figure(figsize=(10,4))
    plt.clf() 
    sns.boxplot(data = Data_Selected_Area,x = 'Bathroom', y = 'Price',palette='pastel')
    plt.title(f'Price Vs. Number of Bathrooms in {selected_area}', fontsize=18)
    plt.xlabel('Number of Bathrooms')
    plt.ylabel('Price (₹ crores)')
    st.pyplot(plt.gcf())

else:
    st.warning("Please select an area on the Home page first.")