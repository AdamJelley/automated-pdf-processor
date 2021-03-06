# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import os

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
pdf_topics = dataiku.Dataset("PDF_topics_category")
pdf_topics_df = pdf_topics.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
pdf_topics_text = dataiku.Folder("htEULTjD")
pdf_topics_text_info = pdf_topics_text.get_info()
pdf_topics_path = pdf_topics_text.get_path()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
for page in os.listdir(pdf_topics_path):
    page_path = os.path.join(pdf_topics_path, page)
    os.remove(page_path)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
for idx, row in pdf_topics_df.iterrows():
    with open(os.path.join(pdf_topics_path, row['document']+"_summary.txt"), 'w') as text_file:
        outputText = 'Document: '+ row['document'] + '\n\nCategory: ' + row['prediction'] +'\n\nSummary: \n\n' + row['text_summary'] + '\n\n\n\n\nFull Document: \n\n' + row['text']
        text_file.write(outputText)