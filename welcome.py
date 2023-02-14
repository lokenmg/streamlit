import streamlit as st

def bienbenida(nombre):
    mymensaje = "bienvenido /a/e " + nombre
    return mymensaje

myname = st.text_input("nombre: ")
if(myname):
    mensaje = bienbenida(myname)
    st.write(f" Result : {mensaje}")
