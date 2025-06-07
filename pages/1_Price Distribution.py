import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
   page_title="Settle Wise - Price Distribution",
   page_icon="image.png",
   layout="wide",
   initial_sidebar_state="expanded",
)

st.title("Price Distribution")

Housing = pd.read_csv("Housing.csv")

selected_area = st.session_state.get('selected_area', None)

if(selected_area):
      st.subheader(selected_area)
      st.markdown("###### (Hist Plot)")
      Data_Selected_Area = Housing[Housing['Address'] == selected_area]
      
      plt.figure(figsize=(10,4))
      plt.clf() 
      sns.histplot(Data_Selected_Area['Price'],bins = 40,color = 'skyblue')
      plt.title(f'Price Vs. Availability in {selected_area}', fontsize=18)
      plt.xlabel('Price (₹ crores)')
      plt.ylabel('House Availability')
      st.pyplot(plt.gcf())
else:
    st.warning("Please select an area on the Home page first.")