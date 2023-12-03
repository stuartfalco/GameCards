import streamlit as st
import random
import os

st.markdown("# Fun Facts 🎉")
st.sidebar.markdown("# Fun Facts 🎉")

if st.checkbox("Read the Instructions"):
    st.write("1. Reveal a new question & everyone secretly writes their answer on their arrow face down")
    st.write("2. Take turns placing arrow in relation to others from LOW to HIGH")
    st.write("3. After everyone has placed their answer, the starting player has the opportunity to move their own arrow — without touching anyone else's!")
    st.write("4. Then you reveal everyone's numbers, and removes each arrow that is out of order.")
    st.write("5. Each remaining arrow represents a correct answer and provides one point for the entire team. ")
    st.write("6. After eight rounds, record the team's score in the Record of Legends.")
    
st.divider()
def load_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
            return lines
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []
    

#cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
file_path = os.path.join(os.getcwd(),'FunFacts.txt')
cards = load_text_file(file_path)

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
    st.markdown(f':red[rounds:] {st.session_state.rounds}')
    st.markdown('#QUESTION:')
    st.markdown(f"# {new_card}")
    
