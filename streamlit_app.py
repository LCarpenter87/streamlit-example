import streamlit as st
import re
import csv

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


st.header("Let's Wordle!")


st.header("Green Letters")
letters = {}
letters[1] = st.text_area('1st letter', value="", height=1, max_chars=1, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False)
letters[2] = st.text_area('2nd letter', value="", height=2, max_chars=1, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False)
letters[3] = st.text_area('3rd letter', value="", height=3, max_chars=1, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False)
letters[4] = st.text_area('4th letter', value="", height=4, max_chars=1, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False)
letters[5] = st.text_area('5th letter', value="", height=5, max_chars=1, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False)


st.header("Gray Letters")
exclude = st.text_area('Gray Letters', value="", height=None, max_chars=None, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False)


orange = {}
st.header("Orange Letters")
orange[1] = st.text_area('1st letter', value="", height=10, max_chars=5, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False)
orange[2] = st.text_area('2nd letter', value="", height=20, max_chars=5, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False)
orange[3] = st.text_area('3rd letter', value="", height=None, max_chars=5, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False)
orange[4] = st.text_area('4th letter', value="", height=None, max_chars=5, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False)
orange[5] = st.text_area('5th letter', value="", height=None, max_chars=5, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False)

include = ''
for v in orange.values():
  include += v


if st.button("Word me up baby", key=None, help=None, on_click=None, args=None, kwargs=None):
  reg = generate_reg(letters, orange, include, exclude)
  st.text(reg)
  create_possible()
  answers = find_poss(possible, reg)
  st.text(f'Found {len(answers)} words')
  st.text(answers)

