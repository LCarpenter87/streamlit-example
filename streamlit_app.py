import pandas as pd
import streamlit as st
import numpy as np




question = st.selectbox("What question do you want?", ["How tall is this?", "how wide is this?"], index=0)
answer = st.text_area("What's the answer") , value="")

if st.button("Let's go", key=None, help=None, on_click=None, args=None, kwargs=None):
  st.text(f'Your question was {question}, your answer was {answer}')
  

