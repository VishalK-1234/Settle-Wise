import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Settle Wise - Schools",
    page_icon="image.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Price by Number of Schools")

Housing = pd.read_csv("Housing.csv")
School = pd.read_csv("Others.csv")

selected_area = st.session_state.get('selected_area', None)


if(selected_area):
    st.subheader(selected_area)
    st.markdown("###### (Box Plot)") 

    Housing_Area = Housing[Housing['Address'] == selected_area]
    School_Area = School[School['Address'] == selected_area]
      
    total_schools = int(School_Area['Schools'].values[0])

    Housing_Area = Housing_Area.copy()
    Housing_Area['Schools'] = total_schools

    fig, ax = plt.subplots(figsize=(10,6))
    
    sns.boxplot(data=Housing_Area, x='Schools', y='Price', color='crimson')
    
    ax.set_xlabel('Total Schools in Locality')
    ax.set_ylabel('House Price (₹)')
    ax.set_title(f'Price Vs. Schools in {selected_area}', fontsize=18)
    st.pyplot(fig)
else:
   st.warning("Please select an area on the Home page first.")