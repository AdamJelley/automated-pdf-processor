# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from sklearn.datasets import fetch_20newsgroups

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
twenty_train = fetch_20newsgroups(subset='train', shuffle=True, random_state=42)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
articles_df = pd.DataFrame(twenty_train.data, columns=['text'])
targets_df = pd.DataFrame(twenty_train.target, columns=['target'])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
assert len(articles_df) == len(targets_df), "Number of articles does not equal number of labels"
twenty_newsgroups_df = articles_df.join(targets_df, how='left')

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
twenty_newsgroups_df

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
target_names_df = pd.DataFrame(twenty_train.target_names, columns=['target_name']).reset_index().rename(columns={'index':'target'})

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

20_newsgroups_df = ... # Compute a Pandas dataframe to write into 20_newsgroups


# Write recipe outputs
20_newsgroups = dataiku.Dataset("20_newsgroups")
20_newsgroups.write_with_schema(20_newsgroups_df)