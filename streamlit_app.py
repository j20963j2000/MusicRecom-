import pandas as pd
import streamlit as st

st.title("MusicRecom")

st.write("""
##### MusicRecom would help you to explore different songs based on your preferences

""")

st.sidebar.header("Give us some informations !")


def user_input_features():
       artist = st.sidebar.text_input("Which artist you like the most ?", "Bruno Mars")
       style = st.sidebar.selectbox("Which style you want to explore ?", ("Pop", "Rock", "Metal"))
       data = {"artist":artist, 
               "style":style}
       features = pd.DataFrame(data, index=[0])
       return features


df = user_input_features()

user_preference_artist = df["artist"].item()
user_preference_style = df["style"].item()

if st.sidebar.button("Go Explore !"):
       st.subheader('We explore songs base on :')
       st.write("Artist :", user_preference_artist)
       st.write("Style :", user_preference_style)

       st.markdown("---")
       container = st.container()
       with container:
              st.markdown(
                     "This would desplay first exploring result"
              )
       
       st.markdown("---")
       container2 = st.container()       
       with container2:
              st.markdown(
                     "This would desplay second exploring result"
              )
              
       st.markdown("---")
else:
       st.write("Let's Explore !")
