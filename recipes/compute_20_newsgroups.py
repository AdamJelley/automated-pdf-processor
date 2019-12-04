# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from sklearn.datasets import fetch_20newsgroups


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

20_newsgroups_df = ... # Compute a Pandas dataframe to write into 20_newsgroups


# Write recipe outputs
20_newsgroups = dataiku.Dataset("20_newsgroups")
20_newsgroups.write_with_schema(20_newsgroups_df)
