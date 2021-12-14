import pandas as pd
import streamlit as st
import numpy as np


with st.echo():
    sentence1 = st.text_input('Input your sentence here:') 

with st.echo():
    sentence2 = st.text_input('Input your second sentence here:') 



dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)
