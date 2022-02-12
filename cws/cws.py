import streamlit as st
from streamlit.components.v1 import iframe
st.set_page_config(layout="wide", page_title='CWS 0.1.0')

import pandas as pd
import numpy as np
from numpy import *
from sklearn.linear_model import LinearRegression

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
# from plotly import tools
# import plotly.io as pio
# from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
# import plotly.figure_factory as ff
# import seaborn as sns
# import matplotlib.pyplot as plt
# import altair as alt
import io
# from io import BytesIO
# import os
# from fpdf import FPDF
# import base64
# from base64 import b64encode
# from PIL import Image 
# import PIL
# import os

# if not os.path.exists("images"):
#     os.mkdir("images")
    


# layout
    # Section - home
    # Section - flowchart

# to do
# normalized multielement diagram
# histogram and to check the distribution type
# bivariate of ratios
# user identified variables
# Discrimination diagram
##############################################################################################################
# home
def home():
    st.title('CWS 0.1.0')
    st.subheader('App to analyze major elemental geochemical data of clastic sediments')
    st.caption('Check the sidebar options (top-left arrow to be clicked, if not visible)')
    st.subheader('Created by Vinay Babu')
    st.write('''CWS is a tool designed using Python and Streamlit to analyze major elemental geochemistry of clastic sediments.''')
    st.write('One may navigate to different options on the sidebar menu.')
    st.write('\n')
    st.write('### Sections')
    st.write('**Data panel:** Selection of the major elemental geochemical dataset.')
    st.write('**Data filter:** Data filter based on sample/category/subcategory/subsubcategory.')
    st.write('**Major Oxides variation**: Variation of major oxides against samples.')
    st.write('**Weathering proxy:** Data table of chemical weathering indices including Chemical Index of Weathering (CIW) after [**Harnois, 1988**](https://doi.org/10.1016/0037-0738(88)90137-6); Chemical Index of Weathering without CaO (CIW*) after [**Cullers, 2000**](https://doi.org/10.1016/S0024-4937(99)00063-8); Chemical Proxy of Alteration (CPA) after [**Buggle et al., 2011**](https://doi.org/10.1016/j.quaint.2010.07.019); Chemical Index of Alteration (CIA) after [**Nesbitt and Young, 1982**](https://doi.org/10.1038/299715a0); Plagioclase Index of Alteration (PIA) after [**Fedo et al., 1995**](https://doi.org/10.1130/0091-7613(1995)023<0921:UTEOPM>2.3.CO;2); Modified Chemical Index of Alteration (CIX) after [**Garzanti et al., 2014**](https://doi.org/10.1016/j.chemgeo.2013.12.016); Index of Compositional Variability (ICV) after [**Cox et al., 1995**](https://doi.org/10.1016/0016-7037(95)00185-9); Weathering Index of Parker (WIP) after [**Parker, 1970**](https://doi.org/10.1017/S0016756800058581) and chemical proxies like SiO2/Al2O3, K2O/Al2O3, K2O/Na2O, Al2O3/TiO2.')
    st.write('**Bivariate plot:** Bivariate plot between oxide and/or weathering proxy with variable-based marker size, linear/non-linear trendline & axes, and marginal distribution.')
    st.write('**Trivariate plot:** Trivariate plot between oxide and/or weathering proxy with variable-based marker size and linear/non-linear trendline & axes.')
    st.write('**Ternary plot:** Ternary plot between oxide and/or weathering proxy.')    
    st.write('**Compositional space diagram:** Compositional space diagrams including A - CN - K compositional space diagram after [**Nesbitt and Young, 1982**](https://doi.org/10.1038/299715a0); A - CNK - FM compositional space diagram after [**Nesbitt and Young, 1989**](https://doi.org/10.1086/629290) and M - F - W compositional space diagram after [**Ohta and Arai, 2007**](https://doi.org/10.1016/j.chemgeo.2007.02.017).')
    st.write('**Chemical classification** Chemical classification including ternary plot of SiO2/20, K2O + Na2O, and TiO2 + MgO + Fe2O3 after [**Kroonenberg, 1990**](https://doi.org/10.1016/0009-2541(90)90172-4) and binary plot of log(Fe2O3/K2O) - log(SiO2/Al2O3) after [**Herron, 1988**](https://doi.org/10.1306/212F8E77-2B24-11D7-8648000102C1865D).')
    st.write('**Harker diagram** Harker variation diagram of oxides against SiO2.')    
    st.write('**Sunburst plot, Statistical details, Histogram, Boxplot, Scatter matrix, Correlation matrix and Heatmap:** Sunburst plot, Statistical details, Histogram, Boxplot, Scatter matrix, Correlation matrix and Heatmap of chemical weathering indices and weathering proxies.')        
##############################################################################################################

##############################################################################################################
# Dataset
def data_analysis():
    st.header('Data panel')
    # major elemental data template
    url = 'https://raw.githubusercontent.com/vinthegreat84/geochemistry/master/template.csv'
    df = pd.read_csv(url)
#     df = pd.read_csv("C:/Users/Hp/CWS/data/template.csv")

    @st.cache
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')

    template = convert_df(df)
    st.download_button("Press to download a csv data template to analyze your data", template, "template.csv", "csv", key='download-template-csv')
    
    st.write('\n')
    
    data = st.sidebar.selectbox('Select Dataset',('Example data', 'User data'))

    st.write(data)
    
    def get_data(name):
        data = None
        if name == 'Example data':
            url = 'https://raw.githubusercontent.com/vinthegreat84/geochemistry/master/SedWeather/raw/sedchem.csv'
            df = pd.read_csv(url)
#             df = pd.read_csv("C:/Users/Hp/CWS/data/sedchem.csv")
        else:
            uploaded_file = st.file_uploader("Choose a CSV file (max 200 MB)")
#             col_list =["sample","category","subcategory","subsubcategory","reference","SiO2","TiO2","Al2O3","Fe2O3","FeO","MnO","MgO","CaO","Na2O","K2O","P2O5","CO2"]
#             df = pd.read_csv(uploaded_file, usecols=col_list)
            df = pd.read_csv(uploaded_file)
        return df

    data = get_data(data)

    st.write(data)

    @st.cache
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')
    sample = convert_df(df)
    st.download_button("Press to download",sample,"sample.csv","csv",key='download-sample-csv')
    
    def plot_html(plot):
        buffer = io.StringIO()
        plot.write_html(buffer, include_plotlyjs='cdn')
        html_bytes = buffer.getvalue().encode()
                
        st.download_button(
        label='Download HTML',
        data=html_bytes,
        file_name='plot.html',
        mime='text/html'
                )
    
#     def get_image_download_link(img,filename,text):
#         buffered = BytesIO()
#         img.save(buffered, format="JPEG")
#         img_str = base64.b64encode(buffered.getvalue()).decode()
#         href =  f'<a href="data:file/txt;base64,{img_str}" download="{filename}">{text}</a>'
#         return href
    
    #     def plot_svg(plot):
#         buffer = io.StringIO()
#         plot.write_html(buffer, include_plotlyjs='cdn')
#         html_bytes = buffer.getvalue().encode()
        
#         st.download_button(
#         label='Download',
#         data=html_bytes,
#         file_name='plot.svg',
#         mime='image/svg'
#                 )  

    # data filter     
    if st.sidebar.checkbox('Data filter'):
        filter = st.sidebar.expander('filter', False)        
        # selection of country from 'location'
        filter = filter.radio('Select the data filter:',['sample', 'category', 'subcategory','subsubcategory'])
        if filter=='sample':
            sample = st.sidebar.multiselect("Select the Samples of the data filter:", data['sample'].unique(), default=data['sample'].iloc[0])
            data_sample = data[data['sample'].isin(sample)]
            data = data_sample   
        if filter=='category':
            cat = st.sidebar.selectbox("Select the Catgory of the data filter:", data['category'].unique())
            data_cat = data[data['category'].isin([cat])]
            data = data_cat
        if filter=='subcategory':
            subcat = st.sidebar.selectbox("Select the Subcatgory of the data filter:", data['subcategory'].unique())
            data_subcat = data[data['subcategory'].isin([subcat])]
            data = data_subcat
        if filter=='subsubcategory':
            subsubcat = st.sidebar.selectbox("Select the Subsubcatgory of the data filter:", data['subsubcategory'].unique())
            data_subsubcat = data[data['subsubcategory'].isin([subsubcat])]
            data = data_subsubcat
    
    # Major oxides
    if st.sidebar.checkbox('Major oxides'):
        st.header('Major oxides')
        data_var = data
        st.write(data_var)
        
        #Major oxides variation
        if st.sidebar.checkbox('Major oxides variation'):
            st.header('Major oxides variation')

            var = px.line(data_var, x='sample', y=['SiO2','TiO2','Al2O3','Fe2O3','FeO','MnO','MgO','CaO','Na2O','K2O','P2O5','CO2'])
            var.update_layout(yaxis_title="Major oxide %",
                              legend_title="Major oxide")
            st.plotly_chart(var, use_container_width=True)

            # exporting the plot to the local machine
            with st.expander("Click to export Major oxides variation diagram"):
                plot_html(var)     
    
#         var = alt.Chart(data_var).transform_fold(
#             ['SiO2','TiO2','Al2O3','Fe2O3','FeO','MnO','MgO','CaO','Na2O','K2O','P2O5','CO2'],
#         ).mark_line().encode(
#             x=alt.X('sample:N', axis=alt.Axis(title='Sample'), sort=None),
#             y=alt.Y('value:Q', axis=alt.Axis(title='Variation %')),
#             tooltip=['sample','category','subcategory','subsubcategory','reference'],
#             color=alt.Color('key:N', legend=alt.Legend(title="Oxide"))
#         ).interactive().properties(width='container')        
#         st.altair_chart(var, use_container_width=True)

#         if st.sidebar.checkbox('Normalization'):
#             st.header('Normalization variation diagram')
#             data_norm = data
#             norm = st.sidebar.selectbox("Select the Sample:", data_norm['sample'].unique())
#             norm = data_norm[data_norm['sample'].isin([norm])]
# # #             norm = data_norm[data_norm['sample'].isin([norm])].drop(["sample","category","subcategory","subsubcategory","reference"], axis=1)
#             st.write(norm)
# #             data_norm.loc["SiO2":].div(norm.loc["SiO2":], axis='columns')
#             data_norm=data_norm.div(norm.loc["SiO2":])
# #             data_norm = data_norm.loc["SiO2":].div(norm.loc["SiO2":], axis=1)
# #             data_norm = data_norm.loc[:,"SiO2":].div(norm.loc[0]["SiO2":])
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

    # Chemical Index of Weathering (CIW') after Cullers, 2000
    data['(CIW*)'] = data['molar_Al2O3'] / (data['molar_Al2O3'] + data['molar_Na2O'])    

    # Chemical Proxy of Alteration (CPA) after Buggle et al., 2011  
    data['(CPA)'] = 100 * data['molar_Al2O3'] / (data['molar_Al2O3'] + data['molar_Na2O']) 

    # Chemical Index of Alteration (CIA) after Nesbitt and Young, 1982
    data['(CIA)'] = 100 * data['molar_Al2O3'] / (data['molar_Al2O3'] + data['molar_CaO*'] + data['molar_Na2O'] + data['molar_K2O']) 

    # Plagioclase Index of Alteration (PIA) after Fedo et al., 1995
    data['(PIA)'] = 100 * (data['molar_Al2O3'] - data['molar_K2O']) / (data['molar_Al2O3'] + data['molar_CaO*'] + data['molar_Na2O'] - data['molar_K2O'])

    # Modified Chemical Index of Alteration (CIX) after Garzanti et al., 2014                                                          
    data['(CIX)'] = 100 * data['molar_Al2O3'] / (data['molar_Al2O3'] + data['molar_Na2O'] + data['molar_K2O']) 

    # Index of Compositional Variability (ICV) after Cox et al., 1995
    data['(ICV)'] = (data['Fe2O3'] + data['K2O'] + data['Na2O'] + data['CaO'] + data['MgO'] + data['MnO'] + data['TiO2']) / data['Al2O3']

    # Weathering Index of Parker (WIP) after Parker, 1970
    data['(WIP)'] = 100 * (2*data['molar_Na2O']/0.35 + data['molar_MgO']/0.9 + 2*data['molar_K2O']/0.25 + data['molar_CaO*']/0.7)
    
    # ratios
    data['SiO2/Al2O3'] = data['SiO2'] / data['Al2O3']
    data['K2O/Al2O3']  = data['K2O'] / data['Al2O3']
    data['K2O/Na2O']  = data['K2O'] / data['Na2O']    
    data['Al2O3/TiO2'] = data['Al2O3'] / data['TiO2']
        
    if st.sidebar.checkbox('Weathering proxy'):
        st.header('Weathering proxy')
        proxy =["sample","category","subcategory","subsubcategory","reference","(CIW)","(CIW*)","(CPA)","(CIA)","(PIA)","(CIX)","(ICV)","(WIP)","SiO2/Al2O3","K2O/Al2O3","K2O/Na2O","Al2O3/TiO2"]
        proxy=data[proxy]
        st.write(proxy)
        
        proxy_download=proxy
        @st.cache
        def convert_df(proxy_download):
            return proxy_download.to_csv(index=False).encode('utf-8')
        proxy_download = convert_df(proxy_download)
        st.download_button("Press to download",proxy_download,"proxy.csv","csv",key='download-proxy-csv')

        # weathering proxy variation
        if st.sidebar.checkbox('Weathering proxy variation'):
            st.header('Weathering proxy variation')

            var_proxy = px.line(proxy, x='sample', y=['(CIW)','(CIW*)','(CPA)','(CIA)','(PIA)','(CIX)','(ICV)','(WIP)','SiO2/Al2O3','K2O/Al2O3','K2O/Na2O','Al2O3/TiO2'])
            var_proxy.update_layout(yaxis_title="Weathering proxy",
                              legend_title="Weathering proxy")
            st.plotly_chart(var_proxy, use_container_width=True)

            # exporting the plot to the local machine
            with st.expander("Click to export Weathering proxy variation diagram"):
                plot_html(var_proxy) 
    
    # bivariate plot
    if st.sidebar.checkbox('Bivariate plot'):
        st.header('Bivariate plot')
        data_bivar = data.drop(["molar_SiO2","molar_TiO2","molar_Al2O3","molar_Fe2O3","molar_MnO","molar_MgO","molar_CaO","molar_Na2O","molar_K2O","molar_P2O5","molar_CO2","diff","molar_CaO*"], axis=1)
        hover_name="sample"
        color="subcategory"
        symbol="subsubcategory"
        size = trendline = marginal_x = marginal_y = facet_col = facet_col_wrap = None

        # subplot     
        if st.sidebar.checkbox('Subplot'):        
            # selection of subplot
            sub = st.sidebar.expander('Subplot', False)            
            sub = sub.radio('Select the Subplot of bivariate plot:',['category', 'subcategory','subsubcategory'])  
            if sub=='category':
                facet_col='category'
            if sub=='subcategory':
                facet_col='subcategory'
            if sub=='subsubcategory':
                facet_col='subsubcategory'            

            # subplot wrap     
            if st.sidebar.checkbox('Subplot wrap of bivariate plot'):

                # wrapping of subplot
                facet_col_wrap = st.sidebar.number_input('Set the Subplot wrap of bivariate plot:', min_value=1, value=1, step=1)
                facet_col_wrap = int(facet_col_wrap)
        
        if st.sidebar.checkbox('Trendline'):
            data_bivar = data_bivar.drop(["sample","category","subcategory","subsubcategory","reference"], axis=1)
            hover_name = color = symbol = facet_col = facet_col_wrap = None
            trendline_type = st.sidebar.expander('Trendline type', False)              
            trendline_type = trendline_type.radio('Trendline:',['Linear', 'Non-Linear'])
            if trendline_type=='Linear':
                trendline="ols"
            else:
                trendline="lowess"    
        
        if st.sidebar.checkbox('Variable-based marker size of bivariate plot'):
            size = st.sidebar.expander('oxide/weathering index/ratio', False)              
            size = size.radio('Select the oxide/weathering index/ratio of bivariate plot:',['oxide', 'weathering index', 'ratio'])
            if size=='oxide':
                col_first="SiO2"
                col_last="P2O5"
            if size=='weathering index':
                col_first="(CIW)"
                col_last="(WIP)"            
            if size=='ratio':
                col_first="SiO2/Al2O3"
                col_last="Al2O3/TiO2"
            size = st.sidebar.selectbox('Select the oxide/weathering index/ratio of bivariate plot:',list(data_bivar.loc[:,col_first:col_last]))
            
        if st.sidebar.checkbox('Add marginal distribution of bivariate plot'):
            if st.sidebar.checkbox('X-axis marginal distribution of bivariate plot'):
                type = st.sidebar.expander('X-axis marginal distribution', False)                
                type = type.radio('Select the X-axis marginal distribution of bivariate plot:',['histogram','rug','box','violin'])
                if type=='histogram':
                    marginal_x='histogram'
                if type=='rug':
                    marginal_x='rug'
                if type=='box':
                    marginal_x='box'
                if type=='violin':
                    marginal_x='violin'
            if st.sidebar.checkbox('Y-axis marginal distribution of bivariate plot'):
                type = st.sidebar.expander('Y-axis marginal distribution', False)                 
                type = type.radio('Select the Y-axis marginal distribution of bivariate plot:',['histogram','rug','box','violin'])
                if type=='histogram':
                    marginal_y='histogram'
                if type=='rug':
                    marginal_y='rug'
                if type=='box':
                    marginal_y='box'
                if type=='violin':
                    marginal_y='violin'
                    
        x = st.sidebar.selectbox('Select the x-axis of bivariate plot',list(data_bivar))         
        xaxis_type = st.sidebar.expander('X-axis type', False)           
        xaxis_type = xaxis_type.radio('x axis type of bivariate plot:',['Linear', 'Logarithmic'])
        if xaxis_type=='Linear':
            log_x=False
        else:
            log_x=True
            marginal_x=None
        
        y = st.sidebar.selectbox('Select the y-axis of bivariate plot',list(data_bivar))        
        yaxis_type = st.sidebar.expander('Y-axis type', False)         
        yaxis_type = yaxis_type.radio('y axis type of bivariate plot:',['Linear', 'Logarithmic'])
        if yaxis_type=='Linear':
            log_y=False
        else:
            log_y=True 
            marginal_y=None
            
        bivar = px.scatter(data_bivar, x=x, y=y, log_x=log_x, log_y=log_y, hover_name=hover_name, color=color, symbol=symbol, size=size, trendline=trendline, marginal_x=marginal_x, marginal_y=marginal_y, facet_col=facet_col, facet_col_wrap=facet_col_wrap, render_mode="webgl", title="Bivariate Plot", color_discrete_sequence=px.colors.qualitative.Antique)        
        st.plotly_chart(bivar, use_container_width=True)
        
        # exporting the plot to the local machine
        with st.expander("Click to export bivariate plot"):
#             if st.button("bivariate plot as PNG"):
#                 bivar.write_image("images/bivar.png")
#             if st.button("bivariate plotas JPEG"):
#                 bivar.write_image("bivar.JPEG")
#                 img_file = "plot.jpg"
#                 st.markdown(get_image_download_link(bivar,img_file,'Download '+img_file), unsafe_allow_html=True)

#             if st.button("bivariate plot as WebP"):
#                 bivar.write_image("bivar.webp")
#             if st.button("bivariate plot as SVG"):
#                 bivar.write_image("bivar.svg")
#             if st.button("bivariate plot as PDF"):
#                 bivar.write_image("bivar.pdf")
            if st.button("bivariate plot as HTML"):
                plot_html(bivar)
    
    # 3d/trivariate plot
    if st.sidebar.checkbox('Trivariate plot'):
        st.header('Trivariate plot')
        data_trivar = data.drop(["molar_SiO2","molar_TiO2","molar_Al2O3","molar_Fe2O3","molar_MnO","molar_MgO","molar_CaO","molar_Na2O","molar_K2O","molar_P2O5","molar_CO2","diff","molar_CaO*"], axis=1)
        hover_name="sample"
        color="subcategory"
        symbol="subsubcategory"
        size = trendline = marginal_x = marginal_y = marginal_z = None  
                
        if st.sidebar.checkbox('Variable-based marker size of trivariate plot'):
            size = st.sidebar.expander('oxide/weathering index/ratio', False)            
            size = size.radio('Select the oxide/weathering index/ratio of trivariate plot:',['oxide', 'weathering index', 'ratio'])
            if size=='oxide':
                col_first="SiO2"
                col_last="P2O5"
            if size=='weathering index':
                col_first="(CIW)"
                col_last="(WIP)"            
            if size=='ratio':
                col_first="SiO2/Al2O3"
                col_last="Al2O3/TiO2"
            size = st.sidebar.selectbox('Select the oxide/weathering index/ratio of trivariate plot',list(data_trivar.loc[:,col_first:col_last]))                             
                    
        x = st.sidebar.selectbox('Select the x-axis of trivariate plot',list(data_trivar))
        xaxis_type = st.sidebar.expander('X-axis type', False)         
        xaxis_type = xaxis_type.radio('x axis type of trivariate plot:',['Linear', 'Logarithmic'])
        if xaxis_type=='Linear':
            log_x=False
        else:
            log_x=True
            marginal_x=None
        
        y = st.sidebar.selectbox('Select the y-axis of trivariate plot',list(data_trivar))
        yaxis_type = st.sidebar.expander('Y-axis type', False) 
        yaxis_type = yaxis_type.radio('y axis type of trivariate plot:',['Linear', 'Logarithmic'])
        if yaxis_type=='Linear':
            log_y=False
        else:
            log_y=True 
            marginal_y=None

        z = st.sidebar.selectbox('Select the z-axis of trivariate plot',list(data_trivar))
        zaxis_type = st.sidebar.expander('Z-axis type', False)        
        zaxis_type = zaxis_type.radio('z axis type of trivariate plot:',['Linear', 'Logarithmic'])
        if zaxis_type=='Linear':
            log_z=False
        else:
            log_z=True 
            marginal_z=None            
            
        trivar = px.scatter_3d(data_trivar, x=x, y=y, z=z, log_x=log_x, log_y=log_y, log_z=log_z, hover_name=hover_name, color=color, symbol=symbol, size=size, title="Trivariate Plot", color_discrete_sequence=px.colors.qualitative.Antique)        
        st.plotly_chart(trivar, use_container_width=True)        
        
    # Ternary plot
    def tern(a,b,c,color,symbol,hover_name):
        tern_plot = px.scatter_ternary(data, a=a, b=b, c=c, color=color, symbol=symbol, hover_name=hover_name, color_discrete_sequence=px.colors.qualitative.Antique)
        
        tern_plot.update_layout({'ternary': {'sum': 100}})
        tern_plot.update_ternaries(bgcolor='yellow')
        tern_plot.update_traces(marker=dict(size=12, line=dict(width=2, color='DarkSlateGrey')), selector=dict(mode='markers'))
        
        tern_plot.update_layout({
            'ternary':
                {
                'sum':100,
                'aaxis':{'title': title_a},
                'baxis':{'title': title_b},
                'caxis':{'title': title_c}
                }
        })
        st.plotly_chart(tern_plot, use_container_width=True)
        return tern_plot
    
    # Ternary plot
    if st.sidebar.checkbox('Ternary plot'):
        st.header('Ternary plot')
        data_ter=data.drop(["diff"], axis=1)
        st.write(data_ter)
        
        hover_name=data_ter['sample']
        category = st.sidebar.expander('Categorization', False)         
        category = category.radio('Categorization of Ternary plot', ['Category','Subcategory'])
        if category=='Category':
            color=data_ter['category']
            symbol=None
        else:
            color=data_ter['subcategory']
            symbol=data_ter['subsubcategory']        
        
        axis = st.sidebar.expander('Axes', False)
        a = axis.selectbox('Select the component A of Ternary plot', list(data_ter))        
        b = axis.selectbox('Select the component B of Ternary plot', list(data_ter))   
        c = axis.selectbox('Select the component C of Ternary plot', list(data_ter))           

        title_a, title_b, title_c = a, b, c
        fig = tern(a,b,c,color,symbol,hover_name) 
            
    # Compositional space diagram selection
    if st.sidebar.checkbox('Compositional space diagram'):
        st.header('Compositional space diagram')
        csd =["sample","category","subcategory","subsubcategory","reference","SiO2","TiO2","Al2O3","Fe2O3","MgO","CaO","Na2O","K2O","molar_Al2O3","molar_CaO*","molar_Na2O","molar_K2O","molar_Fe2O3","molar_MgO"]
        data_csd=data[csd]
        hover_name=data_csd['sample']        
        category = st.sidebar.expander('Categorization', False)          
        category = category.radio('Categorization of Compositional space diagram', ['Category','Subcategory'])
        if category=='Category':
            color=data_csd['category']
            symbol=None
        else:
            color=data_csd['subcategory']
            symbol=data_csd['subsubcategory']        
        csd_type = st.sidebar.expander('Compositional space diagram', False)         
        csd_type = csd_type.radio('Compositional space diagram:',['A - CN - K', 'A - CNK - FM', 'M - F - W'])
        a=data_csd['molar_Al2O3']
        if csd_type == 'A - CN - K':
            b=data_csd['molar_CaO*'] + data_csd['molar_Na2O']            
            c=data_csd['molar_K2O']
            title_a = 'Al<sub>2</sub>O<sub>3</sub>'
            title_b = 'CaO*+Na<sub>2</sub>O'
            title_c = 'K<sub>2</sub>O'
        elif csd_type == 'A - CNK - FM':
            b=data_csd['molar_CaO*'] + data_csd['molar_Na2O'] + data_csd['molar_K2O']           
            c=data_csd['molar_Fe2O3'] + data_csd['molar_MgO']
            title_a = 'Al<sub>2</sub>O<sub>3</sub>'
            title_b = 'CaO*+Na<sub>2</sub>O+K<sub>2</sub>O'
            title_c = 'Fe<sub>2</sub>O<sub>3</sub>+MgO'
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

            a=data_csd['(M)']
            b=data_csd['(F)']            
            c=data_csd['(W)']
            title_a = 'M'
            title_b = 'F'
            title_c = 'W'
            
        fig = tern(a,b,c,color,symbol,hover_name)      

        # exporting the plot to the local machine
        with st.expander("Click to export compositional space diagram"):
            if st.button("compositional space diagram as HTML"):
                plot_html(fig)

    # Chemical classification selection
    # Ternary plot of SiO2/20, K2O + Na2O, and TiO2 + MgO + Fe2O3 after Kroonenberg, 1990
    # Binary plot of log(Fe2O3/K2O) - log(SiO2/Al2O3) after Herron, 1988             
    # overlays from Rollinson, 2021
    if st.sidebar.checkbox('Chemical classification'):
        st.header('Chemical classification')
        classfication = ['sample','category','subcategory','subsubcategory','reference','SiO2','TiO2','Al2O3','Fe2O3','FeO','MnO','MgO','CaO','Na2O','K2O','P2O5']
        data_class = data[classfication]
        hover_name=data_class['sample']        
        
        # color palette
        col = ['darkorchid','darkred','darksalmon','darkseagreen','darkslateblue','darkslategray','darkslategrey,darkturquoise','darkviolet','deeppink','deepskyblue','dimgray','dimgrey','dodgerblue','firebrick','floralwhite','forestgreen','fuchsia','gainsboro','ghostwhite','gold','goldenrod','gray','grey','green','greenyellow','honeydew','hotpink','indianred','indigo','ivory','khaki','lavender','lavenderblush','lawngreen','lemonchiffon','lightblue','lightcoral','lightcyan','lightgoldenrodyellow','lightgray','lightgrey','lightgreen','lightpink','lightsalmon','lightseagreen','lightskyblue','lightslategray','lightslategrey','lightsteelblue','lightyellow','lime','limegreen','linen','magenta','maroon','mediumaquamarine','mediumblue','mediumorchid','mediumpurple','mediumseagreen','mediumslateblue','mediumspringgreen','mediumturquoise','mediumvioletred','midnightblue','mintcream','mistyrose','moccasin','navajowhite','navy,oldlace','olive','olivedrab','orange','orangered','orchid','palegoldenrod','palegreen','paleturquoise','palevioletred','papayawhip','peachpuff','peru','pink','plum','powderblue','purple','red','rosybrown','royalblue','saddlebrown','salmon','sandybrown','seagreen','seashell','sienna','silver','skyblue','slateblue','slategray','slategrey','snow','springgreen','steelblue','tan','teal','thistle','tomato','turquoise','violet','wheat','white','whitesmoke','yellow','yellowgreen']
        
        text_col = ['Gainsboro', 'LightGray', 'Silver', 'DarkGray', 'Gray', 'DimGray', 'LightSlateGray', 'SlateGray', 'DarkSlateGray', 'Black']
        
        # line style
        dash = ['solid', 'dot', 'dash', 'longdash', 'dashdot', 'longdashdot']
        
        # Opacity
        opacity = 1 # default
        
        # selection of classification diagram
        class_type = st.sidebar.radio('Classification diagram:',['SiO2/20 - K2O+Na2O - TiO2+MgO+Fe2O3', 'log(Fe2O3/K2O) - log(SiO2/Al2O3)'])

        if class_type == 'SiO2/20 - K2O+Na2O - TiO2+MgO+Fe2O3':
            marker_size = 12
            marker_line_col = marker_line_width = None
            category = st.sidebar.expander('Categorization', False)
            category = category.radio('Categorization of Compositional space diagram',['Category','Subcategory'])
            if category=='Category':
                color=data_class['category']
                symbol=None
            else:
                color=data_class['subcategory']
                symbol=data_class['subsubcategory']            

            if st.sidebar.checkbox('Marker attributes'):
                marker_size = st.sidebar.expander('Size of marker', False)                
                marker_size = marker_size.number_input('Set the Size of marker of SiO2/20 - K2O+Na2O - TiO2+MgO+Fe2O3:', min_value=1, value=12, step=1)
                marker_size = int(marker_size)                
                marker_line_col = st.sidebar.expander('Line color of marker', False) 
                marker_line_col = marker_line_col.selectbox('Select the Line color of marker of SiO2/20 - K2O+Na2O - TiO2+MgO+Fe2O3', col)
                marker_line_width = st.sidebar.expander('Line width of marker', False)                 
                marker_line_width = marker_line_width.number_input('Set the Line width of marker of SiO2/20 - K2O+Na2O - TiO2+MgO+Fe2O3:', min_value=1, value=1, step=1)
                opacity = st.sidebar.expander('Opacity of marker', False)                
                opacity = opacity.number_input('Set the Opacity of marker of SiO2/20 - K2O+Na2O - TiO2+MgO+Fe2O3:', min_value=0.1, max_value=1.0, value=0.5, step=0.1)                 

            fig = px.scatter_ternary(data_class, a=data_class['SiO2']/20, b=data_class['TiO2'] + data_class['MgO'] + data_class['Fe2O3'], c=data_class['K2O'] + data_class['Na2O'], opacity=opacity, color=color, symbol=symbol, hover_name=hover_name, color_discrete_sequence=px.colors.qualitative.Antique)

            line_color = 'gray'
            line_width = 10
            opacity = 0.5
            if st.sidebar.checkbox('Overlay attributes'):
                line_color = st.sidebar.expander('Line color of overlay', False) 
                line_color = line_color.selectbox('Select the Line color of overlay of SiO2/20 - K2O+Na2O - TiO2+MgO+Fe2O3', col)            
                line_width = st.sidebar.expander('Line width of overlay', False)                 
                line_width = line_width.number_input('Set the Line width of overlay of SiO2/20 - K2O+Na2O - TiO2+MgO+Fe2O3:', min_value=1, value=1, step=1)                   
                opacity = st.sidebar.expander('Opacity of overlay', False)                
                opacity = opacity.number_input('Set the Opacity of overlay of SiO2/20 - K2O+Na2O - TiO2+MgO+Fe2O3:', min_value=0.1, max_value=1.0, value=0.5, step=0.1)  
            fig.add_scatterternary(a=[10], b=[80], mode='text', text='immature', opacity=opacity, showlegend=False)
            fig.add_scatterternary(a=[80], b=[14], mode='text', text='mature', opacity=opacity, showlegend=False)                
            fig.add_scatterternary(a=[89,37,26,19,13,8,7,5], b=[4,23,29,34,40,48,55,80], mode='lines', marker=dict(color=line_color),line=dict(width=line_width), opacity=opacity, showlegend=False)

            fig.update_layout({'ternary': {'sum': 100}})
            fig.update_ternaries(bgcolor='yellow')
            fig.update_traces(marker=dict(size=marker_size, line=dict(width=marker_line_width, color=marker_line_col)), selector=dict(mode='markers'))                

            fig.update_layout({
                'ternary':
                    {
                    'sum':100,
                    'aaxis':{'title': 'SiO<sub>2</sub>/20'},
                    'baxis':{'title': 'TiO<sub>2</sub> + MgO + Fe<sub>2</sub>O<sub>3</sub>'},             
                    'caxis':{'title': 'K<sub>2</sub>O + Na<sub>2</sub>O'}
                    }
            })                 

        if class_type == 'log(Fe2O3/K2O) - log(SiO2/Al2O3)':
            marker_color = color = width = None
            size = 12
            symbol = 0

            if st.sidebar.checkbox('Marker attributes'):
                marker = st.sidebar.expander('Symbol', False)
                symbol = marker.number_input('Set the Symbol of marker of log(Fe2O3/K2O) - log(SiO2/Al2O3):', min_value=0, max_value=24, value=0, step=1)
                symbol = int(symbol)                
                if st.sidebar.checkbox('Symbol variant'):
                    variant = st.sidebar.expander('Symbol variant', False)
                    variant = variant.radio('Select a variant:',['open', 'dot', 'open-dot'])
                    if variant=='open':
                        symbol = symbol+100
                    if variant=='dot':
                        symbol = symbol+200
                    if variant=='open-dot':
                        symbol = symbol+300                
                marker_color = st.sidebar.expander('Color of marker', False)
                marker_color = marker_color.selectbox('Select the Color of marker of log(Fe2O3/K2O) - log(SiO2/Al2O3)', col)
                size = st.sidebar.expander('Size of marker', False)
                size = size.number_input('Set the Size of marker of log(Fe2O3/K2O) - log(SiO2/Al2O3):', min_value=1, value=12, step=1)
                size = int(size)                
                color = st.sidebar.expander('Line color of marker', False)
                color = color.selectbox('Select the Line color of marker of log(Fe2O3/K2O) - log(SiO2/Al2O3)', col)
                width = st.sidebar.expander('Line width of marker', False)                
                width = width.number_input('Set the Line width of marker of log(Fe2O3/K2O) - log(SiO2/Al2O3):', min_value=1, value=2, step=1)
                width = int(width)
                opacity = st.sidebar.expander('Opacity of marker', False)                  
                opacity = opacity.number_input('Set the Opacity of marker of log(Fe2O3/K2O) - log(SiO2/Al2O3):', min_value=0.1, max_value=1.0, value=0.5, step=0.1)                 

            x = np.log(data_class['SiO2']/data_class['Al2O3'])
            y = np.log(data_class['Fe2O3']/data_class['K2O'])                

            fig = go.Figure()

            fig.add_trace(go.Scatter(x=x, y=y, opacity=opacity, marker_symbol=symbol, mode='markers', marker=dict(color=marker_color, size=size, opacity=opacity, line=dict(color=color,width=width))))

            color = width = None
            if st.sidebar.checkbox('Overlay attributes'):
                color = st.sidebar.expander('Color of overlay', False)                  
                color = color.selectbox('Select the Color of overlay of log(Fe2O3/K2O) - log(SiO2/Al2O3)', col)
                width = st.sidebar.expander('Width of overlay', False)                  
                width = width.number_input('Select the Width of overlay of log(Fe2O3/K2O) - log(SiO2/Al2O3):', min_value=1, value=2, step=1)
                width = int(width)                 
                opacity = st.sidebar.expander('Opacity of overlay', False)                 
                opacity = opacity.number_input('Set the Opacity of overlay of log(Fe2O3/K2O) - log(SiO2/Al2O3):', min_value=0.1, max_value=1.0, value=0.5, step=0.1) 

            # boundaries overlay            
            # boundary between Shale and Fe-shale
            x_overlay = [+0.00, +0.71]
            y_overlay = [+0.60, +0.60]            
            fig.add_trace(go.Scatter(x=x_overlay, y=y_overlay, opacity=opacity, mode='lines', line=dict(color=color, width=width)))            
            # boundary between Fe-shale and Fe-sand
            x_overlay = [+0.71, +0.71]
            y_overlay = [+0.60, +1.50]            
            fig.add_trace(go.Scatter(x=x_overlay, y=y_overlay, opacity=opacity, mode='lines', line=dict(color=color, width=width)))                        
            # boundary between Wacke and Shale
            x_overlay = [+0.55, +0.71]
            y_overlay = [-0.10, +0.60]            
            fig.add_trace(go.Scatter(x=x_overlay, y=y_overlay, opacity=opacity, mode='lines', line=dict(color=color, width=width)))            
            # boundary between Wacke and Fe-sand
            x_overlay = [+0.71, +0.87]
            y_overlay = [+0.60, +0.60]            
            fig.add_trace(go.Scatter(x=x_overlay, y=y_overlay, opacity=opacity, mode='lines', line=dict(color=color, width=width)))            
            # boundary between Litharenite and Fe-sand
            x_overlay = [+0.87, +1.14]
            y_overlay = [+0.60, +0.60]            
            fig.add_trace(go.Scatter(x=x_overlay, y=y_overlay, opacity=opacity, mode='lines', line=dict(color=color, width=width)))            
            # boundary between Sublitharenite and Fe-sand
            x_overlay = [+1.14, +1.70]
            y_overlay = [+0.60, +0.60]            
            fig.add_trace(go.Scatter(x=x_overlay, y=y_overlay, opacity=opacity, mode='lines', line=dict(color=color, width=width)))
            # boundary between Arkose and Wacke
            x_overlay = [+0.64, +0.76]
            y_overlay = [-0.50, +0.00]            
            fig.add_trace(go.Scatter(x=x_overlay, y=y_overlay, opacity=opacity, mode='lines', line=dict(color=color, width=width)))            
            # boundary between Litharenite and Wacke
            x_overlay = [+0.76, +0.87]
            y_overlay = [+0.00, +0.60]            
            fig.add_trace(go.Scatter(x=x_overlay, y=y_overlay, opacity=opacity, mode='lines', line=dict(color=color, width=width)))  
            # boundary between Arkose, Litharenite and Subarkose, Sublitharenite
            x_overlay = [+1.00, +1.14]
            y_overlay = [-1.00, +0.60]            
            fig.add_trace(go.Scatter(x=x_overlay, y=y_overlay, opacity=opacity, mode='lines', line=dict(color=color, width=width))) 
            # boundary between Arkose, Subarkose and Litharenite, Sublitharenite
            x_overlay = [+0.76, +1.68]
            y_overlay = [+0.00, +0.00]            
            fig.add_trace(go.Scatter(x=x_overlay, y=y_overlay, opacity=opacity, mode='lines', line=dict(color=color, width=width)))                          
            # boundary between Subarkose and Quartz arenite 
            x_overlay = [+1.60, +1.68]
            y_overlay = [-1.00, +0.00]            
            fig.add_trace(go.Scatter(x=x_overlay, y=y_overlay, opacity=opacity, mode='lines', line=dict(color=color, width=width)))            
            # boundary between Sublitharenite and Quartz arenite 
            x_overlay = [+1.68, +1.70]
            y_overlay = [+0.00, +0.60]            
            fig.add_trace(go.Scatter(x=x_overlay, y=y_overlay, opacity=opacity, mode='lines', line=dict(color=color, width=width)))                
            # boundary between Fe-sand and Quartz arenite 
            x_overlay = [+1.80, +1.70]
            y_overlay = [+1.50, +0.60]            
            fig.add_trace(go.Scatter(x=x_overlay, y=y_overlay, opacity=opacity, mode='lines', line=dict(color=color, width=width)))

            # text annotation
            size = 16
            color = 'Black'
            opacity = 0.8
            if st.sidebar.checkbox('Text attributes'):
                size = st.sidebar.expander('Size of text', False)                 
                size = size.number_input('Select the Size of text overlay of log(Fe2O3/K2O) - log(SiO2/Al2O3):', min_value=1, value=20, step=1)
                size = int(size) 
                color = st.sidebar.expander('Color of text', False)  
                color = color.selectbox('Select the Color of text overlay of log(Fe2O3/K2O) - log(SiO2/Al2O3)', text_col)                
                opacity = st.sidebar.expander('Opacity of text', False)                  
                opacity = opacity.number_input('Set the Opacity of text overlay of log(Fe2O3/K2O) - log(SiO2/Al2O3):', min_value=0.1, max_value=1.0, value=0.5, step=0.1) 

            # text overlay
            fig.add_annotation(x=0.35, y=1,text="Fe-shale",showarrow=False,font=dict(family="Times New Roman",size=size,color=color),opacity=opacity)
            fig.add_annotation(x=0.35, y=0,text="Shale",showarrow=False,font=dict(family="Times New Roman",size=size,color=color),opacity=opacity)            
            fig.add_annotation(x=1.2, y=1,text="Fe-sand",showarrow=False,font=dict(family="Times New Roman",size=size,color=color),opacity=opacity)
            fig.add_annotation(x=1.4, y=0.25,text="Sublitharenite",showarrow=False,font=dict(family="Times New Roman",size=size,color=color),opacity=opacity)
            fig.add_annotation(x=1.4, y=-0.5,text="Subarkose",showarrow=False,font=dict(family="Times New Roman",size=size,color=color),opacity=opacity)
            fig.add_annotation(x=0.97, y=0.3,text="Litharenite",showarrow=False,font=dict(family="Times New Roman",size=size,color=color),opacity=opacity)
            fig.add_annotation(x=0.9, y=-0.5,text="Arkose",showarrow=False,font=dict(family="Times New Roman",size=size,color=color),opacity=opacity)
            fig.add_annotation(x=0.7, y=0.16,text="Wacke",showarrow=False,font=dict(family="Times New Roman",size=size,color=color),opacity=opacity, xref="x", yref="y", textangle=-35)            
            fig.add_annotation(x=1.9, y=0.5,text="Quartz arenite",showarrow=False,font=dict(family="Times New Roman",size=size,color=color),opacity=opacity)            

            fig.update_layout(yaxis_title="log(Fe<sub>2</sub>O<sub>3</sub>/K<sub>2</sub>O)", xaxis_title="log(SiO<sub>2</sub>/Al<sub>2</sub>O<sub>3</sub>)", showlegend=False)

        st.plotly_chart(fig, use_container_width=True)

        # exporting the plot to the local machine
        with st.expander("Click to export Classification diagram"):
            plot_html(fig)

#         # Discrimination diagram
#         if st.sidebar.checkbox('Discrimination diagram'):
#             st.header('Discrimination diagram')            

#             # line segment intersection using vectors
#             # see Computer Graphics by Hill (2008)
#             def perp (a):
#                 b = empty_like(a)
#                 b[0] = -a[1]
#                 b[1] = a[0]
#                 return b

#             # line segment a given by endpoints a1, a2
#             # line segment b given by endpoints b1, b2
#             # return 
#             def seg_intersect (a1,a2, b1,b2):
#                 da = a2-a1
#                 db = b2-b1
#                 dp = a1-b1
#                 dap = perp (da)
#                 denom = dot (dap, db)
#                 num = dot (dap, dp )
#                 return (num / denom)*db + b1

#             p1 = array( [-6.0, +6.0] )
#             p2 = array( [-3.0, -4.8] )

#             p3 = array( [+4.0, -5.0] )
#             p4 = array( [+4.0, +2.0] )

#             st.write(seg_intersect(p1,p2,p3,p4))

#             # selection of discrimination diagram
#             dis_type = st.sidebar.radio('Discrimination diagram:',['SiO2/20 - K2O+Na2O - TiO2+MgO+Fe2O3', 'log(Fe2O3/K2O) - log(SiO2/Al2O3)'])

	    # Harker diagram
    if st.sidebar.checkbox('Harker diagram'):
        st.header('Harker diagram')
        ox =['sample','category','subcategory','subsubcategory','reference','SiO2','TiO2','Al2O3','Fe2O3','FeO','MnO','MgO','CaO','Na2O','K2O','P2O5']
        data_harker=data[ox]
        fig = make_subplots(specs=[[{"secondary_y": True}]])

        # Add traces
        fig.add_trace(
            go.Scatter(x=data_harker['SiO2'], y=data_harker['TiO2'], name="TiO<sub>2</sub>", mode='markers'),secondary_y=False,)
        fig.add_trace(
            go.Scatter(x=data_harker['SiO2'], y=data_harker['Al2O3'], name="Al<sub>2</sub>O<sub>3</sub>", mode='markers'),secondary_y=False,)
        fig.add_trace(        
        go.Scatter(x=data_harker['SiO2'], y=data_harker['Fe2O3'], name="Fe<sub>2</sub>O<sub>3</sub>", mode='markers'),secondary_y=False,)
        fig.add_trace(        
            go.Scatter(x=data_harker['SiO2'], y=data_harker['FeO'], name="FeO", mode='markers'),secondary_y=False,)
        fig.add_trace(        
            go.Scatter(x=data_harker['SiO2'], y=data_harker['MnO'], name="MnO", mode='markers'),secondary_y=False,)
        fig.add_trace(        
            go.Scatter(x=data_harker['SiO2'], y=data_harker['MgO'], name="MgO", mode='markers'),secondary_y=False,)
        fig.add_trace(        
            go.Scatter(x=data_harker['SiO2'], y=data_harker['CaO'], name="CaO", mode='markers'),secondary_y=False,)
        fig.add_trace(        
            go.Scatter(x=data_harker['SiO2'], y=data_harker['Na2O'], name="Na<sub>2</sub>O<sub>", mode='markers'),secondary_y=False,)
        fig.add_trace(        
            go.Scatter(x=data_harker['SiO2'], y=data_harker['K2O'], name="K<sub>2</sub>O<sub>", mode='markers'),secondary_y=False,)
        fig.add_trace(        
            go.Scatter(x=data_harker['SiO2'], y=data_harker['P2O5'], name="P<sub>2</sub>O<sub>5</sub>", mode='markers'),secondary_y=False,)                   
        
        # trendline
        data_harker = data_harker.dropna() # dropping missing values
        trend = LinearRegression()        
        x = data_harker.loc[:, data_harker.columns == 'SiO2']
        
        y = data_harker.loc[:, data_harker.columns == 'TiO2']
        trend.fit(x,y)
        data_harker['trend_TiO2'] = trend.predict(x)
        fig.add_trace(        
            go.Scatter(x=data_harker['SiO2'], y=data_harker['trend_TiO2'], name='TiO<sub>2</sub>', mode='lines'),secondary_y=False,)
        
        y = data_harker.loc[:, data_harker.columns == 'Al2O3']
        trend.fit(x,y)
        data_harker['trend_Al2O3'] = trend.predict(x)
        fig.add_trace(        
            go.Scatter(x=data_harker['SiO2'], y=data_harker['trend_Al2O3'], name='Al<sub>2</sub>O<sub>3</sub>', mode='lines'),secondary_y=False,) 

        y = data_harker.loc[:, data_harker.columns == 'Fe2O3']
        trend.fit(x,y)
        data_harker['trend_Fe2O3'] = trend.predict(x)
        fig.add_trace(        
            go.Scatter(x=data_harker['SiO2'], y=data_harker['trend_Fe2O3'], name='Fe<sub>2</sub>O<sub>3</sub>', mode='lines'),secondary_y=False,)         

        y = data_harker.loc[:, data_harker.columns == 'FeO']
        trend.fit(x,y)
        data_harker['trend_FeO'] = trend.predict(x)
        fig.add_trace(        
            go.Scatter(x=data_harker['SiO2'], y=data_harker['trend_FeO'], name='FeO', mode='lines'),secondary_y=False,)

        y = data_harker.loc[:, data_harker.columns == 'MnO']
        trend.fit(x,y)
        data_harker['trend_MnO'] = trend.predict(x)
        fig.add_trace(        
            go.Scatter(x=data_harker['SiO2'], y=data_harker['trend_MnO'], name='MnO', mode='lines'),secondary_y=False,) 

        y = data_harker.loc[:, data_harker.columns == 'MgO']
        trend.fit(x,y)
        data_harker['trend_MgO'] = trend.predict(x)
        fig.add_trace(        
            go.Scatter(x=data_harker['SiO2'], y=data_harker['trend_MgO'], name='MgO', mode='lines'),secondary_y=False,)

        y = data_harker.loc[:, data_harker.columns == 'CaO']
        trend.fit(x,y)
        data_harker['trend_CaO'] = trend.predict(x)
        fig.add_trace(        
            go.Scatter(x=data_harker['SiO2'], y=data_harker['trend_CaO'], name='CaO', mode='lines'),secondary_y=False,)

        y = data_harker.loc[:, data_harker.columns == 'Na2O']
        trend.fit(x,y)
        data_harker['trend_Na2O'] = trend.predict(x)
        fig.add_trace(        
            go.Scatter(x=data_harker['SiO2'], y=data_harker['trend_Na2O'], name='Na<sub>2</sub>O', mode='lines'),secondary_y=False,)          
        
        y = data_harker.loc[:, data_harker.columns == 'K2O']
        trend.fit(x,y)
        data_harker['trend_K2O'] = trend.predict(x)
        fig.add_trace(        
            go.Scatter(x=data_harker['SiO2'], y=data_harker['trend_K2O'], name='K<sub>2</sub>O', mode='lines'),secondary_y=False,)

        y = data_harker.loc[:, data_harker.columns == 'P2O5']
        trend.fit(x,y)
        data_harker['trend_P2O5'] = trend.predict(x)
        fig.add_trace(        
            go.Scatter(x=data_harker['SiO2'], y=data_harker['trend_P2O5'], name='P<sub>2</sub>O<sub>5</sub>', mode='lines'),secondary_y=False,)        
        
        fig.update_yaxes(rangemode="nonnegative")
        fig.update_layout(xaxis_title='SiO<sub>2</sub> (%)', yaxis_title='Oxide (%)', showlegend=True)   
        
        st.plotly_chart(fig, use_container_width=True)

    # boxplot
    def box(x,y,color):
        box = px.box(data, x=x, y=y, color=color)
        box.update_layout(showlegend=False)
        st.plotly_chart(box, use_container_width=True)
        
        # exporting the plot to the local machine
        with st.expander("Click to export boxplot"):
            if st.button("boxplot as HTML"):
                plot_html(box)
            
    if st.sidebar.checkbox('Sunburst plot, Statistical details, Histogram, Boxplot, Scatter matrix, Correlation matrix and Heatmap'):
        data_ox_pr = data.drop(["molar_SiO2","molar_TiO2","molar_Al2O3","molar_Fe2O3","molar_MnO","molar_MgO","molar_CaO","molar_Na2O","molar_K2O","molar_P2O5","molar_CO2","diff","molar_CaO*"], axis=1)

        if st.sidebar.checkbox('Statistical details'):
            st.subheader('Statistical details')
            stats = data_ox_pr.describe()
            st.write(stats, use_container_width=True)
            
            @st.cache
            def convert_df(stats):
                return stats.to_csv(index=True).encode('utf-8')
            stats = convert_df(stats)
            st.download_button("Press to download",stats,"stats.csv","csv",key='download-stats-csv')

        # Subburst plot
        if st.sidebar.checkbox('Sunburst plot'):
            st.header('Sunburst plot')            
            
            # selection of 'values'
            values = st.sidebar.expander('Values', False)            
            values = values.selectbox("Select the Oxide and/or Weathering proxy for values:", data_ox_pr.drop(["sample","category","subcategory","subsubcategory","reference"], axis=1).columns)
            
            # selection of 'color'
            color = st.sidebar.expander('Color', False)            
            color = color.selectbox("Select the Oxide and/or Weathering proxy for color:", data_ox_pr.drop(["sample","category","subcategory","subsubcategory","reference"], axis=1).columns)            
            
            sun = px.sunburst(data_ox_pr, path=['category','subcategory','subsubcategory','sample'], values=values, color=color)
            sun.update_traces(sort=False)
            st.plotly_chart(sun, use_container_width=True)
            
            # exporting the plot to the local machine
            with st.expander("Click to export Sunburst plot"):
                plot_html(sun)            
                  
        if st.sidebar.checkbox('Histogram'):
            st.subheader('Histogram')

            # selection of variable(s) (oxide and/or weathering index)
            var = st.sidebar.expander('Oxide and/or Weathering proxy', False)            
            var = var.multiselect("Select the Oxide and/or Weathering proxy of Histogram:", data_ox_pr.drop(["sample","category","subcategory","subsubcategory","reference"], axis=1).columns)

            # Linear/Non-linear y axis
            yaxis_type = st.sidebar.expander('Y-axis type', False)            
            yaxis_type = yaxis_type.radio('y axis type of Histogram:',['Linear', 'Logarithmic'])
            if yaxis_type=='Linear':
                log_y=False
            else:
                log_y=True
            
            hist = px.histogram(data_ox_pr, x=var, opacity=0.6, log_y=log_y)
            hist.update_layout(xaxis_title="Oxide/Weathering proxy")
            st.plotly_chart(hist)
            
            # exporting the plot to the local machine
            with st.expander("Click to export Histogram"):
                plot_html(hist)
        
        if st.sidebar.checkbox('Boxplot'):
            st.subheader('Boxplot')
            category = st.sidebar.expander('Categorization', False)            
            category = category.radio('Categorization of the boxplot', ['Category','Subcategory','Subsubcategory'])
            if category=='Category':
                color=data_ox_pr['category']
            elif category=='Subcategory':
                color=data_ox_pr['subcategory']
            else:
                color=data_ox_pr['subsubcategory']

            axis = st.sidebar.expander('Axes', False)            
            x = axis.selectbox('Select the x-axis of Boxplot',list(data_ox_pr))
            y = axis.selectbox('Select the y-axis of Boxplot',list(data_ox_pr))
            box(x,y,color)

        # scatter matrix of oxides
        if st.sidebar.checkbox('Scatter matrix of oxides'):
            st.subheader('Scatter matrix of oxides')
            scatter_ox = px.scatter_matrix(data_ox_pr, dimensions=['SiO2','TiO2','Al2O3','Fe2O3','FeO','MnO','MgO','CaO','Na2O','K2O'], hover_name="sample")
            st.plotly_chart(scatter_ox, use_container_width=True)

            # exporting the plot to the local machine
            with st.expander("Click to export Scatter matrix of oxides"):
                if st.button("Scatter matrix of oxides as HTML"):
                    plot_html(scatter_ox)
        
        # scatter matrix of weathering indices
        if st.sidebar.checkbox('Scatter matrix of weathering proxy'):
            st.subheader('Scatter matrix of weathering proxy')
            scatter_pr = px.scatter_matrix(data_ox_pr, dimensions=["(CIW)", "(CIW*)", "(CPA)", "(CIA)", "(PIA)", "(CIX)", "(ICV)", "(WIP)","SiO2/Al2O3","K2O/Al2O3","K2O/Na2O","Al2O3/TiO2"], hover_name="sample")
            st.plotly_chart(scatter_pr, use_container_width=True)
            
            # exporting the plot to the local machine
            with st.expander("Click to export Scatter matrix of weathering indices"):
                if st.button("Scatter matrix of weathering indices as HTML"):
                    plot_html(scatter_pr)

        # correlation matrix
        if st.sidebar.checkbox('Correlation matrix'):
            data_corr=data_ox_pr
            st.subheader('Correlation matrix')
            
            # oxide, weathering indices filter
            if st.sidebar.checkbox('Oxides/Weathering proxy filter'):
                filter = st.sidebar.expander('filter', False)                
                filter = filter.radio('Choose the filter of Oxides/Weathering proxy', ['Oxides','Weathering proxy'])
                if filter=='Oxides':                
                    ox =["sample","category","subcategory","subsubcategory","reference","SiO2","TiO2","Al2O3","Fe2O3","MgO","CaO","Na2O","K2O"]
                    data_corr=data[ox]
                if filter=='Weathering proxy':                
                    pr =["sample","category","subcategory","subsubcategory","reference","(CIW)","(CIW*)","(CPA)","(CIA)","(PIA)","(CIX)","(ICV)","(WIP)","SiO2/Al2O3","K2O/Al2O3","K2O/Na2O","Al2O3/TiO2"]
                    data_corr=data[pr]                     
            
            # Method of correlation
            method = st.sidebar.expander('method of correlation', False)            
            method = method.radio('Choose the method of correlation', ['Pearson', 'Kendall','Spearman'])
            if method=='Pearson':
                method='pearson'
            elif method=='Kendall':
                method='kendall'
            else:
                method='spearman'

            corrMatrix = round(data_corr.corr(method=method), 4)
            st.write(corrMatrix, use_container_width=True)

            @st.cache
            def convert_df(corrMatrix):
                return corrMatrix.to_csv(index=False).encode('utf-8')
            corrMatrix = convert_df(corrMatrix)
            st.download_button("Press to download",corrMatrix,"corrMatrix.csv","csv",key='download-corrMatrix-csv')

            # heatmap
            if st.sidebar.checkbox('Heatmap of correlation matrix'):
                st.subheader('Heatmap of correlation matrix')
                color_continuous_scale=None
                
                if st.sidebar.checkbox('Color scale'):
                    color_scale = ['agsunset','blackbody','bluered','blues','blugrn','bluyl','brwnyl','bugn','bupu','burg','burgyl','cividis','darkmint','electric','emrld','gnbu','greens','greys','hot','inferno','jet','magenta','magma','mint','orrd','oranges','oryel','peach','pinkyl','plasma','plotly3','pubu','pubugn','purd','purp','purples','purpor','rainbow','rdbu','rdpu','redor','reds','sunset','sunsetdark','teal','tealgrn','turbo','viridis','ylgn','ylgnbu','ylorbr','ylorrd','algae','amp','deep','dense','gray','haline','ice','matter','solar','speed','tempo','thermal','turbid','armyrose','brbg','earth','fall','geyser','prgn','piyg','picnic','portland','puor','rdgy','rdylbu','rdylgn','spectral','tealrose','temps','tropic','balance','curl','delta','oxy','edge','hsv','icefire','phase','twilight','mrybm','mygbm'] 
                    color_continuous_scale = st.sidebar.selectbox('Select the color:', color_scale)                      
                heat = px.imshow(data_corr.corr(method=method), color_continuous_scale=color_continuous_scale)           
                st.plotly_chart(heat, use_container_width=True)

                # exporting the plot to the local machine
                with st.expander("Click to export Heatmap of correlation matrix"):
                    plot_html(heat)
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