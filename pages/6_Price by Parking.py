import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
   page_title="Settle Wise - Parking",
   page_icon="image.png",
   layout="wide",
   initial_sidebar_state="expanded",
)

st.title("Price by Availability of Parking")

Housing = pd.read_csv("Housing.csv")

selected_area = st.session_state.get('selected_area', None)

if(selected_area):
    st.subheader(selected_area)
    st.markdown("###### (Violin Plot)")
    Data_Selected_Area = Housing[Housing['Address'] == selected_area]
      
    plt.figure(figsize=(10,4))
    plt.clf()
    sns.violinplot(data = Data_Selected_Area,x = 'Bathroom', y = 'Price',palette='coolwarm')
    plt.title(f'Price Vs. Parking Availability in {selected_area}', fontsize=18)
    plt.xlabel('Number of Parking Spaces')
    plt.ylabel('Price (₹ crores)')
    st.pyplot(plt.gcf())
else:
   st.warning("Please select an area on the Home page first.")