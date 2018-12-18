import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import sqlite3

def user_interest_matrix():
    df = pd.read_csv('user_interests.csv')
    df = df.drop_duplicates(subset=['user_handle','interest_tag'], keep="first")
    df = df.groupby(['user_handle', 'interest_tag']).size().unstack(fill_value=0).reset_index()
    return df

interests = user_interest_matrix()
interests = interests.set_index('user_handle')

print interests