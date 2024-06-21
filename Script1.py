from re import template
from httpx import options
import streamlit as st
import pandas as pd
import plotly.express as px
from applicationfunctions import pca_maker

st.set_page_config(layout="wide")

scatter_column, settings_column = st.columns((4,1))

scatter_column.title("Multi-Dimensional Product Analysis")

settings_column.title("Parameters")

## The PCA plot will have PCA1 on one axis and PCA2 on the other, then we plot every point individually

uploaded_file = settings_column.file_uploader("Choose file")

if uploaded_file is not None:
    data_import = pd.read_excel(uploaded_file)
    pca_data, cat_cols, pca_cols= pca_maker(data_import)
    
    categorical_variable = settings_column.selectbox("Variable Select", options= cat_cols)
    cat_cols.remove(categorical_variable)
    categorical_variable2 = settings_column.selectbox("Variable Select 2", options= cat_cols)
    size_variable = settings_column.selectbox("Size Depends on:", options= pca_data.columns)
    
    pca_1 = settings_column.selectbox("First Priciple Component", options = pca_cols)
    pca_cols.remove(pca_1)
    pca_2 = settings_column.selectbox("Second Priciple Component", options = pca_cols )
    
    scatter_column.plotly_chart(px.scatter(data_frame = pca_data, x=pca_1, y=pca_2, color = categorical_variable, template="simple_white", height = 800, hover_data = [categorical_variable2], size = size_variable), use_container_width= True)
else:
    scatter_column.header("Please choose a file")
    






