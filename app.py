# import the streamlit library
import streamlit as st

import random

keys = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
scales = ["Major", "Minor"]
patterns = [
    "1,3 - 2,4 - etc.",
    "1,2,3 - 2,3,4 - etc.",
    "3,2,1 - 4,3,2 - etc.",
    "1,3,5 - 2,4,6 - etc.",
    "1,2,3,4 - 2,3,4,5 - etc.",
    "1,2,3,1 - 2,3,4,2 - etc.",
    "1,3,2,1 - 2,4,3,2 - etc.",
    ]

# give a title to our app
st.title('Welcome to Random Scale Excercise')

# check if the button is pressed or not
if(st.button('Randomize excercise!')):

    selected_key = keys[random.randint(0, len(keys) - 1)]
    selected_scale = scales[random.randint(0, len(scales) - 1)]
    selected_pattern = patterns[random.randint(0, len(patterns) - 1)]

    st.text(f"Key:     {selected_key}")
    st.text(f"Scale:   {selected_scale}")
    st.text(f"Pattern: {selected_pattern}")
