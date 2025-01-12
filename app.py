import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzN2Y2MWQ3NzA2N2FiNzE3M2YxMTFiMjJlMGZhMDNmYiIsIm5iZiI6MTczNjQzOTcwNC41OTAwMDAyLCJzdWIiOiI2NzdmZjc5ODIxOGZkNTdhY2Y0ZThkYTUiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0._DN-X1S_68b8PQej4qIEzcboK_IJDRRsHP7bttMF2eo"
    }
    response = requests.get(url.format(movie_id), headers=headers)
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        # print(i[0])   it returns the index of similar movies
        recommended_movies.append(movies.iloc[i[0]].title)
        #fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


movies=pickle.load(open('movies.pkl','rb'))

similarity=pickle.load(open('similarity.pkl','rb'))

movies_title=movies['title'].values

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
"How would you like to be contacted?",
movies_title)

if st.button("Recommend"):
    names , posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])