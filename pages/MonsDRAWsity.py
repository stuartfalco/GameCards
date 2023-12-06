import streamlit as st
import random
import os

from helper_fcn import load_text_file, shuffle_cards,draw_card , load_value_from_json
###

game_name = 'MonsDRAWsity'

st.markdown(f"# :green[{game_name}] ")

file_path = os.path.join(os.getcwd(),'instruction.json')
instructions = load_value_from_json(file_path, game_name)
 
with st.expander('Click to toggle => Rules'):
    for i, item in enumerate(instructions):
        st.markdown(f"{i+1}. {item}")
    
st.divider()