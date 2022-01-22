import pandas as pd
import streamlit as st

st.title("MusicRecom")

st.write("""
##### MusicRecom would help you to explore different songs based on your preferences

""")

st.sidebar.header("Give us some informations !")


def user_input_features():
       artist = st.sidebar.text_input("Which artist you like the most ?", "Bruno Mars")
       style = st.sidebar.text_input("Which style you want to explore ?", "Pop")
       data = {"artist":artist, 
               "style":style}
       features = pd.DataFrame(data, index=[0])
       return features


df = user_input_features()

user_preference_artist = df["artist"].item()
user_preference_style = df["style"].item()

if st.sidebar.button("Go Explore !"):
       st.subheader('We explore songs base on :')
       st.write("Artist :", user_preference_artist, "Style :", user_preference_style)
else:
       st.write("Let's Explore !")
