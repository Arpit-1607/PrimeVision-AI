import streamlit as st
import plotly.express as px
from recommendation_engine import recommend_movies

# Page Configuration
st.set_page_config(
    page_title="PrimeVision AI",
    page_icon="🎬",
    layout="wide"
)

# CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

local_css("style.css")

# Header
st.title("🎬 PrimeVision AI")
st.subheader("Amazon Prime Inspired AI Movie Recommendation System")

# Search Bar
search_query = st.text_input(
    "🔍 Search Genres"
)

# Genre Buttons
st.subheader("Choose Genres")

col1, col2, col3, col4 = st.columns(4)

with col1:
    action = st.checkbox("🎬 Action")
    comedy = st.checkbox("😂 Comedy")

with col2:
    scifi = st.checkbox("🚀 Sci-Fi")
    romance = st.checkbox("❤️ Romance")

with col3:
    adventure = st.checkbox("🏔 Adventure")
    thriller = st.checkbox("🔥 Thriller")

with col4:
    horror = st.checkbox("😱 Horror")
    drama = st.checkbox("🎭 Drama")

# Recommend Button
if st.button("Recommend Movies"):

    selected_genres = []

    if action:
        selected_genres.append("Action")

    if comedy:
        selected_genres.append("Comedy")

    if scifi:
        selected_genres.append("Sci-Fi")

    if romance:
        selected_genres.append("Romance")

    if adventure:
        selected_genres.append("Adventure")

    if thriller:
        selected_genres.append("Thriller")

    if horror:
        selected_genres.append("Horror")

    if drama:
        selected_genres.append("Drama")

    if search_query:
        selected_genres.append(search_query)

    user_input = " ".join(selected_genres)

    recommendations = recommend_movies(user_input)

    st.header("🔥 Top Picks For You")

    for index, row in recommendations.iterrows():

        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(
                row["PosterURL"],
                width=150
            )

        with col2:

            st.markdown(
                f"""
<div class="movie-card">

<h3>{row['Title']}</h3>

⭐ Rating : {row['Rating']}

<br><br>

🎭 Genre : {row['Genre']}

<br><br>

🟢 Match Score : {row['Match Score']:.1f}%

</div>
""",
                unsafe_allow_html=True
            )

            st.info(
                "Recommended because of similar genres."
            )

    # Graph
    fig = px.bar(
        recommendations,
        x="Title",
        y="Match Score",
        color="Match Score",
        title="Recommendation Scores"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )