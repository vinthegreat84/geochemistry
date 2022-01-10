import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly import tools

# layout
    # Section - dataset
        # siderbar: data selection - example data or user data in dropdown
        # data template to download
        # composite in dropdown to select (dafult none)
        # composite to merge with sample

    # section - WIs
        # WI table
        # Boxplot
        # scatter matrix
        # Correlation diagrams

    # section - variation plot

    # section - Compositional space diagrams
        # A-CN-K Compositional space diagram
        # M-F-W Compositional space diagram
        # A-CNK-FM Compositional space diagram

st.title("GEOCHEM 1.0")
st.markdown("App to analyze major elmental geochemistry of clastic sediments")             

# major elemental data template
url = 'https://raw.githubusercontent.com/vinthegreat84/geochemistry/master/template.csv'
df = pd.read_csv(url)

@st.cache
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df(df)
st.download_button("Press to download major elemental data template",csv,"template.csv","csv",key='download1-csv')

data = st.sidebar.selectbox('Select Dataset',('Example data', 'User data'))

st.write(data)

def get_data(name):
    data = None
    if name == 'Example data':
        url = 'https://raw.githubusercontent.com/vinthegreat84/geochemistry/master/SedWeather/raw/sedchem.csv'
        df = pd.read_csv(url)
    else:
        uploaded_file = st.file_uploader("Choose a CSV file")
        col_list =["sample","category","subcategory","subsubcategory","reference","SiO2","TiO2","Al2O3","Fe2O3","FeO","MnO","MgO","CaO","Na2O","K2O","P2O5","CO2"]
        df = pd.read_csv(uploaded_file, usecols=col_list)
    return df

data = get_data(data)

st.write(data)

@st.cache
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')
csv = convert_df(df)
st.download_button("Press to download",csv,"sedchem.csv","csv",key='download2-csv')