from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st



with st.echo():
    sentence1 = st.text_input('Input your sentence here:') 

with st.echo():
    sentence2 = st.text_input('Input your second sentence here:') 

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df
