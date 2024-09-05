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

st.markdown('<div style="text-align: justify;">  this establishes the missing link between the tair and the pubmed, given the file ATH_GO_GOSLIM.txt and an output file name and the specific locus or the gene id, it will first fetch the corresponding pubmed id and then will fetch the corresponding abstract for those pubmed id. Establishes a connecting link between the gene and locus to language model training.</div>',
unsafe_allow_html=True)

input = st.text_input("Please provide the path to the ids files:")
output = st.text_input("Please provide the path to the association
file")
arg_id = st.text_input("Please enter the arg_id")

if idsfile and associationfile and st.button("Analyze Literature"):
    with open(input, "r") as file_read:
        with open(output, "w") as file_out:
            for line in file_read.readlines():
                if line.startswith("!"):
                    continue
                file_out.write(line)
    with open(output, "r") as file_re_read:
        read_file = pd.read_csv(output, sep = "\t")
        correspondence = read_file.iloc[::,[1,12]].iloc[::,1]. \
                           apply(lambda n: n.split("|")).to_list()
        gene_id = list(map(lambda n: n.replace("gene:", ""), \
                            map(lambda n: n.replace("locus:", ""), \
                                         read_file.iloc[::,1].to_list())))
    pubmed = []
    for i in range(len(correspondence)):
        pubmed.append([gene_id[i],correspondence[i]])
    format_id = set([j.replace("PMID:", "") for i in ([i.split() \
                    for i in ([j for i in [pubmed[i][1] for i \
                                in range(len(pubmed)) if pubmed[i][0] == arg_id] \
                                          for j in i]) if "PMID" in i]) for j in i])
    format_id_links = list(format_id)
    format_check = []
    for i in range(len(format_id_links)):
        format_check.append(f"https://pubmed.ncbi.nlm.nih.gov/{format_id_links[i]}/")
    ncbi_derive_information = {}
    for i in range(len(format_check)):
        ncbi_derive_information[format_check[i]] = ''.join([i.get_text().strip() \
            for i in BeautifulSoup(urlopen(format_check[i]), \
                "html.parser").find_all("div", class_ = "abstract-content selected")])
    literature = [(k,v) for k,v in ncbi_derive_information.items() if k or v != ""]
    st.write(literature)
