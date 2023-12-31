import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
with col1:
    #st.image("images/photo.jpeg", width=200")
    col11,col22,col33=st.columns([2,5,0.2])
    with col22:
        st.image("images/photo.jpeg", width=200)

with col2:
    st.title("Sai Bharghav Chollangi")
    content = """
    Hi I am Sai Bharghav! I am a Python Programmer and a business analytics student. I am currently pursuing 
    Master's in Business Analytics at University of Connecticut. I have worked as a Senior Software Engineer
    at Larsen and Toubro Infotech in India and did my bachelors in Electrical Engineering at VNR VJIET
    """
    st.info(content)

content2 = """
Below you can find some of the apps that I have built using Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, rows in df[:11].iterrows():
        st.header(rows['title'])
        st.write(rows['description'])
        st.image("images/" + rows["image"])
        st.write(f"[Source Code]({rows['url']})")

with col4:
    for index, rows in df[11:].iterrows():
        st.header(rows['title'])
        st.write(rows['description'])
        st.image("images/" + rows["image"])
        st.write(f"[Source Code]({rows['url']})")
