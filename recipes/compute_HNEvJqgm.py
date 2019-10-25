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
