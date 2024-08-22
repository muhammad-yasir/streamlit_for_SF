import pandas as pd
import streamlit as st
import os

st.title("Hierarchical Data Viewer")

st.write("Current working directory:", os.getcwd())
df = pd.read_csv("data\employees.csv",header=0).convert_dtypes()
st.dataframe(df)
edges = ""

for _, row in df.iterrows():
    if not pd.isna(row.iloc[1]):
        edges += f'\t "{row.iloc[0]}" -> "{row.iloc[1]}";\n'

d = f'digraph {{\n{edges}}}'

st.graphviz_chart(d)

#print(d)