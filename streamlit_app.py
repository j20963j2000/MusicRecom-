import pandas as pd
import streamlit as st

st.title("MusicRecom")

st.write("""
##### MusicRecom would help you to explore different songs based on your preferences

""")

st.sidebar.header("Give us some infors !")


def user_input_features():
       artist = st.sidebar.text_input("Which artist you like the most ?", "Bruno Mars")
       data = {"artist":artist}
       features = pd.DataFrame(data, index=[0])
       return features

df = user_input_features()

user_preference_artist = df["artist"]

if df:
       st.write("We explore songs based on :", user_input_features)
