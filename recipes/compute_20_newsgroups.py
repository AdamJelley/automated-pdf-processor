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
target_names_df = pd.DataFrame(twenty_train.target_names, columns=['target_name']).reset_index().rename(columns={'index':'target'})

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
assert len(articles_df) == len(targets_df), "Number of articles does not equal number of labels"
twenty_newsgroups_df = articles_df.join(targets_df, how='left')
twenty_newsgroups_df = twenty_newsgroups_df.merge(target_names_df, on=['target'], how='inner')

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
twenty_newsgroups = dataiku.Dataset("twenty_newsgroups")
twenty_newsgroups.write_with_schema(twenty_newsgroups_df)