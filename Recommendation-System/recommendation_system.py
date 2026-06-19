import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = {
    'title': [
        'Avatar',
        'Titanic',
        'Avengers Endgame',
        'Iron Man',
        'The Dark Knight',
        'Interstellar',
        'Inception',
        'Doctor Strange'
    ],
    'genre': [
        'Action Adventure Sci-Fi',
        'Romance Drama',
        'Action Superhero',
        'Action Superhero',
        'Action Crime Drama',
        'Sci-Fi Adventure',
        'Sci-Fi Thriller',
        'Action Fantasy'
    ]
}

df = pd.DataFrame(movies)

vectorizer = TfidfVectorizer()
genre_matrix = vectorizer.fit_transform(df['genre'])

similarity = cosine_similarity(genre_matrix)

def recommend(movie_name):
    movie_name = movie_name.strip()

    if movie_name not in df['title'].values:
        print("Movie not found.")
        return

    index = df[df['title'] == movie_name].index[0]

    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("\nRecommended Movies:")

    count = 0
    for movie in scores[1:]:
        print(df.iloc[movie[0]]['title'])
        count += 1
        if count == 3:
            break

movie = input("Enter a movie name: ")
recommend(movie)