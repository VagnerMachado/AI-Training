# Install all libraries by browsing to this file locations and running in the terminal: pip install -q -r requirement-list.txt>

# Interesting https://docs.streamlit.io/develop/concepts/design/buttons

# Run like this:  streamlit run <filename.py>

# pip install streamlit

# streamlit hello  -> will display a demo app to confirm that it is working

# At every file change, streamlit runs the py file top to bottom
# To help the overhead, streamlit has caching options. 

#----------------------------------------------------------------------------------#

# Displaying data on the screen:
# 1. st.write()
# 2. Magic 🙂

import streamlit as st
import pandas as pd

st.title('Hello Streamlit World! :100:')

st.write('We learn Streamlit!')

l1 = [1, 2, 3]
st.write(l1)

l2 = list('abc')
d1 = dict(zip(l1, l2))
st.write(d1)

# using magic
'Displaying using magic :smile:'

df = pd.DataFrame({
    'first_column': [1, 2, 3, 4],
    'second_column': [10, 20, 30, 40]
})

df #magic: wlll implicitly call the  st.write(df)
# more emoji shot codes:https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
# Run it: streamlit run .\file.py

