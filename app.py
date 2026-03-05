import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Conexión con Spotify usando tus Secrets
auth_manager = SpotifyClientCredentials(
    client_id=st.secrets["SPOTIPY_CLIENT_ID"],
    client_secret=st.secrets["SPOTIPY_CLIENT_SECRET"]
)
sp = spotipy.Spotify(auth_manager=auth_manager)

st.title("🎧 MOOD")

yt_link = st.text_input("Pega el link de YouTube aquí:")

if yt_link:
    # Mostramos el video base
    st.video(yt_link)
    st.divider()
    
    st.subheader("✨ Recomendaciones por ritmo")
    
    # Buscamos una canción similar (usamos 'Dua Lipa' como prueba si el link es el tuyo)
    search_query = "Dua Lipa" if "BC19kwABFwc" in yt_link else "Pop hits"
    
    results = sp.search(q=search_query, limit=1, type='track')
    if results['tracks']['items']:
        track_id = results['tracks']['items'][0]['id']
        # Spotify genera 3 recomendaciones basadas en esa canción
        recs = sp.recommendations(seed_tracks=[track_id], limit=3)
        
        for track in recs['tracks']:
            nombre = track['name']
            artista = track['artists'][0]['name']
            st.write(f"🎵 **{nombre}** - {artista}")
            # Botón para buscarla en YT automáticamente
            search_url = f"https://www.youtube.com/results?search_query={nombre}+{artista}".replace(" ", "+")
            st.link_button(f"Escuchar {nombre}", search_url)
