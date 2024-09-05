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

st.markdown('<div style="text-align: justify;"> this function analyzes the phytozome file for the search of the corresponding pacid and provided a agi_id file, phytozome file, it will search for the corresponding pacid.</div>',
unsafe_allow_html=True)

gfffile = st.text_input("Please provide the path to the ids files:")
idsfile = st.text_input("Please provide the path to the association
file")

if idsfile and associationfile and st.button("Analyze PacID"):
    with open(os.path.abspath(os.path.join(os.getcwd(),gff_file)), "r") as phytozome:
        with open(os.path.abspath(os.path.join(os.getcwd(),gff_file + "name")), "w") as phytozomer:
            for line in phytozome.readlines():
                if line.startswith("!"):
                    continue
                phytozomer.write(line)
        phytozomedataframe = pd.read_csv(os.path.abspath(os.path.join(os.getcwd(),gff_file + "name")), sep = "\t")
        mRNA = phytozomedataframe.iloc[::,[2,8]]. \
                  where(phytozomedataframe.iloc[::,[2,8]]["gene"] == "mRNA").dropna()
        name = [i.split("=")[1] for i in ([j for i in ([i.split(";") \
                        for i in (mRNA.iloc[::,1].to_list())]) \
                                for j in i if j.startswith("Name=")])]
        pacid = [j for i in ([i.split(";") \
                          for i in (mRNA.iloc[::,1].to_list())]) \
                                    for j in i if j.startswith("pacid=")]
        agiPacID = [(i,j) for i,j in zip(name,pacid)]
        agi_ids = []
        final_ids = []
        with open(os.path.abspath(os.path.join(os.getcwd(), ids_file)), "r") as ids:
            for line in ids.readlines():
                agi_ids.append(line.strip())
            final_ids = [i.upper() for i in agi_ids if i!= ""]
            analyzedgff = [i for i in agiPacID for j in final_ids if j==i[0]]
            st.write(analyzedgff)
