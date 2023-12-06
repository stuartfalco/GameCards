import streamlit as st
import os
import random
import pandas as pd

## to need enter in command terminal below
# streamlit run partyCards_st.py

data = pd.DataFrame({
    'Name': ['DoodleDash', 'FunFacts', 'HiveMind', 'JustOne',"MonsDRAWsity","OkayGenius","TopTen"],
    'Player_min': [4, 4, 4, 4,4,4,4],
    'Player_max': [7, 8, 8, 7,6,8,8],
    'Style': ['Competitive','Co-op','Competitive','Co-op','Competitive','Competitive','Co-op'],
    'Type' : ['Drawing','Guessing','Trivia','Guessing','Drawing','Trivia','Guessing']
})

# radio button filters
player_options = [4,5,6,7,8]
style_options = ["Any",'Competitive','Co-op']
type_options = ['Any','Drawing','Guessing','Trivia']

st.markdown(f"# :blue[Lets play some games!] ")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
   player_filter = st.radio('How many Players?',player_options)


with col2:
   style_filter = st.radio("Choose a Style:",style_options)

with col3:
   type_filter = st.radio("Choose a Type:",type_options)

# apply selected filters
filtered_data = data.copy()

#player count
filtered_data = filtered_data[filtered_data['Player_max'] > player_filter - 1]

if style_filter != 'Any':
    filtered_data = filtered_data[filtered_data['Style'] == style_filter ]
    
if type_filter != 'Any':
    filtered_data = filtered_data[filtered_data['Type'] == type_filter ]

# display filtered table
st.write(filtered_data)

st.divider()

with st.expander('Click to toggle => Games Dets'):
    tab1, tab2, tab3 , tab4 ,tab5, tab6, tab7 = st.tabs(["DoodleDash", "FunFacts", "HiveMind","JustOne","MonsDRAWsity","OkayGenius","TopTen"])

with tab7:
    st.header('Top Ten')
    st.markdown("![Alt Text](https://cf.geekdo-images.com/0LVOOyXtNNyFhyj7tFaKCQ__itemrep/img/vfGYy9y2mobyuZvN_XCTMAHNsJo=/fit-in/246x300/filters:strip_icc()/pic5212719.jpg)")
    st.write('a 4-8 player ; co-op clue guessing')
    st.write("Answer a question based on your number (1-10) so the Captain can get the order right!")

with tab6:
    st.header('OkayGenius')
    st.markdown("![Alt Text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSp6Ck61GsvLFu4YLDjNU2CcS-JmDOphZ-OOEtimOsYYArvgTCLwXOThg6iuKJk6FydyTI&usqp=CAU)")
    st.write('a 4-8 player ; competitive trivia \ opinion guessing')
    st.write("Show off your “correct” numbered opinions on ridiculous topics and prove you’re the true Genius!")

with tab5:
    st.header('MonsDRAWsity')
    st.markdown("![Alt Text](https://cf.geekdo-images.com/7oRPCQ_9TzJXw16AG7qrsw__itemrep/img/Zln28fuYYrcMvR1--4A-bFUa8Bc=/fit-in/246x300/filters:strip_icc()/pic5794428.png)")
    st.write('a 4-6 player ; competitive drawing')
    st.write("Paranormal sketch artists draw the monsters a witness says they saw.")
    
with tab4:
    st.header('JustOne')
    st.markdown("![Alt Text](https://cf.geekdo-images.com/ocAuKT9hp99yBY77e4uuPg__itemrep/img/z0G8pfPvUewTm8apjBQHq0qkwAw=/fit-in/246x300/filters:strip_icc()/pic5137279.jpg)")
    st.write('a 4-7 player ; co-op clue guessing')
    st.write("Give one-word clues so someone can guess one word, but duplicate clues are discarded")
    
with tab3:
    st.header('HiveMind')
    st.markdown("![Alt Text](https://cf.geekdo-images.com/XGips7byTMCnylCqOTc-FA__crop100/img/XJGmmuNny-WGh9q-C41_8wYLa8s=/100x100/filters:strip_icc()/pic3043513.jpg)")
    st.write('a 4-8 player ; competitive trivia with no wrong answers')
    st.write("Match answers to win in this hilarious party game!")
    
with tab2:
    st.header('FunFacts')
    st.markdown("![Alt Text](https://cf.geekdo-images.com/wkj9lur-J5Bxun09mnI2rQ__itemrep/img/S-6RpfOqdggo-osnOm_UvMj8Fcg=/fit-in/246x300/filters:strip_icc()/pic7070521.jpg)")
    st.write('a 4-8 player ; co-op number order guessing')
    st.write("Where do you rank compared to everyone else at the table?")
    
with tab1:
    st.header('DoodleDash')
    st.markdown("![Alt Text](https://cf.geekdo-images.com/Vg3qEly2Sx379Vo1t73XCw__itemrep/img/_owG4ZQojPIOmAwtPFko94oiLx0=/fit-in/246x300/filters:strip_icc()/pic6102105.png)")
    st.write('a 4-7 player ; competitive speed drawing & guessing')
    st.write("The drawing competition where speed can beat skill, so anyone can win!")
