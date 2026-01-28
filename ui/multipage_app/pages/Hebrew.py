import streamlit as st

# Inject CSS for RTL support
st.markdown("""
    <style>
    body, html, div, p, input, label, textarea {
        direction: RTL;
        text-align: right;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("שלום עולם")
st.write("זהו טקסט בעברית המיושר לימין.")
st.text_input("הכנס טקסט:")