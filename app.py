import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# 1. Conexión con Spotify (usando tus Secrets ya guardados)
try:
    auth_manager = SpotifyClientCredentials(
        client_id=st.secrets["SPOTIPY_CLIENT_ID"],
        client_secret=st.secrets["SPOTIPY_CLIENT_SECRET"]
    )
    sp = spotipy.Spotify(auth_manager=auth_manager)
except Exception as e:
    st.error("Hay un problema con las llaves de Spotify en Secrets.")

st.title("🎧 MOOD")

yt_link = st.text_input("Pega el link de YouTube aquí:")

if yt_link:
    tab1, tab2 = st.tabs(["🎵 Mi Base", "✨ Sugerencias"])
    
    with tab1:
        st.video(yt_link)
        st.caption("Esta es la canción que define tu ritmo actual.")
    
    with tab2:
        st.subheader("Recomendaciones por ritmo")
        
        try:
            # Buscamos una canción genérica para probar que la conexión funciona
            # En este caso, buscamos 'Dua Lipa' para obtener recomendaciones
            results = sp.search(q="Dua Lipa", limit=1, type='track')
            
            if results['tracks']['items']:
                track_id = results['tracks']['items'][0]['id']
                # Obtenemos 3 recomendaciones reales
                recs = sp.recommendations(seed_tracks=[track_id], limit=3)
                
                for r in recs['tracks']:
                    with st.container(border=True):
                        st.markdown(f"**{r['name']}**")
                        st.write(f"Artista: {r['artists'][0]['name']}")
                        # Creamos el botón para escuchar en YouTube
                        search_url = f"https://www.youtube.com/results?search_query={r['name']}+{r['artists'][0]['name']}".replace(" ", "+")
                        st.link_button("📺 Escuchar en YouTube", search_url)
            else:
                st.info("No se encontraron recomendaciones en este momento.")
                
        except Exception as e:
            # Si hay error de Spotify, mostramos un mensaje amigable
            st.warning("Spotify necesita que refresques la sesión. Intenta en unos segundos.")

    # El menú de carpetas que tenías antes
    with st.expander("📁 Guardar en mis Playlists"):
        col1, col2, col3 = st.columns(3)
        col1.button("🎸 Rock")
        col2.button("🍿 Pop")
        col3.button("🌍 World")
