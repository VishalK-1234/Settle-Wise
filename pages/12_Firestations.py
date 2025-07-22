import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Settle Wise - Firestation",
    page_icon="image.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Price by Number of Firestations")

Housing = pd.read_csv("Housing.csv")
Firestations = pd.read_csv("Others.csv")

selected_area = st.session_state.get('selected_area', None)


if(selected_area):
    st.subheader(selected_area)
    st.markdown("###### (Box Plot)") 

    Housing_Area = Housing[Housing['Address'] == selected_area]
    Firestation_Area = Firestations[Firestations['Address'] == selected_area]
      
    total_firestations = int(Firestation_Area['Firestations'].values[0])

    Housing_Area = Housing_Area.copy()
    Housing_Area['Firestations'] = total_firestations

    fig, ax = plt.subplots(figsize=(10,4))
    
    sns.boxplot(data=Housing_Area, x='Firestations', y='Price', color='orange')
    
    ax.set_xlabel('Total Firestations in Locality')
    ax.set_ylabel('House Price (₹)')
    ax.set_title(f'Price Vs. Firestations in {selected_area}', fontsize=18)
    st.pyplot(fig)
else:
   st.warning("Please select an area on the Home page first.")