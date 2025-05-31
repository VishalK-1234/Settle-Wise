import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
   page_title="Settle Wise - Price by Locality",
   page_icon="image.png",
   layout="wide",
   initial_sidebar_state="expanded",
)

st.title("Price by Locality")

Housing = pd.read_csv("Housing.csv")

selected_area = st.session_state.get('selected_area', None)

if(selected_area):
    st.subheader(selected_area)
    st.markdown("###### (Horizontal Bar Chart)")
    Data_Selected_Area = Housing[Housing['Address'] == selected_area]
      
    plt.figure(figsize=(10,4))
    plt.clf()
    avg_price_by_address = Data_Selected_Area.groupby('Address')['Price'].mean().sort_values()
    sns.barplot(x=avg_price_by_address.values, y=avg_price_by_address.index, palette='crest')
    plt.title('Average Price by locality', fontsize=18)
    plt.xlabel('Average Price (₹ crores)')
    plt.ylabel('Locality')
    st.pyplot(plt.gcf())
else:
   st.warning("Please select an area on the Home page first.")