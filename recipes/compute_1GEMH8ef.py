# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
pdf_topics = dataiku.Dataset("PDF_topics")
pdf_topics_df = pdf_topics.get_dataframe()




# Write recipe outputs
pdf_topics_text = dataiku.Folder("1GEMH8ef")
pdf_topics_text_info = pdf_topics_text.get_info()
