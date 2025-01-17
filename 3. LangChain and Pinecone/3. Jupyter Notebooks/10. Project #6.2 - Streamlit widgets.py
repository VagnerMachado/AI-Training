# Install all libraries by browsing to this file locations and running in the terminal: pip install -q -r requirement-list.txt>

# Interesting https://docs.streamlit.io/develop/concepts/design/buttons

# Run like this:  streamlit run <filename.py>

# pip install streamlit

# streamlit hello  -> will display a demo app to confirm that it is working

# At every file change, streamlit runs the py file top to bottom
# To help the overhead, streamlit has caching options. 

#----------------------------------------------------------------------------------#

# STREAMLIT WIDGETS

import streamlit as st
import pandas as pd

# TEXT INPUT
name = st.text_input('Your name: ')
if name:
    st.write(f'Hello {name}!')

# NUMBER INPUT
x = st.number_input('Enter a  number', min_value=1, max_value=99, step=1) # Step will indicate by how many units the values will change when + or - is clicked. 
st.write(f'The current number is {x}')

st.divider()  # draw a horizontal line

# BUTTON
clicked = st.button('Click me!')
if clicked:
    st.write(':ghost:' * 3)

st.divider()

# CHECKBOX
agree = st.checkbox('I agree')
if agree:
    'Great, you agreed!'


checked = st.checkbox('Continue', value=True)
if checked:
    ':+1:' * 5

df = pd.DataFrame({'Name': ['Anne', 'Mario', 'Douglas'],
                   'Age': [30, 25, 40]
                   })
if st.checkbox('Show data'):
    st.write(df)

st.divider()

# RADIO BUTTONS
pets = ['cat', 'dog', 'fish', 'turtle']
pet = st.radio('Favorite pet', pets, index=2, key='your_pet')
st.write(f'Your favorite pet: {pet}')
st.write(f'Your favorite pet: {st.session_state.your_pet * 3}')

st.divider()

# SELECT BOXES
cities = ['London', 'Berlin', 'Paris', 'Madrid']
city = st.selectbox('Your city', cities, index=1)
st.write(f'You live in {city}')

st.divider()

# SLIDER
x = st.slider('Number Slider', value=15, min_value=12, max_value=78, step=3) # Step will indicate by how many units the values will change when dragged 
st.write(f'x is {x}')

st.divider()

# FILE UPLOADER
uploaded_file = st.file_uploader('Upload a file:', type=['txt', 'csv', 'xlsx'])
if uploaded_file:
    st.write(uploaded_file)
    if uploaded_file.type == 'text/plain':
        from io import StringIO
        stringio = StringIO(uploaded_file.getvalue().decode('utf-8'))
        string_data = stringio.read()
        st.write(string_data)
    elif uploaded_file.type == 'text/csv':
        import pandas as pd
        df = pd.read_csv(uploaded_file)
        st.write(df)
    else:
        import pandas as pd
        df = pd.read_excel(uploaded_file)
        st.write(df)


# CAMERA INPUT
camera_photo = st.camera_input('Take a photo')
if camera_photo:
    st.image(camera_photo)

st.image("https://getwallpapers.com/wallpaper/full/0/b/d/53558.jpg", width=700);

# Run it: streamlit run .\file.py