import streamlit as st
import pandas as pd
import numpy as np

## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
##
##  To run the app in the cmd of containing folder:
#   streamlit run app.py 
##
## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


## Title of the app
st.title("Hello Streamlit")

## Display a Simple Text
st.write("This is a simple text")

## create a simple data frame
df=pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})

## display the data frame
st.write("here is the dataframe")
st.write(df)

## create a line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c'] ## randn 20 righe, 3 colonne
)
st.line_chart(chart_data)