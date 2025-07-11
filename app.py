import streamlit as st
from recommender import get_recommendations

movie = st.text_input('Enter a movie name: ')

st.write("Brother, can i have some oats?")
# if movie:
#     recommendations = get_recommendations(movie)
#     st.write(f"Five Movies Similar to '{movie}' are :/n")
#     for rec in recommendations:
#         st.write('- ', rec)