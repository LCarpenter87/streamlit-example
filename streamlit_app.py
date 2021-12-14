import pandas as pd
import streamlit as st
import numpy as np


sentence1 = st.text_input('Input your sentence here:') 
sentence2 = st.text_input('Input your second sentence here:') 



dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

print(f'{sentence1} & {sentence2}')

