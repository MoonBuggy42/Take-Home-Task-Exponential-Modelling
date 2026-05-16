import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
st.title('Modelling Exponential Growth and Decay')

st.subheader('Richter Scale: Q2')
df1 = pd.read_excel(r"C:/Users/Mihin/Documents/Richter Scale .xlsx", index_col=0)
