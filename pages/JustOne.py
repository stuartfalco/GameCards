import streamlit as st
import random

st.markdown("# Just One 🎈")
st.sidebar.markdown("# Just One 🎈")

if st.checkbox('Show Instructions to play'):
    st.write('1) each round there is a single guesser & everyone else for the SECRET WORD')
    st.write('2) everyone else writes a ONE-WORD clue for the SECRET WORD')
    st.write('3) everyone compares their clues [without gueser seeing] & delete any repeats')
    st.write('4) now Reveal all leftover Clues to the Guesser')
    st.write('Goal is to get most correct Answers in 13 rounds')

st.divider()

cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

def shuffle_cards(cards):
    
    shuffled_list = cards.copy()
    random.shuffle(shuffled_list)
    return shuffled_list

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
    
def draw_card():
    
    new_card = st.session_state.deck1[st.session_state.count]
    
    if st.session_state.count < len(st.session_state.deck1)-1:
        st.session_state.count += 1
    else:
        st.session_state.count = 0
        
    
      
    return new_card 

    
sub1 = st.button("Next Card", key='rand1')
if sub1:
    st.session_state.rounds += 1
    new_card = draw_card()
    #st.write('OG Deck:', cards)
    st.write('rounds:',st.session_state.rounds)
    st.write('new card:')
    st.markdown(f"# {new_card}")
    