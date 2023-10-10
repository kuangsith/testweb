import pandas as pd
import datetime
import streamlit as st
import numpy

# df = pd.DataFrame(columns = ['Age','Income'])

# for i in range(20):
#   df.loc[len(df)] = [random.randint(15, 60), 10000 + 40000 * random.random()]

df = pd.read_csv('yoyo.csv')
df['Income'] = df['Income'].apply(lambda x: round(x,2))

with st.expander("Click to see DF"):
  st.dataframe(df)


st.scatter_chart(df,x='Age',y='Income')
