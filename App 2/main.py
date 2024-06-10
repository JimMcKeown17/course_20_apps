import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Jim McKeown")
    content = """
    Hey, it's me Jim.Copying and pasting 10 worCopying and pasting 10 worCopying and pasting 10 worCopying and pasting 10 worCopying and pasting 10 worCopying and pasting 10 worCopying and pasting 10 worCopying and pasting 10 worCopying and pasting 10 worCopying and pasting 10 wor Copying and pasting 10 words."""
    st.info(content)

st.write("Below you can find some of the apps I have built in Python. Please feel free to contact me.")

col3, col4 = st.columns(2)

data = pd.read_csv("data.csv", sep=";")

with col3:
    for index,row in data[:10].iterrows():
        st.header(row['title'])
        # st.image(f'images/+ {row["image"]}')
        st.write(row['description'])
        st.write(row['url'])

with col4:
    for index,row in data[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.write(row['url'])