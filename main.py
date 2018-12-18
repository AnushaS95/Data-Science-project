import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import sqlite3

def user_interest_matrix():
    df = pd.read_csv('user_interests.csv')
    df = df.drop_duplicates(subset=['user_handle','interest_tag'], keep="first")
    df = df.groupby(['user_handle', 'interest_tag']).size().unstack(fill_value=0).reset_index()
    return df

def user_author_matrix():
    df = pd.read_csv('user_course_views.csv')
    df = df.drop_duplicates(subset=['user_handle','author_handle'], keep="first")
    df = df.groupby(['user_handle','author_handle']).size().unstack(fill_value=0).reset_index()
    return df

def user_course_matrix():
    df = pd.read_csv("user_course_views.csv")
    df = df.drop_duplicates(subset=['user_handle','course_id'],keep="first")
    df = df.groupby(['user_handle','course_id']).size().unstack(fill_value=0).reset_index()
    return df   

interests = user_interest_matrix()
interests = interests.set_index('user_handle')
authors = user_author_matrix()
authors = authors.set_index('user_handle')
courses = user_course_matrix()
courses = courses.set_index('user_handle')

result =  pd.concat([interests, authors, courses], axis=1)
result = result.fillna(0)

print result.head()