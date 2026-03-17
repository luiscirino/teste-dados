import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((20,3)), columns=['a','b','c'])

st.write("Meu primeiro teste com o streamlit")
st.bar_chart(df)