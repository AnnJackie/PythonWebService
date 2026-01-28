import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

with st.form("form_key"):
    st.write("What would like to order")

    appetizer = st.selectbox("Appetizers", options=["Bruschetta", "Stuffed Mushrooms", "Garlic Bread"])
    main = st.selectbox("Main Course", options=["Grilled Salmon", "Spaghetti Carbonara", "Chicken Parmesan"])
    dessert = st.selectbox("Dessert", options=["Tiramisu", "Cheesecake", "Chocolate Lava Cake"])

    wine = st.checkbox("Are you bringing wine?")

    visit_date = st.date_input("When are you coming?")

    visit_time = st.time_input("At what time are you coming?")

    allergies = st.text_area("Any allergies?", placeholder="Leave us a note for allergies")

    submit_btn = st.form_submit_button("Submit")

st.write(f"""Your order summary:

Appetizer: {appetizer}

Main course: {main}

Dessert: {dessert}

Are you bringing your own wine: {"yes" if wine else "no"}

Date of visit: {visit_date}

Time of visit: {visit_time}

Allergies: {allergies}
""")


