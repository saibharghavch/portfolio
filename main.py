import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.jpeg")

with col2:
    st.title("Sai Bharghav Chollangi")
    content= """
    Hi I am Sai Bharghav! I am a Python Programmer and a business analytics student. I am currently pursuing 
    Master's in Business Analytics at University of Connecticut. I have worked as a Senior Software Engineer
    at Larsen and Toubro Infotech in India and did my bachelors in Electrical Engineering at VNR VJIET
    """
    st.info(content)