import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


st.title("Streamlit Commands Example")

st.header("This is a header")

st.subheader("This is a subheader")

st.text("This is simple preformatted text using st.text.")

st.code("""
def hello_world():
    print("Hello, Streamlit!")

hello_world()
""", language='python')

st.divider()

st.write("This is a simple string using st.write.")
st.write("You can also pass Markdown with **bold** and _italic_ text using st.write.")

data = {
    'year': [2018, 2019, 2020, 2021, 2022],
    'col1': [12, 14, 16, 18, 20],
    'col2': [15, 18, 20, 22, 25],
    'col3': [20, 22, 25, 28, 30]
}

df = pd.DataFrame(data)

st.write("Here is a DataFrame:", df)

st.line_chart(df, x='year', y=['col1', 'col2', 'col3'])

st.area_chart(df, x='year', y=['col1', 'col2'])

st.bar_chart(df, x='year', y=['col1', 'col2', 'col3'])

fig, ax = plt.subplots()

ax.plot(df['year'], df['col1'], marker='o')
ax.set_title('col1 VS year')
ax.set_xlabel('year')
ax.set_ylabel('col1')

st.pyplot(fig)

st.divider()

plt.figure(figsize=(10, 6))

for col in ['col1', 'col1', 'col3']:
    sns.lineplot(x='year', y=col, data=df, marker='o', label=col)

plt.title('Trends over the years')
plt.xlabel('year')
plt.ylabel('values')
st.pyplot(plt)