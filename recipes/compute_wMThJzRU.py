# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import os
import sys
from pdf2image import convert_from_path

# Read recipe inputs
pdf_Input = dataiku.Folder("odbId")
pdf_Input_info = pdf_Input.get_info()
input_path = pdf_Input.get_path()

examplePDF_path = os.path.join(input_path, 'Dataiku_Overview.pdf')

# Write recipe outputs
pdf_Images = dataiku.Folder("wMThJzRU")
pdf_Images_info = pdf_Images.get_info()
pdf_Images_path = pdf_Images.get_path()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
examplePDF_image = convert_from_path(examplePDF_path,fmt='jpg',output_folder=pdf_Images_path)