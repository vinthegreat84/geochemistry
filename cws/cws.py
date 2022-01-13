import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly import tools
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt
# import io
# import os
# import base64
# from PIL import Image

# layout
    # Section - home
    # Section - flowchart

# to do
# spider plot
##############################################################################################################
# home
def home():
    st.title('CWS 0.1.0')
    st.subheader('App to analyze major elemental geochemical data of clastic sediments')
    st.caption('Check the sidebar options (top-left arrow to be clicked, if sidebar is not visible)')
    st.subheader('Created by Vinay Babu')
    st.write('''CWS is a tool designed using Python and Streamlit to analyze major elemental geochemistry of clastic sediments.''')
    st.write('One may navigate to different options on the sidebar menu.')
    st.write('\n')
    st.write('### Sections')
    st.write('**Data panel:** Selection of the major elemental geochemical dataset.')
    st.write('**Variation diagram:** Variation of major oxides against samples.')
    st.write('**Data filter:** Data filter based on sample/category/subcategory/subsubcategory.')
    st.write('**Weathering proxy:** Data table of chemical weathering indices including Chemical Index of Weathering (CIW) after *Harnois, 1988*; Chemical Proxy of Alteration (CPA) after *Buggle et al., 2011*; Chemical Index of Alteration (CIA) after *Nesbitt and Young, 1982*; Plagioclase Index of Alteration (PIA) after *Fedo et al., 1995*; Modified Chemical Index of Alteration (CIX) after *Garzanti et al., 2014*; Index of Compositional Variability (ICV) after *Cox et al., 1995*; Weathering Index of Parker (WIP) after *Parker, 1970* and and chemical proxies like SiO2/Al2O3, K2O/Al2O3, Al2O3/TiO2.')
    st.write('**Compositional space diagram:** Compositional space diagrams including A - CN - K compositional space diagram after *Nesbitt and Young, 1982*; A - CNK - FM compositional space diagram after *Nesbitt and Young, 1989* and M - F - W compositional space diagramm after *Ohta and Arai, 2007*.')
    st.write('**Boxplot, Scatter matrix, Correlation matrix and Heatmap:** Boxplot, Scatter matrix, Correlation matrix and Heatmap of chemical weathering indices and proxies.')
        
##############################################################################################################


##############################################################################################################
# Dataset
def data_analysis():
    st.header('Data panel')
    # major elemental data template
    url = 'https://raw.githubusercontent.com/vinthegreat84/geochemistry/master/template.csv'
    df = pd.read_csv(url)

    @st.cache
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')

    template = convert_df(df)
    st.download_button("Press to download a csv data template to analyze your data", template, "template.csv", "csv", key='download-template-csv')
    
    st.write('\n')
    
    data = st.selectbox('Select Dataset',('Example data', 'User data'))

    st.write(data)

    def get_data(name):
        data = None
        if name == 'Example data':
            url = 'https://raw.githubusercontent.com/vinthegreat84/geochemistry/master/SedWeather/raw/sedchem.csv'
            df = pd.read_csv(url)
        else:
            uploaded_file = st.file_uploader("Choose a CSV file (max 200 MB)")
            col_list =["sample","category","subcategory","subsubcategory","reference","SiO2","TiO2","Al2O3","Fe2O3","FeO","MnO","MgO","CaO","Na2O","K2O","P2O5","CO2"]
            df = pd.read_csv(uploaded_file, usecols=col_list)
        return df

    data = get_data(data)

    st.write(data)

    @st.cache
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')
    sample = convert_df(df)
    st.download_button("Press to download",sample,"sample.csv","csv",key='download-sample-csv')
    
#     # variation plot
#     if st.checkbox('Variation plot'):
#         st.header('Variation plot')
#         y = st.selectbox('Select the y-axis',(list(data)))
#         variation = px.scatter(data, x="sample", y=y, hover_name="sample",color="subcategory", symbol="subsubcategory", render_mode="webgl", title="Variation Plot", color_discrete_sequence=px.colors.qualitative.Antique
#     )
#         st.plotly_chart(variation, use_container_width=True)
    
    # normalized spider diagram
    if st.checkbox('Variation diagram'):
        st.header('Variation diagram')
        data_var = data

        if st.checkbox('Categorization'):
            type = st.radio('Categorization', ['Category','Subcategory','Subsubcategory'])
            if type=='Category':
                cat = st.selectbox("Select the Catgory:", data_var['category'].unique())
                data_var = data_var[data_var['category'].isin([cat])]
            elif type=='Subcategory':
                cat = st.selectbox("Select the Subcatgory:", data_var['subcategory'].unique())
                data_var = data_var[data_var['subcategory'].isin([cat])]
            else:
                cat = st.selectbox("Select the Subsubcatgory:", data_var['subsubcategory'].unique())
                data_var = data_var[data_var['subsubcategory'].isin([cat])]
        
        st.write(data_var)
    
        var = alt.Chart(data_var).transform_fold(
            ['SiO2','TiO2','Al2O3','Fe2O3','FeO','MnO','MgO','CaO','Na2O','K2O','P2O5','CO2'],
        ).mark_line().encode(
            x=alt.X('sample:N', axis=alt.Axis(title='Sample'), sort=None),
            y=alt.Y('value:Q', axis=alt.Axis(title='Variation %')),
            color=alt.Color('key:N', legend=alt.Legend(title="Oxide"))
        ).interactive().properties(width='container')        
        st.altair_chart(var, use_container_width=True)

#         if st.checkbox('Normalization'):
#             norm = st.selectbox("Select the Sample:", data_var['sample'].unique())         
#             data_norm = data_var[data_var['sample'].isin([norm])]
#             st.write(data_norm)
#             data_norm = data_var.loc[:,"SiO2":].div(data_norm.iloc[0]["SiO2":])
#             st.write(data_norm)
        
#             var = alt.Chart(data_norm).transform_fold(
#                 ['SiO2','TiO2','Al2O3','Fe2O3','FeO','MnO','MgO','CaO','Na2O','K2O','P2O5','CO2'],
#             ).mark_line().encode(
#                 x=alt.X('sample:N', axis=alt.Axis(title='Sample'), sort=None),
#                 y=alt.Y('value:Q', axis=alt.Axis(title='Variation %')),
#                 color=alt.Color('key:N', legend=alt.Legend(title="Oxide"))
#             ).interactive().properties(width='container')        
#             st.altair_chart(var, use_container_width=True)

#         spider = px.line(data, x="sample", y=y, hover_name="sample",color="subcategory", symbol="subsubcategory", render_mode="webgl", title="Variation Plot", color_discrete_sequence=px.colors.qualitative.Antique
#     )
#         st.plotly_chart(spider, use_container_width=True)
    
#         # plot download
#         buffer = io.StringIO()
#         variation.write_html(buffer, include_plotlyjs='cdn')
#         html_bytes = buffer.getvalue().encode()

#         st.download_button(
#             label='Download HTML',
#             data=html_bytes,
#             file_name='variation.html',
#             mime='text/html'
#         )

# Weathering Indices calculation
    # molar weights calculation
    data['molar_SiO2']  = data['SiO2']/60.08
    data['molar_TiO2']  = data['TiO2']/79.866
    data['molar_Al2O3'] = data['Al2O3']/101.9618
    data['molar_Fe2O3'] = data['Fe2O3']/159.69
    data['molar_MnO']   = data['MnO']/70.9374
    data['molar_MgO']   = data['MgO']/40.3044
    data['molar_CaO']   = data['CaO']/56.0794
    data['molar_Na2O']  = data['Na2O']/61.97894
    data['molar_K2O']   = data['K2O']/94.1954
    data['molar_P2O5']  = data['P2O5']/141.944522
    data['molar_CO2']   = data['CO2']/44.01

    # CaO* calculation
    # After McLennan, 1993
    data['diff'] = data['molar_CaO'] - (data['molar_CO2'] + data['molar_P2O5'])
    data['molar_CaO*'] = np.where(data['diff'] < data['molar_Na2O'], data['diff'], data['molar_Na2O'])
    
    # Chemical Index of Weathering (CIW) after Harnois, 1988
    data['(CIW)'] = 100 * data['molar_Al2O3'] / (data['molar_Al2O3'] + data['molar_CaO*'] + data['molar_Na2O']) 

    # Chemical Proxy of Alteration (CPA) after Buggle et al., 2011  
    data['(CPA)'] = 100 * data['molar_Al2O3'] / (data['molar_Al2O3'] + data['molar_Na2O']) 

    # Chemical Index of Alteration (CIA) after Nesbitt and Young, 1982
    data['(CIA)'] = 100 * data['molar_Al2O3'] / (data['molar_Al2O3'] + data['molar_CaO*'] + data['molar_Na2O'] + data['molar_K2O']) 

    # Plagioclase Index of Alteration (PIA) after Fedo et al., 1995
    data['(PIA)'] = 100 * (data['molar_Al2O3'] - data['molar_K2O']) / (data['molar_Al2O3'] + data['molar_CaO*'] + data['molar_Na2O'] 
                                                                       - data['molar_K2O'])

    # Modified Chemical Index of Alteration (CIX) after Garzanti et al., 2014                                                            
    data['(CIX)'] = 100 * data['molar_Al2O3'] / (data['molar_Al2O3'] + data['molar_Na2O'] + data['molar_K2O']) 

    # Index of Compositional Variability (ICV) after Cox et al., 1995
    data['(ICV)'] = (data['Fe2O3'] + data['K2O'] + data['Na2O'] + data['CaO'] + data['MgO'] + data['MnO'] + data['TiO2']) / data['Al2O3']

    # Weathering Index of Parker (WIP) after Parker, 1970
    data['(WIP)'] = 100 * (2*data['molar_Na2O']/0.35 + data['molar_MgO']/0.9 + 2*data['molar_K2O']/0.25 + data['molar_CaO*']/0.7)
    
    # ratios
    data['SiO2/Al2O3'] = data['SiO2'] / data['Al2O3']
    data['K2O/Al2O3']  = data['K2O'] / data['Al2O3']
    data['Al2O3/TiO2'] = data['Al2O3'] / data['TiO2']
    
#     # dropping extra variables
#     data=data.drop(['CO2', 'molar_SiO2', 'molar_TiO2', 'molar_Al2O3', 'molar_Fe2O3', 'molar_MnO', 'molar_MgO', 'molar_CaO','molar_Na2O', 'molar_K2O', 'molar_P2O5', 'molar_CO2', 'diff', 'molar_CaO*'], axis=1)
    
    # data filter     
    if st.checkbox('Data filter'):
        st.header('Data filter')
        # selection of country from 'location'
        filter = st.radio('Select the filter:',['sample', 'category', 'subcategory','subsubcategory'])
        if filter=='sample':
            sample = st.multiselect("Select the Samples:", data['sample'].unique())
            data_sample = data[data['sample'].isin(sample)]
            data = data_sample   
        if filter=='category':
            cat = st.selectbox("Select the Catgory:", data['category'].unique())
            data_cat = data[data['category'].isin([cat])]
            data = data_cat
        if filter=='subcategory':
            subcat = st.selectbox("Select the Subcatgory:", data['subcategory'].unique())
            data_subcat = data[data['subcategory'].isin([subcat])]
            data = data_subcat
        if filter=='subsubcategory':
            subsubcat = st.selectbox("Select the Subsubcatgory:", data['subsubcategory'].unique())
            data_subsubcat = data[data['subsubcategory'].isin([subsubcat])]
            data = data_subsubcat              
             
    if st.checkbox('Weathering proxy'):
        st.header('Weathering proxy')
        proxy =["sample","category","subcategory","subsubcategory","reference","(CIW)","(CPA)","(CIA)","(PIA)","(CIX)","(ICV)","(WIP)","SiO2/Al2O3","K2O/Al2O3","Al2O3/TiO2"]
        proxy=data[proxy]
        st.write(proxy)
        
        @st.cache
        def convert_df(proxy):
            return proxy.to_csv(index=False).encode('utf-8')
        proxy = convert_df(proxy)
        st.download_button("Press to download",proxy,"proxy.csv","csv",key='download-proxy-csv')
    
    # Category plot
    def tern(x,y,z,color,symbol,hover_name):
        tern_plot = px.scatter_ternary(data, a=x, b=y, c=z, color=color, symbol=symbol, hover_name=hover_name, color_discrete_sequence=px.colors.qualitative.Antique)
        
        tern_plot.update_layout({'ternary': {'sum': 100}})
        tern_plot.update_ternaries(bgcolor='yellow')
        tern_plot.update_traces(marker=dict(size=12, line=dict(width=2, color='DarkSlateGrey')), selector=dict(mode='markers'))
        
        tern_plot.update_layout({
            'ternary':
                {
                'sum':100,
                'aaxis':{'title': title_x},
                'baxis':{'title': title_y},
                'caxis':{'title': title_z}
                }
        })
        st.plotly_chart(tern_plot, use_container_width=True)
    
    # Compositional space diagrams selection
    if st.checkbox('Compositional space diagram'):
        st.header('Compositional space diagram')
        csd =["sample","category","subcategory","subsubcategory","reference","SiO2","TiO2","Al2O3","Fe2O3","MgO","CaO","Na2O","K2O","molar_Al2O3","molar_CaO*","molar_Na2O","molar_K2O","molar_Fe2O3","molar_MgO"]
        data_csd=data[csd]        
        csd_type = st.radio('Compositional space diagram:',['A - CN - K', 'A - CNK - FM', 'M - F - W'])
        type = st.radio('Categorization', ['Category','Subcategory'])
        if type=='Category':
            color=data_csd['category']
            symbol=None
        else:
            color=data_csd['subcategory']
            symbol=data_csd['subsubcategory']
        x=data_csd['molar_Al2O3']
        hover_name=data_csd['sample']
        if csd_type == 'A - CN - K':
            y=data_csd['molar_CaO*'] + data_csd['molar_Na2O']            
            z=data_csd['molar_K2O']
            title_x = 'Al<sub>2</sub>O<sub>3</sub>'
            title_y = 'CaO*+Na<sub>2</sub>O'
            title_z = 'K<sub>2</sub>O'
        elif csd_type == 'A - CNK - FM':
            y=data_csd['molar_CaO*'] + data_csd['molar_Na2O'] + data_csd['molar_K2O']           
            z=data_csd['molar_Fe2O3'] + data_csd['molar_MgO']
            title_x = 'Al<sub>2</sub>O<sub>3</sub>'
            title_y = 'CaO*+Na<sub>2</sub>O+K<sub>2</sub>O'
            title_z = 'Fe<sub>2</sub>O<sub>3</sub>+MgO'
        else:
            # eight oxides (SiO2, TiO2, Al2O3, Fe2O3, MgO, CaO, Na2O and K2O) used in the formulas and re-closing to 100 wt.% (expressed as OXIDE.100 = 100*OXIDE/sum)
            data_csd['sum'] = data_csd[['SiO2', 'TiO2', 'Al2O3', 'Fe2O3', 'MgO', 'CaO', 'Na2O', 'K2O']].sum(axis=1)

            data_csd['SiO2.100']  = 100 * data_csd['SiO2']  / data_csd['sum']
            data_csd['TiO2.100']  = 100 * data_csd['TiO2']  / data_csd['sum']
            data_csd['Al2O3.100'] = 100 * data_csd['Al2O3'] / data_csd['sum']
            data_csd['Fe2O3.100'] = 100 * data_csd['Fe2O3'] / data_csd['sum']
            data_csd['MgO.100']   = 100 * data_csd['MgO']   / data_csd['sum']
            data_csd['CaO.100']   = 100 * data_csd['CaO']   / data_csd['sum']
            data_csd['Na2O.100']  = 100 * data_csd['Na2O']  / data_csd['sum']
            data_csd['K2O.100']   = 100 * data_csd['K2O']   / data_csd['sum']

            # M - F - W apices calculation after Ohta and Arai, 2007
            ## Step 1 of the formulas for calculating vertices (M, F and W) of M - F - W compositional space diagram
            data_csd['(M)'] = - 0.395*np.log(data_csd['SiO2.100']) + 0.206*np.log(data_csd['TiO2.100']) - 0.316*np.log(data_csd['Al2O3.100']) + 0.160*np.log(data_csd['Fe2O3.100']) + 0.246*np.log(data_csd['MgO.100']) + 0.368*np.log(data_csd['CaO.100']) + 0.073*np.log(data_csd['Na2O.100']) - 0.342*np.log(data_csd['K2O.100']) + 2.266
            data_csd['(F)'] = + 0.191*np.log(data_csd['SiO2.100']) - 0.397*np.log(data_csd['TiO2.100']) + 0.020*np.log(data_csd['Al2O3.100']) - 0.375*np.log(data_csd['Fe2O3.100']) - 0.243*np.log(data_csd['MgO.100']) + 0.079*np.log(data_csd['CaO.100']) + 0.392*np.log(data_csd['Na2O.100']) + 0.333*np.log(data_csd['K2O.100']) - 0.892
            data_csd['(W)'] = + 0.203*np.log(data_csd['SiO2.100']) + 0.191*np.log(data_csd['TiO2.100']) + 0.296*np.log(data_csd['Al2O3.100']) + 0.215*np.log(data_csd['Fe2O3.100']) - 0.002*np.log(data_csd['MgO.100']) - 0.448*np.log(data_csd['CaO.100']) - 0.464*np.log(data_csd['Na2O.100']) + 0.008*np.log(data_csd['K2O.100']) - 1.374

            ## Step 2 of the formulas for calculating vertices (M, F and W) of M - F - W compositional space diagram
            data_csd['(M)'] = np.exp(data_csd['(M)'])
            data_csd['(F)'] = np.exp(data_csd['(F)'])
            data_csd['(W)'] = np.exp(data_csd['(W)'])

            x=data_csd['(M)']
            y=data_csd['(F)']            
            z=data_csd['(W)']
            title_x = 'M'
            title_y = 'F'
            title_z = 'W'
            
        fig = tern(x,y,z,color,symbol,hover_name)
    
    # boxplot
    def box(x,y,color):
        box = px.box(data, x=x, y=y, color=color)
        box.update_layout(showlegend=False)
        st.plotly_chart(box, use_container_width=True)
            
    if st.checkbox('Boxplot, Scatter matrix, Correlation matrix and Heatmap'):
        st.header('Boxplot, Scatter matrix, Correlation matrix and Heatmap')
        ox_px =["sample","category","subcategory","subsubcategory","reference","SiO2","TiO2","Al2O3","Fe2O3","MgO","CaO","Na2O","K2O","(CIW)","(CPA)","(CIA)","(PIA)","(CIX)","(ICV)","(WIP)"]
        data_ox_px=data[ox_px]            
        
        if st.checkbox('Boxplot'):
            st.subheader('Boxplot')
            type = st.radio('Categorization', ['Category','Subcategory','Subsubcategory'])
            if type=='Category':
                color=data_ox_px['category']
            elif type=='Subcategory':
                color=data_ox_px['subcategory']
            else:
                color=data_ox_px['subsubcategory']

            x = st.selectbox('Select the x-axis',(list(data_ox_px)))
            y = st.selectbox('Select the y-axis',(list(data_ox_px)))
            box(x,y,color)

        # scatter matrix of oxides
        if st.checkbox('Scatter matrix of oxides'):
            st.subheader('Scatter matrix of oxides')
            scatter_ox = px.scatter_matrix(data_ox_px, dimensions=["SiO2","TiO2","Al2O3","Fe2O3","MgO","CaO","Na2O","K2O"], hover_name="sample")
            st.plotly_chart(scatter_ox, use_container_width=True)
        
        # scatter matrix of weathering indices
        if st.checkbox('Scatter matrix of weathering indices'):
            st.subheader('Scatter matrix of weathering indices')
            scatter_px = px.scatter_matrix(data_ox_px, dimensions=["(CIW)", "(CPA)", "(CIA)", "(PIA)", "(CIX)", "(ICV)", "(WIP)"], hover_name="sample")
            st.plotly_chart(scatter_px, use_container_width=True)

        # correlation matrix
        if st.checkbox('Correlation matrix'):
            st.subheader('Correlation matrix')

            # Method of correlation
            method = st.radio('Choose the method of correlation', ['Pearson', 'Kendall','Spearman'])
            if method=='Pearson':
                method='pearson'
            elif method=='Kendall':
                method='kendall'
            else:
                method='spearman'

            corrMatrix = round(data_ox_px.corr(method=method), 4)
            st.write(corrMatrix, use_container_width=True)

            @st.cache
            def convert_df(corrMatrix):
                return corrMatrix.to_csv(index=False).encode('utf-8')
            corrMatrix = convert_df(corrMatrix)
            st.download_button("Press to download",corrMatrix,"corrMatrix.csv","csv",key='download-corrMatrix-csv')

            # heatmap
            if st.checkbox('Heatmap of correlation matrix'):
                st.subheader('Heatmap of correlation matrix')
                fig, ax = plt.subplots()
                sns.heatmap(data_ox_px.corr(method=method), ax=ax)
                st.write(fig)
             ##############################################################################################################


##############################################################################################################
# Sidebar Navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select a page:',['Home', 'Data Analysis'])

if options == 'Home':
    home()
elif options == 'Data Analysis':
    data_analysis()

st.sidebar.write("For source code, check out my [github](https://github.com/vinthegreat84/geochemistry/tree/master/cws)", unsafe_allow_html=True)
st.sidebar.write("If you want to get in touch, you can find me on [linkedin](https://www.linkedin.com/in/vinay-babu-81791015/)", unsafe_allow_html=True)    
##############################################################################################################
        