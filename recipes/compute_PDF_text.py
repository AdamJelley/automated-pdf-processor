# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
pdfs_Processed = dataiku.Folder("w3DdXIhY")
pdfs_Processed_info = pdfs_Processed.get_info()
pdfs_Processed_path = pdfs_Processed.get_path()

# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

PDF_pages = sorted(os.listdir(pdfs_Processed_path))
PDF_pages_path = [os.path.join(pdfs_Processed_path, page) for page in PDF_pages]

pdf_text_df = ... # Compute a Pandas dataframe to write into PDF_text


# Write recipe outputs
pdf_text = dataiku.Dataset("PDF_text")
pdf_text.write_with_schema(pdf_text_df)
