import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
   page_title="Settle Wise - Rental Income",
   page_icon="image.png",
   layout="wide",
   initial_sidebar_state="expanded",
)

st.title("Price by Projected 10 Years Rental Income")

Housing = pd.read_csv("Housing.csv")

selected_area = st.session_state.get('selected_area', None)

if selected_area:
    st.subheader(selected_area)
    st.markdown("###### (Regression Plot)")
    area_data = Housing[Housing['Address'] == selected_area].reset_index(drop=True)

    plt.figure(figsize=(10, 6))
    sns.regplot(data=area_data, x='Projected 10Y Rent', y='Price', line_kws={"color":"red"})
    plt.title('Price Vs. Projected 10-Year Rental Income', fontsize=16)
    plt.xlabel('Projected 10-Year Rental Income (₹)')
    plt.ylabel('House Price (₹)')
    st.pyplot(plt.gcf())
else:
    st.warning("Please select an area on the Home page first.")
