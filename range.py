import streamlit as st
import pandas as pd

st.title('Streamlite - search ranges')

DATA_URL =('https://firebasestorage.googleapis.com/v0/b/datasetcsv-68031.appspot.com/o/csv%2FRodrigo%2Fdataset.csv?alt=media&token=53f3a527-0d07-4b5c-96c7-1ef52b61dfb0')

@st.cache
def load_data_byrange(startid, endid):
    data = pd.read_csv(DATA_URL)
    fitered_data_byrange = data[ (data['index'] >= startid) & (data['index'] <= endid) ]

    return fitered_data_byrange

startid = st.text_input('Start index: ')
endid = st.text_input('End index: ')
btnRange=st.button('Search by rabge')

if(btnRange):
    fiterebyrange = load_data_byrange(int(startid), int(endid))
    count_row=fiterebyrange.shape[0]
    st.write(f"Total items: {count_row}")

    st.dataframe(fiterebyrange)