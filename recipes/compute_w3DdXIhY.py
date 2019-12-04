# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from PIL import Image
import os
import pytesseract

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
images = dataiku.Folder("HNEvJqgm")
images_info = images.get_info()
images_folder_path = images.get_path()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
pdfs_processed = dataiku.Folder("w3DdXIhY")
pdfs_processed_info = pdfs_processed.get_info()
pdfs_folder_path = pdfs_processed.get_path()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
os.listdir(pdfs_folder_path)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
for output_pdf_folder in os.listdir(pdfs_folder_path):
    os.rmdir(os.path.join(pdfs_folder_path, output_pdf_folder))

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
for pdf_folder in os.listdir(images_folder_path):
    PDF_pages = sorted(os.listdir(os.path.join(images_folder_path, pdf_folder)))
    PDF_pages_path = [os.path.join(images_folder_path, pdf_folder) for pdf_folder in PDF_pages]

    pdfs_processed_path = os.path.join(pdfs_folder_path, pdf_folder)
    os.mkdir(pdfs_processed_path)

    for i, page_path in enumerate(os.listdir(pdfs_processed_path)):
        print(PDF_pages_path)
        output_path = os.path.join(pdfs_processed_path, 'page_'+"{0:0=2d}".format(i+1)+'.txt')
        pdf_text = pytesseract.image_to_string(Image.open(page_path))
        with open(output_path, "w") as f:
            f.write(pdf_text)
            f.close()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

PDF_pages = sorted(os.listdir(images_path))
PDF_pages_path = [os.path.join(images_path, page) for page in PDF_pages]

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
for i, page_path in enumerate(PDF_pages_path):
    output_path = os.path.join(pdfs_processed_path, 'page_'+"{0:0=2d}".format(i+1)+'.txt')
    pdf_text = pytesseract.image_to_string(Image.open(page_path))
    with open(output_path, "w") as f:
        f.write(pdf_text)
        f.close()