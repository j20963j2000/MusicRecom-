from PIL import Image 
import pandas as pd
import streamlit as st
from bokeh.models.widgets import Div

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
              col1, col2 = st.columns([1, 3])
              original = Image.open("images/silksonic.jpg")
              col1.image(original, use_column_width=True)

              with col2:
                     col2.write("Artist : ", "Bruno Mars")
                     col2.write("Album : ", "Leave the door open")
                     button1 = st.button("Listening on Spotify", key=0)
                     if button1:
                            js = "window.open('https://www.streamlit.io/')"  # New tab or window
                            js = "window.location.href = 'https://www.streamlit.io/'"  # Current tab
                            html = '<img src onerror="{}">'.format(js)
                            div = Div(text=html)
                            st.bokeh_chart(div)

       st.markdown("---")
       container2 = st.container()       
       with container2:
              col1, col2 = st.columns([1, 3])
              original = Image.open("images/24magics.jpg")
              col1.image(original, use_column_width=True)

              with col2:
                     col2.write("Artist : ", "Bruno Mars")
                     col2.write("Album : ", "24k Magics")
                     button2 = st.button("Listening on Spotify", key=1)
                     if button2:
                            js = "window.open('https://www.streamlit.io/')"  # New tab or window
                            js = "window.location.href = 'https://www.streamlit.io/'"  # Current tab
                            html = '<img src onerror="{}">'.format(js)
                            div = Div(text=html)
                            st.bokeh_chart(div)

       st.markdown("---")
else:
       st.write("Let's Explore !")
