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

st.markdown('<div style="text-align: justify;"> this functions takes a gff file and a specific type and returns the coordinates of those ids including the splice variants.</div>',unsafe_allow_html=True)

idsfile = st.text_input("Please provide the path to the ids files:")
associationfile = st.text_input("Please provide the path to the association
file")

if idsfile and associationfile and st.button("Analyze GFF"):

  if ids_file and gff_file and gene_type == "gene":
        tair = pd.read_csv(gff_file, sep = "\t")
        renaming_tair = tair.rename(columns={"Chr1":"Chromosome", "chromosome": "gene_type", "1": \
                            "Start", "30427671": "End", "..1": "Strand", "ID=Chr1;Name=Chr1":"Gene_ID"})
        gene_type = renaming_tair[["gene_type", "Start", "End"]].where(renaming_tair["gene_type"] == "gene").dropna()
        gene_type_start = list(map(int,renaming_tair[["gene_type", "Start", "End"]].where(renaming_tair["gene_type"] \
                                                                                    == "gene").dropna()["Start"].to_list()))
        gene_type_end = list(map(int,renaming_tair[["gene_type", "Start", "End"]].where(renaming_tair["gene_type"] == \
                                                                                    "gene").dropna()["End"].to_list()))
        gene_type_strand = list(map(lambda n: 1 if n == "+" else -1,renaming_tair[["gene_type", "Start", "End", "Strand"]].
                                           where(renaming_tair["gene_type"] == "gene").dropna()["Strand"].to_list()))
        gene_type_gene_ID = pd.DataFrame(renaming_tair[["gene_type", "Start", "End","Gene_ID"]].where(renaming_tair["gene_type"] == "gene").dropna()
                                      ["Gene_ID"].apply(lambda n : n.split(";")[0]).apply(lambda n : n.split(".")[0]) \
                                          .apply(lambda n: n.replace("Parent=", "")).apply(lambda n: n.replace("ID=", "")))
        gene_type_gene_ID_AGI = pd.DataFrame(renaming_tair[["gene_type", "Start", "End","Gene_ID"]]. \
                                     where(renaming_tair["gene_type"] == "gene").dropna() \
                                      ["Gene_ID"].apply(lambda n : n.split(";")[0]).apply(lambda n : n.split(".")[0]) \
                                          .apply(lambda n: n.replace("Parent=", "")).apply(lambda n: \
                                                               n.replace("ID=", "")))["Gene_ID"].to_list()
        arabidopsis_gene = []
        for i in range(len(gene_type_start)):
            arabidopsis_gene.append([gene_type_gene_ID_AGI[i],gene_type_start[i], gene_type_end[i], gene_type_strand[i]])
        agi_ids = []
        final_ids = []
        with open(os.path.abspath(os.path.join(os.getcwd(), ids_file)), "r") as ids:
            for line in ids.readlines():
                agi_ids.append(line.strip())
        final_ids = [i.upper() for i in agi_ids if i!= ""]
        selected_gene = [i for i in arabidopsis_gene for j in final_ids if j in i[0]]
        return selected_gene
  if ids_file and gff_file and gene_type == "exon":
        tair = pd.read_csv(gff_file, sep = "\t")
        renaming_tair = tair.rename(columns={"Chr1":"Chromosome", "chromosome": "gene_type", "1": \
                            "Start", "30427671": "End", "..1": "Strand", "ID=Chr1;Name=Chr1":"Gene_ID"})
        exon_type = renaming_tair[["gene_type", "Start", "End"]].where(renaming_tair["gene_type"] == "exon").dropna()
        exon_type_start = list(map(int,renaming_tair[["gene_type", "Start", "End"]].where(renaming_tair["gene_type"] \
                                                                                    == "exon").dropna()["Start"].to_list()))
        exon_type_end = list(map(int,renaming_tair[["gene_type", "Start", "End"]].where(renaming_tair["gene_type"] == \
                                                                                    "exon").dropna()["End"].to_list()))
        exon_type_strand = list(map(lambda n: 1 if n == "+" else -1,renaming_tair[["gene_type", "Start", "End", "Strand"]].
                                           where(renaming_tair["gene_type"] == "exon").dropna()["Strand"].to_list()))
        exon_type_exon_ID = pd.DataFrame(renaming_tair[["gene_type", "Start", "End","Gene_ID"]]. \
                                     where(renaming_tair["gene_type"] == "exon").dropna() \
                                      ["Gene_ID"].apply(lambda n: n.replace("Parent=", "")))
        exon_type_exon_ID_AGI = pd.DataFrame(renaming_tair[["gene_type", "Start", "End","Gene_ID"]]. \
                                     where(renaming_tair["gene_type"] == "exon").dropna() \
                                      ["Gene_ID"].apply(lambda n: n.replace("Parent=", "")))["Gene_ID"].to_list()
        arabidopsis_exon = []
        for i in range(len(exon_type_start)):
            arabidopsis_exon.append([exon_type_exon_ID_AGI[i], exon_type_start[i], exon_type_end[i], exon_type_strand[i]])
        agi_ids = []
        final_ids = []
        with open(os.path.abspath(os.path.join(os.getcwd(), ids_file)), "r") as ids:
            for line in ids.readlines():
                agi_ids.append(line.strip())
        final_ids = [i.upper() for i in agi_ids if i!= ""]
        selected_exon = [i for i in arabidopsis_exon for j in final_ids if j in i[0]]
        return selected_exon
  if ids_file and gff_file and gene_type == "three_prime_UTR":
        tair = pd.read_csv(gff_file, sep = "\t")
        renaming_tair = tair.rename(columns={"Chr1":"Chromosome", "chromosome": "gene_type", "1": \
                            "Start", "30427671": "End", "..1": "Strand", "ID=Chr1;Name=Chr1":"Gene_ID"})
        three_prime_UTR_type = renaming_tair[["gene_type", "Start", "End"]].where(renaming_tair["gene_type"] == "three_prime_UTR").dropna()
        three_prime_UTR_type_start = list(map(int,renaming_tair[["gene_type", "Start", "End"]].where(renaming_tair["gene_type"] \
                                                                                    == "three_prime_UTR").dropna()["Start"].to_list()))
        three_prime_UTR_type_end = list(map(int,renaming_tair[["gene_type", "Start", "End"]].where(renaming_tair["gene_type"] == \
                                                                                    "three_prime_UTR").dropna()["End"].to_list()))
        three_prime_UTR_type_strand = list(map(lambda n: 1 if n == "+" else -1,renaming_tair[["gene_type", "Start", "End", "Strand"]].
                                           where(renaming_tair["gene_type"] == "three_prime_UTR").dropna()["Strand"].to_list()))
        three_prime_UTR_type_ID = pd.DataFrame(renaming_tair[["gene_type", "Start", "End","Gene_ID"]]. \
                                     where(renaming_tair["gene_type"] == "three_prime_UTR").dropna() \
                                      ["Gene_ID"].apply(lambda n: n.replace("Parent=", "")))
        three_prime_UTR_type_ID_AGI = pd.DataFrame(renaming_tair[["gene_type", "Start", "End","Gene_ID"]]. \
                                     where(renaming_tair["gene_type"] == "three_prime_UTR").dropna() \
                                      ["Gene_ID"].apply(lambda n: n.replace("Parent=", "")))["Gene_ID"].to_list()
        arabidopsis_three_prime_UTR = []
        for i in range(len(three_prime_UTR_type_start)):
            arabidopsis_three_prime_UTR.append([three_prime_UTR_type_ID_AGI[i],\
                                                   three_prime_UTR_type_start[i],\
                                                   three_prime_UTR_type_end[i],\
                                                   three_prime_UTR_type_strand[i]])
        agi_ids = []
        final_ids = []
        with open(os.path.abspath(os.path.join(os.getcwd(), ids_file)), "r") as ids:
            for line in ids.readlines():
                agi_ids.append(line.strip())
        final_ids =[i.upper() for i in agi_ids if i!= ""]
        selected_three_prime_UTR = [i for i in arabidopsis_three_prime_UTR for j in final_ids if j in i[0]]
        return selected_three_prime_UTR
  if ids_file and gff_file and gene_type == "five_prime_UTR":
        tair = pd.read_csv(gff_file, sep = "\t")
        renaming_tair = tair.rename(columns={"Chr1":"Chromosome", "chromosome": "gene_type", "1": \
                            "Start", "30427671": "End", "..1": "Strand", "ID=Chr1;Name=Chr1":"Gene_ID"})
        five_prime_UTR_type = renaming_tair[["gene_type", "Start", "End"]].where(renaming_tair["gene_type"] == "five_prime_UTR").dropna()
        five_prime_UTR_type_start = list(map(int,renaming_tair[["gene_type", "Start", "End"]].where(renaming_tair["gene_type"] \
                                                                                    == "five_prime_UTR").dropna()["Start"].to_list()))
        five_prime_UTR_type_end = list(map(int,renaming_tair[["gene_type", "Start", "End"]].where(renaming_tair["gene_type"] == \
                                                                                    "five_prime_UTR").dropna()["End"].to_list()))
        five_prime_UTR_type_strand = list(map(lambda n: 1 if n == "+" else -1,renaming_tair[["gene_type", "Start", "End", "Strand"]].
                                           where(renaming_tair["gene_type"] == "five_prime_UTR").dropna()["Strand"].to_list()))
        five_prime_UTR_type_ID = pd.DataFrame(renaming_tair[["gene_type", "Start", "End","Gene_ID"]]. \
                                     where(renaming_tair["gene_type"] == "five_prime_UTR").dropna() \
                                      ["Gene_ID"].apply(lambda n: n.replace("Parent=", "")))
        five_prime_UTR_type_ID_AGI = pd.DataFrame(renaming_tair[["gene_type", "Start", "End","Gene_ID"]]. \
                                     where(renaming_tair["gene_type"] == "five_prime_UTR").dropna() \
                                      ["Gene_ID"].apply(lambda n: n.replace("Parent=", "")))["Gene_ID"].to_list()
        arabidopsis_five_prime_UTR = []
        for i in range(len(five_prime_UTR_type_start)):
            arabidopsis_five_prime_UTR.append([five_prime_UTR_type_ID_AGI[i],\
                                                   five_prime_UTR_type_start[i],\
                                                   five_prime_UTR_type_end[i],\
                                                   five_prime_UTR_type_strand[i]])
        agi_ids = []
        final_ids = []
        with open(os.path.abspath(os.path.join(os.getcwd(), ids_file)), "r") as ids:
            for line in ids.readlines():
                agi_ids.append(line.strip())
        final_ids =[i.upper() for i in agi_ids if i!= ""]
        selected_five_prime_UTR = [i for i in arabidopsis_five_prime_UTR for j in final_ids if j in i[0]]
        return selected_five_prime_UTR
  if ids_file and gff_file and gene_type == "cds":
        tair = pd.read_csv(gff_file, sep = "\t")
        renaming_tair = tair.rename(columns={"Chr1":"Chromosome", "chromosome": "gene_type", "1": \
                            "Start", "30427671": "End", "..1": "Strand", "ID=Chr1;Name=Chr1":"Gene_ID"})
        cds_type = renaming_tair[["gene_type", "Start", "End", "Strand"]].where(renaming_tair["gene_type"] == "CDS").dropna()
        cds_type_start = list(map(int,renaming_tair[["gene_type", "Start", "End"]].where(renaming_tair["gene_type"] \
                                                                                    == "CDS").dropna()["Start"].to_list()))
        cds_type_end = list(map(int,renaming_tair[["gene_type", "Start", "End"]].where(renaming_tair["gene_type"] == \
                                                                                    "CDS").dropna()["End"].to_list()))
        cds_type_strand = list(map(lambda n: 1 if n == "+" else -1,renaming_tair[["gene_type", "Start", "End", "Strand"]].
                                           where(renaming_tair["gene_type"] == "CDS").dropna()["Strand"].to_list()))
        cds_type_ID = pd.DataFrame(renaming_tair[["gene_type", "Start", "End","Gene_ID"]]. \
                                     where(renaming_tair["gene_type"] == "CDS").dropna() \
                                      ["Gene_ID"].apply(lambda n: n.split(",")[0]).apply(lambda n: n.replace("Parent=", "")))
        cds_type_ID_AGI = pd.DataFrame(renaming_tair[["gene_type", "Start", "End","Gene_ID"]]. \
                                     where(renaming_tair["gene_type"] == "CDS").dropna() \
                                      ["Gene_ID"].apply(lambda n: n.split(",")[0]).apply(lambda n: n.replace("Parent=", "")))["Gene_ID"].to_list()
        arabidopsis_cds = []
        for i in range(len(cds_type_start)):
            arabidopsis_cds.append([cds_type_ID_AGI[i], cds_type_start[i],cds_type_end[i], cds_type_strand[i]])
        agi_ids = []
        final_ids = []
        with open(os.path.abspath(os.path.join(os.getcwd(), ids_file)), "r") as ids:
            for line in ids.readlines():
                agi_ids.append(line.strip())
        final_ids = [i.upper() for i in agi_ids if i!= ""]
        selected_cds = [i for i in arabidopsis_cds for j in final_ids if j in i[0]]
        return selected_cds
