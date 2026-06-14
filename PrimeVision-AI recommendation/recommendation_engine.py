import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recommend_movies(user_input):

    df = pd.read_csv("data/movies.csv")

    genres = df["Genre"].tolist()

    genres.append(user_input)

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(genres)

    similarity_scores = cosine_similarity(
        tfidf_matrix[-1],
        tfidf_matrix[:-1]
    )

    df["Match Score"] = similarity_scores.flatten() * 100

    recommendations = df.sort_values(
        by="Match Score",
        ascending=False
    )

    return recommendations.head(10)