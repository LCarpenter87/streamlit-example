import streamlit as st
import re
import csv

@st.cache
def create_possible():
  global possible
  with open('wordlelist.csv', newline='') as f:
      reader = csv.reader(f)
      possible = [x[0] for x in reader]
      f.close()

def find_poss(possible, reg):
    r = re.compile(reg)
    return list(filter(r.match, possible))

def generate_reg(letters, orange, include, exclude):
  reg = '^'

  for letter in include:
    reg += f'(?=[a-z]*{letter})'

  for letter in exclude:
    reg += f'(?![a-z]*[{letter}])'

  for k,v in letters.items():
    if v != '':
      reg += v
    elif orange[k] != '':
      reg += f'[^{orange[k]}]'
    else:
        reg += "."
  
  return reg


st.header("Let's go!")

letters = {}
letters[1] = st.text_area('1st letter', value="", height=None, max_chars=1, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False)
letters[2] = st.text_area('2nd letter', value="", height=None, max_chars=1, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False)
letters[3] = st.text_area('3rd letter', value="", height=None, max_chars=1, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False)
letters[4] = st.text_area('4th letter', value="", height=None, max_chars=1, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False)
letters[5] = st.text_area('5th letter', value="", height=None, max_chars=1, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False)


question = st.selectbox("What question do you want?", ["How tall is this?", "how wide is this?"], index=0)
answer = st.text_area("What's the answer" , value="")

if st.button("Let's go", key=None, help=None, on_click=None, args=None, kwargs=None):
  st.text(f'Your question was {question}, your answer was {answer}')
  

