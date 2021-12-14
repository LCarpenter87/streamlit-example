from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st



with st.echo():
    sentence1 = st.text_input('Input your sentence here:') 

with st.echo():
    sentence2 = st.text_input('Input your second sentence here:') 
