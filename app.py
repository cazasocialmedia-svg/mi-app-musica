import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# 1. Conexión segura con tus llaves
try:
    auth_manager = SpotifyClientCredentials(
        client_id=st.secrets["SPOTIPY_CLIENT_ID"],
        client_secret=st.secrets["SPOTIPY_CLIENT_SECRET"]
    )
    sp = spotipy.Spotify(auth_manager=auth_manager)
except Exception as e:
    st.error("Error en las llaves de Spotify. Revisa tus Secrets.")

st.title("🎧 MOOD")

yt_link = st.text_input("Pega el link de YouTube aquí:")

if yt_link:
    # Pestañas para que se vea ordenado en el celular
    tab1, tab2 = st.tabs(["🎵 Mi Base", "✨ Sugerencias"])
    
    with tab1:
        st.video(yt_link)
    
    with tab2:
        st.subheader("Recomendaciones por ritmo")
        try:
            # Buscamos 'Dua Lipa' por defecto para probar la conexión
            results = sp.search(q="Dua Lipa", limit=1, type='track')
            
            if results['tracks']['items']:
                track = results['tracks']['items'][0]
                track_id = track['id']
                
                # Pedimos recomendaciones basadas en ese ID
                recs = sp.recommendations(seed_tracks=[track_id], limit=3)
                
                for r in recs['tracks']:
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.write(f"👉 **{r['name']}** - {r['artists'][0]['name']}")
                    with col2:
                        # Botón que busca la canción en YouTube
                        busca_yt = f"https://www.youtube.com/results?search_query={r['name']}+{r['artists'][0]['name']}".replace(" ", "+")
                        st.link_button("Ir", busca_yt)
            else:
                st.warning("No encontré canciones similares ahora mismo.")
                
        except Exception as e:
            st.error("Spotify está tardando en responder. Intenta refrescar la app.")

    # El botón de guardar que dibujaste en la pizarra
    with st.expander("📁 Guardar en mis Playlists"):
        c1, c2, c3 = st.columns(3)
        c1.button("🎸 Rock")
        c2.button("🍿 Pop")
        c3.button("🌍 World")

