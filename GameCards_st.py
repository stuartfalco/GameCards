import streamlit as st
import os
import random


## to need enter in command terminal below
# streamlit run partyCards_st.py

st.header(":blue[LETS PLAY SOME GAMES] :sunglasses:")

games = {
    'Just One' : "this co-op everyone is trying together to get a solo guesser the SECRET word by providing a one-word clue.",
    'Ticked Off' : "this trivia games about categories",
    'Hivemind' : "can you think of the same thing as most people",
}

st.write('List of Games')

st.write("filter by Player coutn")

st.write("filter by Type : word guessing ; drawaing ; etc")

st.write("Image + Game Blurb")