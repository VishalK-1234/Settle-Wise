import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
   page_title="Settle Wise - Price vs Area",
   page_icon="image.png",
   layout="wide",
   initial_sidebar_state="expanded",
)

st.title("Price vs. Area")

Housing = pd.read_csv("Housing.csv")

selected_area = st.session_state.get('selected_area', None)

if(selected_area):
      st.subheader(selected_area)
      st.markdown("###### (Scatter Plot)")
      Data_Selected_Area = Housing[Housing['Address'] == selected_area]
      
      plt.figure(figsize=(10,4))
      plt.clf() 
      sns.scatterplot(data = Data_Selected_Area,x = 'Area', y = 'Price',color = 'green')
      plt.title('Price vs Area', fontsize=18)
      plt.xlabel('Area (sq ft)', fontsize=12)
      plt.ylabel('Price (₹ crores)', fontsize=12)
      st.pyplot(plt.gcf())
else:
   st.warning("Please select an area on the Home page first.")