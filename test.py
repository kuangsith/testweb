import pandas as pd
import datetime
import get_price_binanace
import streamlit as st
import numpy

df = pd.DataFrame(columns = ['Age','Income'])

for i in range(20):
  df = df.append({'Age': random.randint(15,60),'Income':10000+40000*random.random()},ignore_index=True)

with st.expander("Section 1"):
  st.dataframe(df)
