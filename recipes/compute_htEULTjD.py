# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import os

# Read recipe inputs
pdf_topics = dataiku.Dataset("PDF_topics")
pdf_topics_df = pdf_topics.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
outputText = pdf_topics_df['text_summary'][0]

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
pdf_topics_text = dataiku.Folder("htEULTjD")
pdf_topics_text_info = pdf_topics_text.get_info()
pdf_topics_path = pdf_topics_text.get_path()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
with open(os.path.join(pdf_topics_path,"PDF_summary.txt"), 'w') as text_file:
    text_file.write(outputText)