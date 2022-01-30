import streamlit as st
from streamlit.components.v1 import iframe
st.set_page_config(layout="wide", page_title='CWS 0.1.0')

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly import tools
import plotly.io as pio
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.figure_factory as ff
import seaborn as sns
import matplotlib.pyplot as plt
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
# spider plot
# histogram and to check the distribution type
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
    st.write('**Data filter:** Data filter based on sample/category/subcategory/subsubcategory.')
    st.write('**Major Oxides variation**: Variation of major oxides against samples.')
    st.write('**Weathering proxy:** Data table of chemical weathering indices including Chemical Index of Weathering (CIW) after [**Harnois, 1988**](https://doi.org/10.1016/0037-0738(88)90137-6); Chemical Proxy of Alteration (CPA) after [**Buggle et al., 2011**](https://doi.org/10.1016/j.quaint.2010.07.019); Chemical Index of Alteration (CIA) after [**Nesbitt and Young, 1982**](https://doi.org/10.1038/299715a0); Plagioclase Index of Alteration (PIA) after [**Fedo et al., 1995**](https://doi.org/10.1130/0091-7613(1995)023<0921:UTEOPM>2.3.CO;2); Modified Chemical Index of Alteration (CIX) after [**Garzanti et al., 2014**](https://doi.org/10.1016/j.chemgeo.2013.12.016); Index of Compositional Variability (ICV) after [**Cox et al., 1995**](https://doi.org/10.1016/0016-7037(95)00185-9); Weathering Index of Parker (WIP) after [**Parker, 1970**](https://doi.org/10.1017/S0016756800058581) and chemical proxies like SiO2/Al2O3, K2O/Al2O3, Al2O3/TiO2.')
    st.write('**Bivariate plot:** Bivariate plot between oxide and/or weathering index with variable-based marker size, linear/non-linear trendline & axes, and marginal distribution.')
    st.write('**Trivariate plot:** Trivariate plot between oxide and/or weathering index with variable-based marker size and linear/non-linear trendline & axes.')
    st.write('**Compositional space diagram:** Compositional space diagrams including A - CN - K compositional space diagram after [**Nesbitt and Young, 1982**](https://doi.org/10.1038/299715a0); A - CNK - FM compositional space diagram after [**Nesbitt and Young, 1989**](https://doi.org/10.1086/629290) and M - F - W compositional space diagram after [**Ohta and Arai, 2007**](https://doi.org/10.1016/j.chemgeo.2007.02.017).')
    st.write('**Sunburst plot, Histogram, Boxplot, Scatter matrix, Correlation matrix and Heatmap:** Sunburst plot, Histogram, Boxplot, Scatter matrix, Correlation matrix and Heatmap of chemical weathering indices and weathering proxies.')
        
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
        # selection of country from 'location'
        filter = st.sidebar.radio('Select the data filter:',['sample', 'category', 'subcategory','subsubcategory'])
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
            
    # Major oxides variation
    if st.sidebar.checkbox('Major oxides variation'):
        st.header('Major oxides variation')
        data_var = data
        st.write(data_var)

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
    data['Al2O3/TiO2'] = data['Al2O3'] / data['TiO2']
        
    if st.sidebar.checkbox('Weathering proxy'):
        st.header('Weathering proxy')
        proxy =["sample","category","subcategory","subsubcategory","reference","(CIW)","(CPA)","(CIA)","(PIA)","(CIX)","(ICV)","(WIP)","SiO2/Al2O3","K2O/Al2O3","Al2O3/TiO2"]
        proxy=data[proxy]
        st.write(proxy)
        
        proxy_download=proxy
        @st.cache
        def convert_df(proxy_download):
            return proxy_download.to_csv(index=False).encode('utf-8')
        proxy_download = convert_df(proxy_download)
        st.download_button("Press to download",proxy_download,"proxy.csv","csv",key='download-proxy-csv')

        # weathering indices variation
        if st.sidebar.checkbox('Weathering proxy variation'):
            st.header('Weathering proxy variation')

            var_proxy = px.line(proxy, x='sample', y=['(CIW)','(CPA)','(CIA)','(PIA)','(CIX)','(ICV)','(WIP)','SiO2/Al2O3','K2O/Al2O3','Al2O3/TiO2'])
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
        size=None
        trendline=None      
        marginal_x=None
        marginal_y=None
        if st.sidebar.checkbox('Trendline'):
            data_bivar = data_bivar.drop(["sample","category","subcategory","subsubcategory","reference"], axis=1)
            hover_name=None
            color=None
            symbol=None            
            trendline_type = st.sidebar.radio('Trendline:',['Linear', 'Non-Linear'])
            if trendline_type=='Linear':
                trendline="ols"
            else:
                trendline="lowess"    
        
        if st.sidebar.checkbox('Variable-based marker size'):
            size = st.sidebar.radio('Select the oxide/weathering index/ratio:',['oxide', 'weathering index', 'ratio'])
            if size=='oxide':
                col_first="SiO2"
                col_last="P2O5"
            if size=='weathering index':
                col_first="(CIW)"
                col_last="(WIP)"            
            if size=='ratio':
                col_first="SiO2/Al2O3"
                col_last="Al2O3/TiO2"
            size = st.sidebar.selectbox('Select the oxide/weathering index/ratio',(list(data_bivar.loc[:,col_first:col_last])))
            
        if st.sidebar.checkbox('Add marginal distribution'):
            if st.sidebar.checkbox('X-axis marginal distribution'):
                type = st.sidebar.radio('Select the X-axis marginal distribution:',['histogram','rug','box','violin'])
                if type=='histogram':
                    marginal_x='histogram'
                if type=='rug':
                    marginal_x='rug'
                if type=='box':
                    marginal_x='box'
                if type=='violin':
                    marginal_x='violin'
            if st.sidebar.checkbox('Y-axis marginal distribution'):
                type = st.sidebar.radio('Select the Y-axis marginal distribution:',['histogram','rug','box','violin'])
                if type=='histogram':
                    marginal_y='histogram'
                if type=='rug':
                    marginal_y='rug'
                if type=='box':
                    marginal_y='box'
                if type=='violin':
                    marginal_y='violin'
                    
        x = st.sidebar.selectbox('Select the x-axis',(list(data_bivar)))
        xaxis_type = st.sidebar.radio('x axis type:',['Linear', 'Logarithmic'])
        if xaxis_type=='Linear':
            log_x=False
        else:
            log_x=True
            marginal_x=None
        
        y = st.sidebar.selectbox('Select the y-axis',(list(data_bivar)))
        yaxis_type = st.sidebar.radio('y axis type:',['Linear', 'Logarithmic'])
        if yaxis_type=='Linear':
            log_y=False
        else:
            log_y=True 
            marginal_y=None
            
        bivar = px.scatter(data_bivar, x=x, y=y, log_x=log_x, log_y=log_y, hover_name=hover_name, color=color, symbol=symbol, size=size, trendline=trendline, marginal_x=marginal_x, marginal_y=marginal_y, render_mode="webgl", title="Bivariate Plot", color_discrete_sequence=px.colors.qualitative.Antique
    )        
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
        size=None
        trendline=None      
        marginal_x=None
        marginal_y=None
        marginal_z=None   
        
        if st.sidebar.checkbox('Variable-based marker size of trivariate plot'):
            size = st.sidebar.radio('Select the oxide/weathering index/ratio:',['oxide', 'weathering index', 'ratio'])
            if size=='oxide':
                col_first="SiO2"
                col_last="P2O5"
            if size=='weathering index':
                col_first="(CIW)"
                col_last="(WIP)"            
            if size=='ratio':
                col_first="SiO2/Al2O3"
                col_last="Al2O3/TiO2"
            size = st.sidebar.selectbox('Select the oxide/weathering index/ratio',(list(data_trivar.loc[:,col_first:col_last])))                              
                    
        x = st.sidebar.selectbox('Select the x-axis of trivariate plot',(list(data_trivar)))
        xaxis_type = st.sidebar.radio('x axis type of trivariate plot:',['Linear', 'Logarithmic'])
        if xaxis_type=='Linear':
            log_x=False
        else:
            log_x=True
            marginal_x=None
        
        y = st.sidebar.selectbox('Select the y-axis of trivariate plot',(list(data_trivar)))
        yaxis_type = st.sidebar.radio('y axis type of trivariate plot:',['Linear', 'Logarithmic'])
        if yaxis_type=='Linear':
            log_y=False
        else:
            log_y=True 
            marginal_y=None

        z = st.sidebar.selectbox('Select the z-axis of trivariate plot',(list(data_trivar)))
        zaxis_type = st.sidebar.radio('z axis type of trivariate plot:',['Linear', 'Logarithmic'])
        if zaxis_type=='Linear':
            log_z=False
        else:
            log_z=True 
            marginal_z=None            
            
        trivar = px.scatter_3d(data_trivar, x=x, y=y, z=z, log_x=log_x, log_y=log_y, log_z=log_z, hover_name=hover_name, color=color, symbol=symbol, size=size, title="Trivariate Plot", color_discrete_sequence=px.colors.qualitative.Antique
    )        
        st.plotly_chart(trivar, use_container_width=True)        
        
    # Ternary plot
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
        return tern_plot
    
    # Compositional space diagrams selection
    if st.sidebar.checkbox('Compositional space diagram'):
        st.header('Compositional space diagram')
        csd =["sample","category","subcategory","subsubcategory","reference","SiO2","TiO2","Al2O3","Fe2O3","MgO","CaO","Na2O","K2O","molar_Al2O3","molar_CaO*","molar_Na2O","molar_K2O","molar_Fe2O3","molar_MgO"]
        data_csd=data[csd]
        hover_name=data_csd['sample']        
        type = st.sidebar.radio('Categorization', ['Category','Subcategory'])
        if type=='Category':
            color=data_csd['category']
            symbol=None
        else:
            color=data_csd['subcategory']
            symbol=data_csd['subsubcategory']        
        csd_type = st.sidebar.radio('Compositional space diagram:',['A - CN - K', 'A - CNK - FM', 'M - F - W'])
        x=data_csd['molar_Al2O3']
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

        # exporting the plot to the local machine
        with st.expander("Click to export compositional space diagram"):
#             if st.button("compositional space diagram as PNG"):
#                 fig.write_image("tern_plot.png")
#             if st.button("compositional space diagram as JPEG"):
#                 fig.write_image("tern_plot.JPEG")
#             if st.button("compositional space diagram as WebP"):
#                 fig.write_image("tern_plot.webp")
#             if st.button("compositional space diagram as SVG"):
#                 fig.write_image("tern_plot.svg") 
#             if st.button("compositional space diagram as PDF"):
#                 fig.write_image("tern_plot.pdf")
            if st.button("compositional space diagram as HTML"):
#                 buffer = io.StringIO()
#                 fig.write_html(buffer, include_plotlyjs='cdn')
#                 html_bytes = buffer.getvalue().encode()
                
#                 st.download_button(
#                     label='Download HTML',
#                     data=html_bytes,
#                     file_name='tern_plot.html',
#                     mime='text/html'
#                 )
                plot_html(fig)

    
    # boxplot
    def box(x,y,color):
        box = px.box(data, x=x, y=y, color=color)
        box.update_layout(showlegend=False)
        st.plotly_chart(box, use_container_width=True)
        
        # exporting the plot to the local machine
        with st.expander("Click to export boxplot"):
#             if st.button("boxplot as PNG"):
#                 box.write_image("box.png")
#             if st.button("boxplot as JPEG"):
#                 box.write_image("box.JPEG")
#             if st.button("boxplot as WebP"):
#                 box.write_image("box.webp")
#             if st.button("boxplot as SVG"):
#                 box.write_image("box.svg") 
#             if st.button("boxplot as PDF"):
#                 box.write_image("box.pdf")
#             if st.button("boxplot as HTML"):
#                 buffer = io.StringIO()
#                 box.write_html(buffer, include_plotlyjs='cdn')
#                 html_bytes = buffer.getvalue().encode()
                
#                 st.download_button(
#                     label='Download HTML',
#                     data=html_bytes,
#                     file_name='box.html',
#                     mime='text/html'
#                 )
                plot_html(box)
            
    if st.sidebar.checkbox('Sunburst plot, Histogram, Boxplot, Scatter matrix, Correlation matrix and Heatmap'):
        ox_wi =["sample","category","subcategory","subsubcategory","reference","SiO2","TiO2","Al2O3","Fe2O3","MgO","CaO","Na2O","K2O","(CIW)","(CPA)","(CIA)","(PIA)","(CIX)","(ICV)","(WIP)"]
        data_ox_wi=data[ox_wi]
        
        # Subburst
        if st.sidebar.checkbox('Sunburst plot'):
            st.header('Sunburst plot')            

            # selection of 'values'
            values = st.sidebar.selectbox("Select the Oxide and/or Weathering index:", data_ox_wi.drop(["sample","category","subcategory","subsubcategory","reference"], axis=1).columns)
            sun = px.sunburst(data_ox_wi, path=['sample','category','subcategory','subsubcategory'], values=values)
            st.plotly_chart(sun, use_container_width=True)
            
            # exporting the plot to the local machine
            with st.expander("Click to export Sunburst plot"):
                plot_html(sun)            

        if st.sidebar.checkbox('Histogram'):
            st.subheader('Histogram')

            # selection of variable(s) (oxide and/or weathering index)
            var = st.sidebar.multiselect("Select the Oxide and/or Weathering index:", data_ox_wi.drop(["sample","category","subcategory","subsubcategory","reference"], axis=1).columns)

            # Linear/Non-linear y axis
            yaxis_type = st.sidebar.radio('y axis type:',['Linear', 'Logarithmic'])
            if yaxis_type=='Linear':
                log_y=False
            else:
                log_y=True
            
            hist = px.histogram(data_ox_wi, x=var, opacity=0.6, log_y=log_y)
            hist.update_layout(xaxis_title="Oxide/Weathering Index")
            st.plotly_chart(hist)
            
            # exporting the plot to the local machine
            with st.expander("Click to export Histogram"):
                plot_html(hist)
            
#             stats = data_ox_wi.describe
#             st.write(stats)  
        
        if st.sidebar.checkbox('Boxplot'):
            st.subheader('Boxplot')
            type = st.sidebar.radio('Categorization of the boxplot', ['Category','Subcategory','Subsubcategory'])
            if type=='Category':
                color=data_ox_wi['category']
            elif type=='Subcategory':
                color=data_ox_wi['subcategory']
            else:
                color=data_ox_wi['subsubcategory']

            x = st.sidebar.selectbox('Select the x-axis',(list(data_ox_wi)))
            y = st.sidebar.selectbox('Select the y-axis',(list(data_ox_wi)))
            box(x,y,color)

        # scatter matrix of oxides
        if st.sidebar.checkbox('Scatter matrix of oxides'):
            st.subheader('Scatter matrix of oxides')
            scatter_ox = px.scatter_matrix(data_ox_wi, dimensions=["SiO2","TiO2","Al2O3","Fe2O3","MgO","CaO","Na2O","K2O"], hover_name="sample")
            st.plotly_chart(scatter_ox, use_container_width=True)

            # exporting the plot to the local machine
            with st.expander("Click to export Scatter matrix of oxides"):
#                 if st.button("Scatter matrix of oxides as PNG"):
#                     scatter_ox.write_image("scatter_ox.png")
#                 if st.button("Scatter matrix of oxides as JPEG"):
#                     scatter_ox.write_image("scatter_ox.JPEG")
#                 if st.button("Scatter matrix of oxides as WebP"):
#                     scatter_ox.write_image("scatter_ox.webp")
#                 if st.button("Scatter matrix of oxides as SVG"):
#                     scatter_ox.write_image("scatter_ox.svg") 
#                 if st.button("Scatter matrix of oxides as PDF"):
#                     scatter_ox.write_image("scatter_ox.pdf")
#                 if st.button("Scatter matrix of oxides as HTML"):
#                     buffer = io.StringIO()
#                     scatter_ox.write_html(buffer, include_plotlyjs='cdn')
#                     html_bytes = buffer.getvalue().encode()

#                     st.download_button(
#                         label='Download HTML',
#                         data=html_bytes,
#                         file_name='Scatter matrix of oxides.html',
#                         mime='text/html'
#                     )
                    plot_html(scatter_ox)
        
        # scatter matrix of weathering indices
        if st.sidebar.checkbox('Scatter matrix of weathering indices'):
            st.subheader('Scatter matrix of weathering indices')
            scatter_wi = px.scatter_matrix(data_ox_wi, dimensions=["(CIW)", "(CPA)", "(CIA)", "(PIA)", "(CIX)", "(ICV)", "(WIP)"], hover_name="sample")
            st.plotly_chart(scatter_wi, use_container_width=True)
            
            # exporting the plot to the local machine
            with st.expander("Click to export Scatter matrix of weathering indices"):
#                 if st.button("Scatter matrix of weathering indices as PNG"):
#                     scatter_wi.write_image("scatter_wi.png")
#                 if st.button("Scatter matrix of weathering indices as JPEG"):
#                     scatter_wi.write_image("scatter_wi.JPEG")
#                 if st.button("Scatter matrix of weathering indices as WebP"):
#                     scatter_wi.write_image("scatter_wi.webp")
#                 if st.button("Scatter matrix of weathering indices as SVG"):
#                     scatter_wi.write_image("scatter_wi.svg") 
#                 if st.button("Scatter matrix of weathering indices as PDF"):
#                     scatter_wi.write_image("scatter_wi.pdf")
#                 if st.button("Scatter matrix of weathering indices as HTML"):
#                     buffer = io.StringIO()
#                     scatter_wi.write_html(buffer, include_plotlyjs='cdn')
#                     html_bytes = buffer.getvalue().encode()

#                     st.download_button(
#                         label='Download HTML',
#                         data=html_bytes,
#                         file_name='Scatter matrix of weathering indices.html',
#                         mime='text/html'
#                     )
                    plot_html(scatter_wi)

        # correlation matrix
        if st.sidebar.checkbox('Correlation matrix'):
            data_corr=data_ox_wi
            st.subheader('Correlation matrix')
            
            # oxide, weathering indices filter
            if st.sidebar.checkbox('Oxide/Weathering indices filter'):
                filter = st.sidebar.radio('Choose the filter', ['Oxides','Weathering indices'])
                if filter=='Oxides':                
                    ox =["sample","category","subcategory","subsubcategory","reference","SiO2","TiO2","Al2O3","Fe2O3","MgO","CaO","Na2O","K2O"]
                    data_corr=data[ox]
                if filter=='Weathering indices':                
                    wi =["sample","category","subcategory","subsubcategory","reference","(CIW)","(CPA)","(CIA)","(PIA)","(CIX)","(ICV)","(WIP)"]
                    data_corr=data[wi]                     
            
            # Method of correlation
            method = st.sidebar.radio('Choose the method of correlation', ['Pearson', 'Kendall','Spearman'])
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
                heat, ax = plt.subplots()
                sns.heatmap(data_corr.corr(method=method), ax=ax)
                st.write(heat)
                 # exporting the plot to the local machine
#                 with st.expander("Click to export Heatmap of correlation matrix"):
#                     if st.button("Heatmap of correlation matrix as PNG"):
#                         heat.savefig('heat.png')
#                     if st.button("Heatmap of correlation matrix as JPEG"):
#                         heat.savefig("heat.JPEG")
#                     if st.button("Heatmap of correlation matrix as SVG"):
#                         heat.savefig("heat.svg") 
#                     if st.button("Heatmap of correlation matrix as PDF"):
#                         heat.savefig("heat.pdf")   
	
#     env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
#     template = env.get_template("template.html")
#     form = left.form("template_form")
#     submit = form.form_submit_button("Generate PDF")

#     if submit:
#         html = template.render(
#             data=data
#         )

#         pdf = pdfkit.from_string(html, False)
#         st.balloons()

#         right.success("🎉 Your diploma was generated!")
#         # st.write(html, unsafe_allow_html=True)
#         # st.write("")
#         right.download_button(
#             "⬇️ Download PDF",
#             data=pdf,
#             file_name="diploma.pdf",
#             mime="application/octet-stream",
#         )
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