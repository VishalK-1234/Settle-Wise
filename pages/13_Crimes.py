import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
   page_title="Settle Wise - Crimes",
   page_icon="image.png",
   layout="wide",
   initial_sidebar_state="expanded",
)

st.title("Price by Number of Crime Incidents")

Housing = pd.read_csv("Housing.csv")
Crimes = pd.read_csv("Others.csv")

selected_area = st.session_state.get('selected_area', None)


if(selected_area):
    st.subheader(selected_area)
    st.markdown("###### (Scatter Plot)")

    Housing_Area = Housing[Housing['Address'] == selected_area]
    Crime_Area = Crimes[Crimes['Address'] == selected_area]
      
    total_crimes = int(Crime_Area['Total Crimes'].values[0])

    Housing_Area = Housing_Area.copy()
    Housing_Area['Total Crimes'] = total_crimes

    fig, ax = plt.subplots(figsize=(10,6))
    sns.scatterplot(data=Housing_Area, x='Total Crimes', y='Price', color='crimson')
    ax.set_xlabel('Total Crimes in Locality')
    ax.set_ylabel('House Price (₹)')
    ax.set_title(f'Price Vs. Crimes in {selected_area}', fontsize=18)
    st.pyplot(fig)
else:
   st.warning("Please select an area on the Home page first.")
    