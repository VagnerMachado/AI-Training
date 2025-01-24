# Install all libraries by browsing to this file locations and running in the terminal: pip install -q -r requirement-list.txt>

# Interesting https://docs.streamlit.io/develop/concepts/design/buttons

# Run like this:  streamlit run <filename.py>

# pip install streamlit

# streamlit hello  -> will display a demo app to confirm that it is working

# At every file change, streamlit runs the py file top to bottom

# To help the overhead, streamlit has caching options. 

#----------------------------------------------------------------------------------#

#Callback

#

# CALLBACKS

# This is a functions that gets callend when the user interacts with a widget
#on_change(slider, text box) and on_click(button) are the interactive methods

import streamlit as st

st.subheader('Distance converter')

def miles_to_km():
    st.session_state.km = st.session_state.miles * 1.609

def km_to_miles():
    st.session_state.miles = st.session_state.km * 0.621

# Page layout
col1, buff, col2 = st.columns([2, 1, 2])
with col1:
    miles = st.number_input('Miles:', key='miles', on_change=miles_to_km) # key adds the value to the state

with col2:
    km = st.number_input('Km:', key='km', on_change=km_to_miles)

# Run it: streamlit run .\file.py