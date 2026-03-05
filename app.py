import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Conexión con Spotify
auth_manager = SpotifyClientCredentials(
    client_id=st.secrets["SPOTIPY_CLIENT_ID"],
    client_secret=st.secrets["SPOTIPY_CLIENT_SECRET"]
)
sp = spotipy.Spotify(auth_manager=auth_manager)

st.title("🎧 MOOD")

yt_link = st.text_input("Pega el link de YouTube aquí:")

if yt_link:
    tab1, tab2 = st.tabs(["🎵 Mi Base", "✨ Sugerencias"])
    
    with tab1:
        st.video(yt_link)
    
    with tab2:
        st.subheader("Recomendaciones por ritmo")
        # Buscamos 'Dua Lipa' como prueba inicial para activar el motor
        results = sp.search(q="Dua Lipa", limit=1, type='track')
        
        if results['tracks']['items']:
            track_id = results['tracks']['items'][0]['id']
            # Spotify genera recomendaciones reales aquí
            recs = sp.recommendations(seed_tracks=[track_id], limit=3)
            
            for r in recs['tracks']:
                with st.container(border=True):
                    st.markdown(f"**{r['name']}**")
                    st.caption(f"{r['artists'][0]['name']}")
                    link_yt = f"https://www.youtube.com/results?search_query={r['name']}+{r['artists'][0]['name']}".replace(" ", "+")
                    st.link_button("📺 Escuchar en YouTube", link_yt)

    # Tus carpetas de playlist (Diseño de tu pizarra)
    with st.expander("📁 Guardar en mis Playlists"):
        c1, c2, c3 = st.columns(3)
        c1.button("🎸 Rock")
        c2.button("🍿 Pop")
        c3.button("🌍 World")
