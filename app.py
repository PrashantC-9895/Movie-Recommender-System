
import streamlit as st
import pickle
import pandas as pd
import requests
api_key ='01bfbf28c880c0e15b27b5d67aa46207'
def fetch_poster(movie_id):
    import requests



    #print(response.text)
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US")
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500'+data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []



    for i in movie_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)

        recommended_movies_posters.append(fetch_poster(movie_id))    #fetch poster from API

    return recommended_movies,recommended_movies_posters


movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Search for movie',
movies['title'].values)

if st.button('Recommend'):
    names,poster = recommend(selected_movie_name)


    col1, col2, col3 , col4 , col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(poster[0])

    with col2:
        st.text(names[1])
        st.image(poster[1])

    with col3:
        st.text(names[2])
        st.image(poster[2])

    with col4:
        st.text(names[3])
        st.image(poster[3])

    with col5:
        st.text(names[4])
        st.image(poster[4])