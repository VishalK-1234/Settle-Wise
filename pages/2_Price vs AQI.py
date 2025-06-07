import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
   page_title="Settle Wise - AQI",
   page_icon="image.png",
   layout="wide",
   initial_sidebar_state="expanded",
)

st.title("Price by Average AQI")


Housing = pd.read_csv("Housing.csv")
AQI = pd.read_csv("AQI.csv")

selected_area = st.session_state.get('selected_area', None)


if(selected_area):
    st.subheader(selected_area)
    st.markdown("###### (Scatter Plot)")

    Housing_Area = Housing[Housing['Address'] == selected_area]
    AQI_Area = AQI[AQI['Address'] == selected_area]
      
    Total_AQI = int(AQI_Area['AQI'].values[0])

    Housing_Area = Housing_Area.copy()
    Housing_Area['AQI'] = Total_AQI

    fig, ax = plt.subplots(figsize=(10,6))
    sns.scatterplot(data=Housing_Area, x='AQI', y='Price', color='crimson')
    ax.set_xlabel('Average AQI in Locality')
    ax.set_ylabel('House Price (₹)')
    ax.set_title(f'Price Vs. Average AQI in {selected_area}', fontsize=18)
    st.pyplot(fig)
else:
   st.warning("Please select an area on the Home page first.")