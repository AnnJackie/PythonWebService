import streamlit as st
import pandas as pd
import numpy as np

st.title("Dashboard")
st.write("This is the dashboard page where you can see data visualizations.")

data = pd.DataFrame(np.random.randn(10, 3), columns=['A', 'B', 'C'])

st.line_chart(data)


