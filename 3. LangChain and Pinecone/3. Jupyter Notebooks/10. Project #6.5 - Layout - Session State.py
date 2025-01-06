# Install all libraries by browsing to this file locations and running in the terminal: pip install -q -r requirement-list.txt>

# Interesting https://docs.streamlit.io/develop/concepts/design/buttons

# Run like this:  streamlit run <filename.py>

# pip install streamlit

# streamlit hello  -> will display a demo app to confirm that it is working

# At every file change, streamlit runs the py file top to bottom

# To help the overhead, streamlit has caching options. 

#----------------------------------------------------------------------------------#

#Session

# Whe your run a streamlit app and access it from the browser - that is a session.

# A session is a Python object that exists in memory to share data betwen runs

# For each tab of streamlit app, that is a new independnent session.

# SESSION STATE

import streamlit as st

st.title('Streamlit Session')
st.write(st.session_state)

# note that you can use both [] notation or . notation for the session_state
if 'counter' not in st.session_state:
    st.session_state['counter'] = 0
else:
    st.session_state.counter += 1

st.write(f'Counter: {st.session_state.counter}')

button = st.button('Update state')
if 'clicks' not in st.session_state:
    st.session_state['clicks'] = 0

if button:
    st.session_state['clicks'] += 1
    f'After pressing button {st.session_state}'

number = st.slider('Value', 1, 10, key='my_slider')
st.write(st.session_state)
st.write(number)

# Run it: streamlit run .\file.py