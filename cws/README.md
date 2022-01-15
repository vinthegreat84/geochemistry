# CWS
## Version 1.0
## App to analyze major elemental geochemical data of clastic sediments
CWS is a tool designed using Python and Streamlit to analyze major elemental geochemistry of clastic sediments. Current functionality includes:

* **Variation diagram**: Variation of major oxides against samples.
* **Data filter**: Data filter based on sample/category/subcategory/subsubcategory.
* **Weathering proxy**: Data table of chemical weathering indices including Chemical Index of Weathering (CIW) after [**Harnois, 1988**](https://doi.org/10.1016/0037-0738(88)90137-6); Chemical Proxy of Alteration (CPA) after [**Buggle et al., 2011**](https://doi.org/10.1016/j.quaint.2010.07.019); Chemical Index of Alteration (CIA) after [**Nesbitt and Young, 1982**](https://doi.org/10.1038/299715a0); Plagioclase Index of Alteration (PIA) after [**Fedo et al., 1995**](https://doi.org/10.1130/0091-7613(1995)023<0921:UTEOPM>2.3.CO;2); Modified Chemical Index of Alteration (CIX) after [**Garzanti et al., 2014**](https://doi.org/10.1016/j.chemgeo.2013.12.016); Index of Compositional Variability (ICV) after [**Cox et al., 1995**](https://doi.org/10.1016/0016-7037(95)00185-9); Weathering Index of Parker (WIP) after [**Parker, 1970**](https://doi.org/10.1017/S0016756800058581) and chemical proxies like SiO2/Al2O3, K2O/Al2O3, Al2O3/TiO2.
* **Bivariate plot:** Bivariate plot between oxide and/or weathering index with variable-based marker size and linear/non-linear trendline and axes.
* **Compositional space diagram**: Compositional space diagrams including A - CN - K compositional space diagram after [**Nesbitt and Young, 1982**](https://doi.org/10.1038/299715a0); A - CNK - FM compositional space diagram after [**Nesbitt and Young, 1989**](https://doi.org/10.1086/629290) and M - F - W compositional space diagramm after [**Ohta and Arai, 2007**](https://doi.org/10.1016/j.chemgeo.2007.02.017).
* **Boxplot, Scatter matrix, Correlation matrix and Heatmap**: Boxplot, Scatter matrix, Correlation matrix and Heatmap of chemical weathering indices and proxies.

A running version of the app can be accessed at https://tinyurl.com/sedweather. The app may run slowly when accessing it. This is due to the hosting and should not affect functionality.

## Notes on Usage
The app can be cloned and run locally using streamlit: streamlit run cws.py. When doing this, ensure you have the required modules listed in the requirements file.
Scales on interactive plots can be changed by double clicking on the lower/upper limit values.
