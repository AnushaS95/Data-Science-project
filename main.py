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

similarity_matrix = pd.DataFrame(cosine_similarity(result))
print similarity_matrix.head(2)

db = sqlite3.connect("similarity.db")
iterator = db.cursor()
iterator.execute("create table users (id, sim1_user, sim1_similarity, sim2_user, sim2_similarity, sim3_user, sim3_similarity, sim4_user, sim4_similarity)")

for index, row in similarity_matrix.iterrows():
   a = np.array(row)
   user_ids = a.argsort()[-5:][::-1]
   similarities = np.take(a, user_ids)
   user_ids = user_ids + 1
   print user_ids
   print similarities
   statement = "insert into users values ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8})".format(index+1, user_ids[1], similarities[1], user_ids[2], similarities[2], user_ids[3], similarities[3], user_ids[4], similarities[4])
   print statement
   iterator.execute(statement)

db.commit()