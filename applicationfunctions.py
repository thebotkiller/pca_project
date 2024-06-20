import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn import preprocessing
import numpy as np
from sklearn.preprocessing import StandardScaler

def pca_maker(data_import):
    data_import = pd.read_excel("D:\Coding\PCA_Stuff\PCA_Dataset.xlsx")
    print(data_import.head())

    numerical_columns= []
    categorical_columns=[]

    for i in data_import.columns:
        if data_import[i].dtype == np.dtype("float64") or data_import[i].dtype == np.dtype("int64"):
            numerical_columns.append(data_import[i])
        else:
            categorical_columns.append(data_import[i])
            
        
    numerical_data = pd.concat(numerical_columns, axis = 1)
    categorical_data = pd.concat(categorical_columns, axis = 1)

    numerical_data = numerical_data.apply(lambda x: x.fillna(np.mean(x)), ) #gets rid of the NA entries

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(numerical_data)
    scaled_data

    pca = PCA()
    pca_data = pca.fit_transform(scaled_data)
    pca_data = pd.DataFrame(pca_data)
    pca_data

    column_names = ["PCA_" + str(i) for i in range(1, len(pca_data.columns)+ 1)]

    column_mapper = dict(zip(list(pca_data.columns), column_names))

    pca_data.rename(columns = column_mapper, inplace = True)

    output = pd.concat([data_import, pca_data], axis = 1)
    
    return output, list(categorical_data.columns),column_names

