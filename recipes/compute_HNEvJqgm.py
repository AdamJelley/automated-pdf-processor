# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
pdf_Input = dataiku.Folder("QZb3pfTL")
pdf_Input_info = pdf_Input.get_info()




# Write recipe outputs
pdf_Images = dataiku.Folder("HNEvJqgm")
pdf_Images_info = pdf_Images.get_info()


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
pdfs = dataiku.Folder("Sz02XquZ")
pdfs_info = pdfs.get_info()


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

input_path = pdfs.get_path()

examplePDF_path = os.path.join(input_path, 'Dataiku_Overview.pdf')

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
print("Path = " + examplePDF_path)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
#pdf_processed = dataiku.Dataset("PDF_processed")
#pdf_processed.write_with_schema(pdf_processed_df)

images = dataiku.Folder("fWe0pI5t")
images_info = images.get_info()
images_path = images.get_path()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
examplePDF_image = convert_from_path(examplePDF_path,fmt='jpg',output_folder=images_path)