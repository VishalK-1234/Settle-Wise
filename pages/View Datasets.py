import streamlit as st
import pandas as pd

st.set_page_config(
   page_title="Settle Wise - Datasets",
   page_icon="image.png",
   layout="wide",
   initial_sidebar_state="expanded",
)

st.title("Datasets in Settle Wise")

st.header("Housing Dataset")
Housing = pd.read_csv("Housing.csv")
st.dataframe(Housing)