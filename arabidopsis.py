#! /usr/bin/env python3
# Author Gaurav Sablok
# Universitat Potsdam
# Date 2024-9-5
# multipage streamlit genome analyzer application

"""
    defining the entry point for the main streamlit application.
    The application consists of the following pages.
"""
import streamlit as st
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Genome analyzer",
    page_icon="Universitat Potsdam",
    layout="wide",
    initial_sidebar_state="expanded")
st.image("https://www.uni-potsdam.de/typo3conf/ext/up_template/Resources/Public/Images/logos/up_logo_international_2.png", width=100)
st.header("Genome analyzer Universitat Potsdam")
st.subheader(
    "Developed by Gaurav Sablok, Universitat Potsdam, Germany")

st.markdown('<div style="text-align: justify;">Welcome to the Arabidopsis Genome Analyzer. This application provides all the functional analysis for the Arabidopsis genome and for these you have the API to download the respective files on the respective pages. This allows you to perform all the analysis from the GO conversion, Uniprot analysis, literature analysis and preparing the Arabidopsis literature for the machine and deep learning approaches</div>', unsafe_allow_html=True)

components.iframe("https://www.arabidopsis.org/", height=200)

analyzeAGIdesription = st.Page("analyzeAGIdescription.py", title="Analyze Genes",
                        icon=":material/add_circle:")
analyzeAGIGO = st.Page(
    "analyzeAGIGO.py", title="Analyze Genome", icon=":material/add_circle:")
analyzeAGITAIR = st.Page(
    "analyzeAGITAIR.py", title="Analyze genome annotations", icon=":material/add_circle:")
analyzeGFF = st.Page("analyzeGFF.py", title="Analyze genome gff",
                      icon=":material/add_circle:")
analyzeuniprotAGI = st.Page(
    "analyzeuniproAGI.py", title="Analyze genome literature", icon=":material/add_circle:")
analyzeuniproTAIR = st.Page(
    "analyzeuniprotTAIR.py", title="Analyze genome vector", icon=":material/add_circle:")
analyzeTAIRNCBI = st.Page(
        "raedTAIRNCBI.py", title="Fetch NCBI Arabidopsis", icon=":material/add_circle:"
        )

pg = st.navigation([analyzeAGIdescription, analyzeAGIGO, analyzeAGITAIR, analyzeGFF, analyzeuniprotAGI, analyzeuniproTAIR, analyzeTAIRNCBI])
pg.run()
