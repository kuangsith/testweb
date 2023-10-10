import pandas as pd
import datetime
import streamlit as st
import numpy

# df = pd.DataFrame(columns = ['Age','Income'])

# for i in range(20):
#   df.loc[len(df)] = [random.randint(15, 60), 10000 + 40000 * random.random()]

df = pd.read_csv('yoyo.csv',index=True)

with st.expander("Section 1"):
  st.dataframe(df)


st.scatter(x=df['Age'],y=df['Income'])
