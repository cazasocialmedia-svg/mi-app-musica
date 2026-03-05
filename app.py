import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Intentar conexión con Spotify
try:
    auth_manager = SpotifyClientCredentials(
        client_id=st.secrets["SPOTIPY_CLIENT_ID"],
        client_secret=st.secrets["SPOTIPY_CLIENT_SECRET"]
    )
    sp = spotipy.Spotify(auth_manager=auth_manager)
except Exception as e:
    st.error("Error crítico en las llaves de Spotify.")

st.title("🎧 MOOD")

yt_link = st.text_input("Pega el link de YouTube aquí:")

if yt_link:
    tab1, tab2 = st.tabs(["🎵 Mi Base", "✨ Sugerencias"])
    
    with tab1:
        st.video(yt_link)
    
    with tab2:
        st.subheader("Recomendaciones")
        try:
            # MÉTODO SEGURO: Buscamos tracks populares de un género
            # Esto no falla aunque no encuentre la canción de YouTube
            results = sp.recommendations(seed_genres=['pop', 'dance'], limit=3)
            
            for r in results['tracks']:
                with st.container(border=True):
                    st.write(f"👉 **{r['name']}** - {r['artists'][0]['name']}")
                    search_url = f"https://www.youtube.com/results?search_query={r['name']}+{r['artists'][0]['name']}".replace(" ", "+")
                    st.link_button("📺 Ver en YouTube", search_url)
        except:
            # Si Spotify falla, damos opciones fijas para que tu app no muera
            st.warning("Usando modo de respaldo (Spotify offline)")
            st.write("🎵 **Levitating** - Dua Lipa")
            st.link_button("Ver", "https://www.youtube.com/results?search_query=Levitating+Dua+Lipa")

