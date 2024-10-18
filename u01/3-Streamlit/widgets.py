import streamlit as st

## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
##
##  To run the app in the cmd of containing folder:
#   streamlit run widgets.py 
##
## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


st.title("Streamlit Text Input")
name=st.text_input("Enter your name:")
age = st.slider("Select your age:",0,100,25)

options=["Pythons","Java","C++","C#"]
choice = st.selectbox("Choose your favorite language:",options)

st.write(f"your age is {age}")
st.write(f"your favourite language is {choice}")

if name:
    st.write(f"Hello, {name}")
