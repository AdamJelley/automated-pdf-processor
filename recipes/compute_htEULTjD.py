# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import os

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
pdf_topics = dataiku.Dataset("PDF_topics_category_summary")
pdf_topics_df = pdf_topics.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
pdf_topics_text = dataiku.Folder("htEULTjD")
pdf_topics_text_info = pdf_topics_text.get_info()
pdf_topics_path = pdf_topics_text.get_path()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
outputText = pdf_topics_df['text_summary'][0]

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
with open(os.path.join(pdf_topics_path,"PDF_summary.txt"), 'w') as text_file:
    text_file.write(outputText)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
for output_pdf_folder in os.listdir(pdf_topics_path):
    output_pdf_folder_path = os.path.join(pdf_topics_path, output_pdf_folder)
    for page in os.listdir(output_pdf_folder_path):
        page_path = os.path.join(output_pdf_folder_path, page)
        os.remove(page_path)
    os.rmdir(output_pdf_folder_path)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
for idx, row in pdf_topics_df.iterrows():
    document_folder_path = os.path.join(pdf_topics_path, row['document'])
    os.mkdir(document_folder_path)

    with open(os.path.join(document_folder_path,"PDF_summary.txt"), 'w') as text_file:
        outputText = 'Document: '+ row['document'] + '\n\nCategory:' + row['target_name'] +'\n\nSummary: \n\n' + row['text_summary'] + '\n\n\nFull Document: \n\n' + row['text']
        print(outputText)