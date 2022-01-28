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

l1, l2, l3, l4, l5 = st.columns([1,1,1,1,1])

letters[1] = l1.text_input('1st letter', value="", max_chars=1)
letters[2] = l2.text_input('2nd letter', value="", max_chars=1)
letters[3] = l3.text_input('3rd letter', value="", max_chars=1)
letters[4] = l4.text_input('4th letter', value="", max_chars=1)
letters[5] = l5.text_input('5th letter', value="", max_chars=1)


st.header("Gray Letters")
exclude = st.text_input('Gray Letters', value="")


orange = {}
st.header("Orange Letters")
orange[1] = st.text_input('1st letter', value="", max_chars=5)
orange[2] = st.text_input('2nd letter', value="", max_chars=5)
orange[3] = st.text_input('3rd letter', value="", max_chars=5)
orange[4] = st.text_input('4th letter', value="", max_chars=5)
orange[5] = st.text_input('5th letter', value="", max_chars=5)

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

