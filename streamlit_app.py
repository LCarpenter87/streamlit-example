import streamlit as st
import re
import csv
import random

## Generate List of possible words
def create_possible():
  global possible
  with open('wordlelist.csv', newline='') as f:
      reader = csv.reader(f)
      possible = set(x[0] for x in reader)
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


st.title("Green Letters")
st.caption("Put in your green known letters, in the correct position")
letters = {}
l1, l2, l3, l4, l5, space = st.columns([1,1,1,1,1, 5])
letters[1] = l1.text_input('1st letter', value="", max_chars=1)
letters[2] = l2.text_input('2nd letter', value="", max_chars=1)
letters[3] = l3.text_input('3rd letter', value="", max_chars=1)
letters[4] = l4.text_input('4th letter', value="", max_chars=1)
letters[5] = l5.text_input('5th letter', value="", max_chars=1)


st.title("Gray Letters")
st.caption("Put in your gray letters, in any order (no spaces)")
exclude = st.text_input('Gray Letters', value="")
orange = {}
st.header("Orange Letters")
st.caption("Put in your orange letters, in the position you tried them in")
st.caption("You can put multiple orange letters in each position (no spaces)")

o1, o2, o3, o4, o5 = st.columns([1,1,1,1,1])
orange[1] = o1.text_input('1st letter', value="", max_chars=5)
orange[2] = o2.text_input('2nd letter', value="", max_chars=5)
orange[3] = o3.text_input('3rd letter', value="", max_chars=5)
orange[4] = o4.text_input('4th letter', value="", max_chars=5)
orange[5] = o5.text_input('5th letter', value="", max_chars=5)

include = ''
for v in orange.values():
  include += v


#if st.button("Word me up baby", key=None, help=None, on_click=None, args=None, kwargs=None):
reg = generate_reg(letters, orange, include, exclude)
st.text(f'The Regex used was: {reg}')
create_possible()
answers = find_poss(possible, reg)
random.shuffle(answers)
st.text(f'Found {len(answers)} words')
for word in answers:
  st.text(word)

