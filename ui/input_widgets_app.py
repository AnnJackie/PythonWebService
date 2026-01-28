import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

primary_btn = st.button(label='Press on me!!!', type='primary')
secondary_btn = st.button(label='Then press on meee', type='secondary')

if primary_btn:
    st.write('Hello from primary button')

if secondary_btn:
    st.write('Hello from secondary button')

st.divider()

checkbox = st.checkbox('Remember me')

if checkbox:
    st.write("I will remember you")
else:
    st.write("I will forget you")

st.divider()

data = {
    'year': [2018, 2019, 2020, 2021, 2022],
    'col1': [12, 14, 16, 18, 20],
    'col2': [15, 18, 20, 22, 25],
    'col3': [20, 22, 25, 28, 30]
}

df = pd.DataFrame(data)

radio = st.radio("choose a column", options=df.columns[1:], index=0, horizontal=False)
st.write(radio)

st.divider()

select = st.selectbox("choose a column", options=df.columns[1:], index=0)
st.write(select)

st.divider()

multiselect = st.multiselect("choose a column", options=df.columns[1:])
st.write(multiselect)

st.divider()

slider = st.slider('Pick a number', min_value=0.0, max_value=5.0, step=0.1)
st.write(slider)

st.divider()

text_input = st.text_input('Enter your name:', placeholder='John Doe')
st.write(text_input)

st.divider()


num_input = st.number_input('Enter your age:', min_value=0.0, max_value=5.0, step=0.1, value=2.5)
st.write(num_input)

st.divider()


text_area = st.text_area('Your comment:', height=100, placeholder='Enter you thoughts here...')
st.write(text_area)

