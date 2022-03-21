import streamlit as st

st.title("Hello DS4")
st.header("DS4 > DS3 == True")

my_str = st.text_input("What's your name?") 

st.text(f'Hello {my_str}') 
