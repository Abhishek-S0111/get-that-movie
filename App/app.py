import streamlit as st
from recommender import get_recommendations

movie = st.text_input('Enter a movie name: ')
if movie:
    recommendations = get_recommendations(movie)
    st.write(f"Five Movies Similar to '{movie}' are :/n")
    for movie in recommendations:
        st.write('- ', movie)