import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
   page_title="Settle Wise - Price by Furnishing Status",
   page_icon="image.png",
   layout="wide",
   initial_sidebar_state="expanded",
)

st.title("Price by Furnishing Status")

Housing = pd.read_csv("Housing.csv")

selected_area = st.session_state.get('selected_area', None)

if(selected_area):
    st.subheader(selected_area)
    st.markdown("###### (Bar Plot)")
    Data_Selected_Area = Housing[Housing['Address'] == selected_area]
      
    plt.figure(figsize=(10,4))
    plt.clf()
    avg_price_by_furnishing = Data_Selected_Area.groupby('Furnishing')['Price'].mean().sort_values()
    sns.barplot(x=avg_price_by_furnishing.index, y=avg_price_by_furnishing.values, palette='Set2')
    plt.title('Average Price by Furnishing Status', fontsize=18)
    plt.xlabel('Furnishing Status')
    plt.ylabel('Average Price (₹ crores)')
    st.pyplot(plt.gcf())
else:
   st.warning("Please select an area on the Home page first.")