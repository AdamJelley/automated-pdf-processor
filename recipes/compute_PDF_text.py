# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import os
import re
import nltk
#nltk.download('punkt')

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
pdfs_Processed = dataiku.Folder("w3DdXIhY")
pdfs_Processed_info = pdfs_Processed.get_info()
pdfs_Processed_path = pdfs_Processed.get_path()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Compute recipe outputs
PDF_pages_folders = os.listdir(pdfs_Processed_path)
PDF_pages__folders_paths = [os.path.join(pdfs_Processed_path, folder) for folder in PDF_pages_folders]

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
sentencesList = []

for folder_path in PDF_pages__folders_paths:
    PDF_pages = sorted(os.listdir(folder_path))
    PDF_pages_path = [os.path.join(folder_path, page) for page in PDF_pages]
    allPagestxt = ''
    for pagetxt in PDF_pages_path:
        allPagestxt += '\n' + open(pagetxt, 'r').read()
    allPagestxt_simple = re.sub(r'([a-z](?=[A-Z])|[A-Z](?=[A-Z][a-z]))', r"\1 ", allPagestxt)
    sentencesList.append(allPagestxt_simple)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
data = {'document':PDF_pages_folders, 'text':sentencesList}

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
#sentencesList = nltk.sent_tokenize(allPagestxt_simple)
df = pd.DataFrame(data)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
pdf_text_df = df # Compute a Pandas dataframe to write into PDF_text


# Write recipe outputs
pdf_text = dataiku.Dataset("PDF_text")
pdf_text.write_with_schema(pdf_text_df)