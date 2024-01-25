import streamlit as st
st.title('My first streamlit app')
st.write("Here's is my first streamlit app")
user_input = st.text_input("Please enter your name", "Harry Potter")
st.write('Hello', user_input)
