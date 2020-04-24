# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import os
import sys
from pdf2image import convert_from_path

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
pdfs = dataiku.Folder("QZb3pfTL")
pdfs_info = pdfs.get_info()

input_path = pdfs.get_path()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
images = dataiku.Folder("HNEvJqgm")
images_info = images.get_info()
images_path = images.get_path()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# If project variable is set to true, all outputs cleared and PDF processing is re-run for all input PDFs.
if dataiku.get_custom_variables()["reprocess_PDFs"].lower() == "true":
    for output_pdf_folder in os.listdir(images_path):
        output_pdf_folder_path = os.path.join(images_path, output_pdf_folder)
        for page in os.listdir(output_pdf_folder_path):
            page_path = os.path.join(output_pdf_folder_path, page)
            os.remove(page_path)
        os.rmdir(output_pdf_folder_path)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
for pdf in os.listdir(input_path):
    pdf_path = os.path.join(input_path, pdf)
    output_path = os.path.join(images_path, pdf.replace('.pdf',''))
    if os.path.exists(output_path):
        print('PDF already processed.')
    else:
        os.mkdir(output_path)
        pdf_image = convert_from_path(pdf_path,fmt='jpg',dpi=300,output_folder=output_path)