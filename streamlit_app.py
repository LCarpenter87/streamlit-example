import pandas as pd
import streamlit as st
import numpy as np


st.title('Testing')

sentence1 = st.text_input('Input your sentence here:') 
sentence2 = st.text_input('Input your second sentence here:') 

example = st.slider('Input Example' , min_value=0, max_value=1000, value=500, step=10)





