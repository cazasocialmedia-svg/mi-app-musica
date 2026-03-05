import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Forzamos una nueva conexión limpia en cada ejecución
@st.cache_resource
def conectar_spotify():
    return spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=st.secrets["SPOTIPY_CLIENT_ID"],
        client_secret=st.secrets["SPOTIPY_CLIENT_SECRET"]
    ))

sp = conectar_spotify()

st.title("🎧 MOOD")

yt_link = st.text_input("Pega el link de YouTube aquí:")

if yt_link:
    tab1, tab2 = st.tabs(["🎵 Mi Base", "✨ Sugerencias"])
    
    with tab1:
        st.video(yt_link)
    
    with tab2:
        st.subheader("Recomendaciones por ADN Musical")
        try:
            # Buscamos una canción de Dua Lipa para arrancar el motor
            busqueda = sp.search(q="Dua Lipa Love Again", limit=1, type='track')
            
            if busqueda['tracks']['items']:
                track_id = busqueda['tracks']['items'][0]['id']
                recs = sp.recommendations(seed_tracks=[track_id], limit=3)
                
                for r in recs['tracks']:
                    with st.container(border=True):
                        st.markdown(f"🌟 **{r['name']}**")
                        st.caption(f"De: {r['artists'][0]['name']}")
                        q = f"{r['name']} {r['artists'][0]['name']}".replace(" ", "+")
                        st.link_button("📺 Ver Video", f"https://www.youtube.com/results?search_query={q}")
            else:
                st.warning("Conectado a Spotify, pero no encontré la canción base.")
        except Exception as e:
            st.error(f"Error de acceso. Spotify dice que no tienes permiso. Verifica que tu correo en el Dashboard esté como 'Accepted'.")

with st.expander("📁 Mis Carpetas"):
    st.button("🍿 Pop")
