import streamlit as st
import pandas as pd
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key = os.getenv("gemini_api_key"))
df = pd.read_csv("mock_films.csv")
# --- Load your data ---
def select_movie(user_input):
    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=f"Given this mood{user_input}, please suggest 5 movies in this list and motivate your choice. List  of movies{df.to_string()}. Please provide a short description of the movie. ALWAYS return the shelf of the movie.",
    )

    return response.text
  # Your CSV should have one column: 'Title'

st.title("🎲 Movie Picker")

st.write("Not sure what to watch tonight? Let's pick one for you!")

# --- Ask the user (optional input for fun) ---
user_input = st.text_input("What kind of movie are you in the mood for? (optional)")

# --- Pick a random movie when the button is pressed ---
if st.button("Pick a Movie!"):
    if df.empty:
        st.error("Your CSV file seems empty 😢")
    else:
        selected_movie = select_movie(user_input)
        st.success(f"🎥 {selected_movie}")
