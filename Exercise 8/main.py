import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("happy.csv")
print(df.columns)

st.title("In Search for Happiness")
data_x = st.selectbox("Select the data for the X-axis", ("gdp", "happiness", "generosity"), key=1)
data_y = st.selectbox("Select the data for the X-axis", ("gdp", "happiness", "generosity"))

st.header(f"{data_x} and {data_y}")

figure = px.scatter(
    x = df[data_x],
    y = df[data_y],
    labels={"x": f"{data_x}",
            "y": f"{data_y}"}
)

st.plotly_chart(figure)

