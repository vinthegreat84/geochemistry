# CWS
## Version 1.0
## App to analyze major elemental geochemical data of clastic sediments
CWS is a tool designed using Python and Streamlit to analyze major elemental geochemistry of clastic sediments. Current functionality includes:

* **Variation plot**: Variation of major oxides against samples.
* **Data filter**: Data filter based on sample/category/subcategory/subsubcategory.
* **Weathering proxy**: Data table of chemical weathering indices including Chemical Index of Weathering (CIW) after *Harnois, 1988*; Chemical Proxy of Alteration (CPA) after *Buggle et al., 2011*; Chemical Index of Alteration (CIA) after *Nesbitt and Young, 1982*; Plagioclase Index of Alteration (PIA) after *Fedo et al., 1995*; Modified Chemical Index of Alteration (CIX) after *Garzanti et al., 2014*; Index of Compositional Variability (ICV) after *Cox et al., 1995*; Weathering Index of Parker (WIP) after *Parker, 1970* and and chemical proxies like SiO2/Al2O3, K2O/Al2O3, Al2O3/TiO2.
* **Compositional space diagram**: Compositional space diagrams including A - CN - K compositional space diagram after *Nesbitt and Young, 1982*; A - CNK - FM compositional space diagram after *Nesbitt and Young, 1989* and M - F - W compositional space diagramm after *Ohta and Arai, 2007*.
* **Boxplot, Scatter matrix, Correlation matrix and Heatmap**: Boxplot, Scatter matrix, Correlation matrix and Heatmap of chemical weathering indices and proxies.

A running version of the app can be accessed at https://tinyurl.com/sedweather. The app may run slowly when accessing it. This is due to the hosting and should not affect functionality.

## Notes on Usage
The app can be cloned and run locally using streamlit: streamlit run cws.py. When doing this, ensure you have the required modules listed in the requirements file.
Scales on interactive plots can be changed by double clicking on the lower/upper limit values.
