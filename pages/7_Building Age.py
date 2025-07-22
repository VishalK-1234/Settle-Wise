import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
   page_title="Settle Wise - Building Age",
   page_icon="image.png",
   layout="wide",
   initial_sidebar_state="expanded",
)

st.title("Price by Building Age")

Housing = pd.read_csv("Housing.csv")

selected_area = st.session_state.get('selected_area', None)

if selected_area:
    
    st.subheader(selected_area)
    st.markdown("###### (Regression Plot)")
    area_data = Housing[Housing['Address'] == selected_area].reset_index(drop=True)

    plt.figure(figsize=(10, 4))
    sns.regplot(data=area_data, x='Building Age', y='Price', scatter_kws={'alpha':0.5}, line_kws={"color":"red"}) 
    plt.title('Price Vs. Building Age', fontsize=16)
    plt.xlabel('Age of Building (Years)')
    plt.ylabel('House Price (₹)')
    st.pyplot(plt.gcf())
    
else:
    st.warning("Please select an area on the Home page first.")
