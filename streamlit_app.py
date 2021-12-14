import pandas as pd
import streamlit as st
import numpy as np


st.title('Testing')

sentence1 = st.text_input('Input your sentence here:') 
sentence2 = st.text_input('Input your second sentence here:') 

example = st.slider('Input Example' , min_value=0, max_value=1000, value=500, step=10)

options = ['Every Time', 'Most of the Time', 'Rarely', 'Never']

kindwords = st.selectbox('How often did you say Please and Thank you?', options, index=0)


if st.button("Let's go", key=None, help=None, on_click=None, args=None, kwargs=None):
  st.text(f'{sentence1} and {sentence2} and {example}')
  

