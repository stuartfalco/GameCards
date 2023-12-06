import streamlit as st
import random
import os
import json

def load_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
            return lines
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []
    
def shuffle_cards(cards):
    
    shuffled_list = cards.copy()
    random.shuffle(shuffled_list)
    return shuffled_list


def draw_card():
    
    new_card = st.session_state.deck1[st.session_state.count]
    
    if st.session_state.count < len(st.session_state.deck1)-1:
        st.session_state.count += 1
    else:
        st.session_state.count = 0
        
    
      
    return new_card 



def load_value_from_json(file_path, key):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if key in data:
                return data[key]
            else:
                print(f"Key '{key}' not found in the JSON file.")
                return None
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error occurred while decoding JSON: {str(e)}")
        return None