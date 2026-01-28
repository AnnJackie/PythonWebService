import streamlit as st

st.title("Counter with Session State")

if 'counter' not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment"):
    st.session_state.counter += 1
    st.write("Counter incremented!")

if st.button("Reset"):
    st.session_state.counter = 0
    st.write("Counter reset.")

if st.button("Check"):
    st.write("You press on check - counter state persists.")

st.write(f"Current counter value: {st.session_state.counter}")






# ## Example of how the counter not remain updated without state manegment
# import streamlit as st
#
# # Set up the app title
# st.title("Counter Without Session State")
#
# # Initialize counter (will reset on every interaction)
# counter = 0
#
# # Button to increment the counter
# if st.button("Increment"):
#     counter += 1
#     st.write("Counter incremented!")
#
# # Button to reset the counter
# if st.button("Reset"):
#     counter = 0
#     st.write("Counter reset.")
#
# # Simulate a restart function (in reality, just re-runs the script)
# if st.button("Simulate Restart"):
#     st.write("Simulated restart - counter resets to 0.")
#
# # Display the current counter value
# st.write(f"Current counter value: {counter}")
