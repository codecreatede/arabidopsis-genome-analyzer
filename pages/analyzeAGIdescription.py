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

st.markdown('<div style="text-align: justify;"> this provides the Go information for the AGI ids presented in a file and presents them as tuples with the AGI at index 0 anthe Description associated with the gene at index 1. This takes the gene_association.tair as the association file.</div>',
unsafe_allow_html=True)

idsfile = st.text_input("Please provide the path to the ids files:")
associationfile = st.text_input("Please provide the path to the association
file")

idsfile and associationfile and st.button("Analyze AGIdescription"):
  with open(os.path.abspath(os.path.join(os.getcwd(),association_file), "r")) as goslim:
    with open(os.path.abspath(os.path.join(os.getcwd(),association_file + "name"), "w")) as gofinal:
        for line in goslim.readlines():
          if line.startswith("!"):
            continue
          gofinal.write(line)
  agi_ids = []
  with open(os.path.abspath(os.path.join(os.getcwd(), ids_file)), "r") as ids:
    for line in ids.readlines():
        agi_ids.append(line.strip())
    final_ids = [i.split(".")[0] for i in [i.upper() for i in agi_ids if i!= ""]]
    go_data = pd.read_csv(os.path.join(os.getcwd(),association_file + "name"), sep = "\t")
    AGI = go_data.iloc[::,1].to_list()
    description = go_data.iloc[::,10].to_list()
    analyzedgo = set([j for i in final_ids for j in ([(i,j) for i,j in
zip(AGI,description)]) if j[0] == i])
    st.write(analyzedgo)
