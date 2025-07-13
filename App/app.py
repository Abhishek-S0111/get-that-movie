import streamlit as st
#from recommender import get_recommendations
import json
from pandas import read_csv

movie = st.text_input('Enter a movie name: ')

#load the precompute file
with open("precompute/movie_sims_dict.json", 'r') as f:
    map = json.load(f)

#load the movie dataset
data = read_csv("data/movie.csv")

if movie:
    st.write("Hullo!!!")
    st.write(f"Five Movies Similar to '{movie}' are :/n")
    movie_id = data[data['title'] == movie].index[0]
    similar_id = map[str(movie_id)]
    recommendations = data.iloc[similar_id]['title'].tolist()
    for rec in recommendations:
        st.write('- ', rec)