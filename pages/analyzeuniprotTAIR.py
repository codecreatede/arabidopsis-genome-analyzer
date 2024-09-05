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

st.markdown('<div style="text-align: justify;">   this takes a TAIR2Uniprot mapping and returns a nested tuple with the IDs and the Uniprot and thier locus ids.</div>',unsafe_allow_html=True)

tair_uniprot_file = st.text_input("Please provide the path to the ids files:")
ids_file = st.text_input("Please provide the path to the association
file")

if idsfile and associationfile and st.button("Analyze GO"):
    tair_uniprot = {}
    agi_ids = []
    final_ids = []
    with open(os.path.abspath(os.path.join(os.getcwd(), ids_file)), "r") as ids:
      for line in ids.readlines():
        agi_ids.append(line.strip())
        final_ids = [i.split(".")[0] for i in [i.upper() for i in agi_ids if i!= ""]]
    with open(os.path.abspath(os.path.join(os.getcwd(), tair_uniprot_file)), "r") as uni:
      for line in uni.readlines():
        tair_uniprot[line.strip().split("\t")[0]] = line.strip().split("\t")[1:]
      analyzed = [(k,v) for k,v in tair_uniprot.items() for i in final_ids if i
== v[1]]
      st.write(analyzed)
