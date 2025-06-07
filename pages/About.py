import streamlit as st

st.set_page_config(
    page_title="About Settle Wise",
    page_icon="image.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("About Settle Wise (Communtiy Project)")
st.markdown("---")


st.header("1. Identifying the Socially Relevant Issue")
st.markdown("""
In a rapidly growing city like **Delhi NCR**, choosing the right locality to live in is a major challenge. People often struggle to find areas that match their preferences for **safety**, **affordability**, **air quality**, **connectivity**, and **lifestyle options**. This lack of clear, organized, and accessible information creates confusion, often leading people to make suboptimal or uninformed decisions about where to settle.

This challenge is especially significant for people **new to the city** who may not have an established understanding of the different neighborhoods, making it hard to navigate and choose suitable localities.

**Settle Wise** aims to bridge this gap with data-driven insights to help all residents, particularly newcomers, make informed choices confidently.
""")

st.header("2. Understanding the Problem")
st.markdown("""
Many individuals and families relocating to or within Delhi NCR lack access to **consolidated information** about key factors such as:
- **House Pricing Trends**
- **Crime Rates**
- **Air Quality (AQI)**
- **Distance to Nearest Metro Stations**
- **Availability of Restaurants and Lifestyle Amenities**

This absence of transparent, location-specific data hinders smart decision-making and quality of life.
""")


st.header("3. Community Data Collection")
st.markdown("""
We collected a range of **community-contributed** and **publicly available datasets** across localities in Delhi NCR, including:

- **Housing prices**, **Distance to metro stations**, **Crime data**, and **Restaurant availability** from datasets sourced from [Kaggle](https://www.kaggle.com).
- **Air Quality Index (AQI)** data sourced from the reliable and up-to-date website [IQAir](https://www.iqair.com/).

We used **pandas** library extensively for cleaning and managing these datasets to ensure accurate and meaningful analysis.
""")


st.header("4. The Solution: Settle Wise")
st.markdown("""
Settle Wise is a **Streamlit-powered web app** that allows users to:
- Select a locality of interest
- View key statistics across multiple dimensions
- Visually compare price trends, safety, accessibility, and lifestyle options
- Use interactive maps and visualizations to assist in choosing the most suitable neighborhood

It acts as a **personalized, data-informed recommendation tool** for home seekers in Delhi NCR.
""")


st.header("5. How Settle Wise Solves the Problem")
st.markdown("""
Settle Wise solves the housing decision-making challenge by:
- Presenting easy-to-understand **graphs and plots** created using **Matplotlib** and **Seaborn**.
- Offering **area-specific summaries** (e.g., average price, AQI, crime levels).
- Visualizing metro connectivity and lifestyle quality.
- Empowering users to **compare and contrast localities**.

This comprehensive approach supports smarter, safer, and more personalized decision-making, making the complex process of finding a home simpler and more transparent.
""")

# 6. Data Visualization
st.header("6. Data Visualization")
st.markdown("""
The final output includes:
-  **Box plots** for comparing housing prices.
-  **Scatter plots** for crime rates and metro distances.
-  **AQI comparisons** across areas.
-  **Restaurant ratings vs. pricing**.
-  **Interactive Delhi NCR Map** powered by Folium, designed for easy neighborhood exploration.
-  **And many more**.

These visualizations help users make **smarter and safer housing decisions**.
""")

st.markdown("---")
st.markdown("##### Settle Wise is more than just a tool—it's a step toward a more informed and empowered urban living experience.")