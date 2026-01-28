import streamlit as st
import pandas as pd

with st.sidebar:
    st.write("Text in the sidebar")

col1, col2, col3 = st.columns(3)

col1.write("Text in a column")
slider = col2.slider("Choose a number", min_value=0, max_value=10)
col3.write(slider)


data = {
    'year': [2018, 2019, 2020, 2021, 2022],
    'sales': [10, 12, 14, 16, 18],
    'marketing': [15, 18, 20, 22, 25],
    'development': [20, 22, 25, 28, 30],
}

df = pd.DataFrame(data)

tab1, tab2 = st.tabs(["Line plot", "Bar plot"])

with tab1:
    tab1.write("A line plot")
    st.line_chart(df, x="year", y=["sales", "marketing", "development"])

with tab2:
    tab2.write("A bar plot")
    st.bar_chart(df, x="year", y=["sales", "marketing", "development"])

with st.expander("Click to expand"):
    st.write("I am text that you only see when you expand")

with st.container():
    st.write("This is inside the container")

st.write("This is outside the container")




