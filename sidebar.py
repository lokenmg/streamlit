import streamlit as st

st.title("mi primera app con streamlit")

sidebar = st.sidebar

sidebar.title("Esta es la barra lateral")
sidebar.write("Datos del slidebar")

st.header("header 1")
st.header("header 2")
st.header("header 3")

st.write("Datos del content")