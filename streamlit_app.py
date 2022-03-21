import streamlit as st

st.title("Hello DS4")
st.header("DS4 > DS3 == True")

number1 = st.text_input("First number?")
number2 = st.text_input("Second number")

st.text(number1 + number2) 
