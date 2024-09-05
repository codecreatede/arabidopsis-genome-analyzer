#! /usr/bin/env python3
# Author Gaurav Sablok
# Universitat Potsdam
# Date 2024-9-5
# multipage streamlit genome analyzer application


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

components.iframe("https://www.arabidopsis.org/", height=300)

st.markdown('<div style="text-align: justify;"> this functions takes as input a uniprot_agi file and a file of ids and returns the converted ids or the links between the agi and the uniprot</div>',
unsafe_allow_html=True)

agi_file = st.text_input("Please provide the path to the ids files:")
ids_file = st.text_input("Please provide the path to the association file")

if agi_file and ids_file and st.button("Analyze UniProtAGI"):

    uniprot_ag = {}
    agi_ids = []
    final_ids = []
    with open(os.path.abspath(os.path.join(os.getcwd(), ids_file)), "r") as ids:
      for line in ids.readlines():
        agi_ids.append(line.strip())
        final_ids = [i for i in agi_ids if i!= ""]
    with open(os.path.abspath(os.path.join(os.getcwd(), agi_file)), "r") as uni:
      for line in uni.readlines():
        uniprot_ag[line.strip().split("\t")[0]] = [j for i in (list(map(lambda n: n.split(";"), \
                                                                line.strip().split("\t")[1:]))) for j in i]
      analyzed = [(k,v) for k,v in uniprot_ag.items() for i in final_ids if i in v]
      st.write(analyzed)
