import streamlit as st
import random
import os

from helper_fcn import load_text_file, shuffle_cards,draw_card , load_value_from_json
###

game_name = 'OkayGenius'

st.markdown(f"# :green[{game_name}] ")

file_path = os.path.join(os.getcwd(),'instruction.json')
instructions = load_value_from_json(file_path, game_name)
 
with st.expander('Click to toggle => Rules'):
    for i, item in enumerate(instructions):
        st.markdown(f"{i+1}. {item}")
    
st.divider()
 
file_name = game_name + ".txt"
file_path = os.path.join(os.getcwd(),file_name)
cards = load_text_file(file_path)

deck = shuffle_cards(cards)

if 'deck1' not in st.session_state:
        st.session_state.deck1 = deck
elif 'deck1'  in st.session_state:
        st.session_state.deck1 = st.session_state.deck1
        
if 'new_card' not in st.session_state:
    st.session_state.new_card = 'empty'
elif 'new_card' in st.session_state:
    st.session_state.new_card = st.session_state.new_card
    
if 'count' not in st.session_state:
    st.session_state.count = 0 
if 'rounds' not in st.session_state:
    st.session_state.rounds = 0 
        
sub1 = st.button("Next Card", key='rand1')
if sub1:
    st.session_state.rounds += 1
    new_card = draw_card()
    st.markdown(f':red[rounds:] {st.session_state.rounds}')
    st.markdown('#QUESTION:')
    st.markdown(f"# {new_card.upper()}")
    