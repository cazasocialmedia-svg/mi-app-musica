import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Conexión limpia usando tus Secrets
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
        st.subheader("Recomendaciones por ADN Musical")
        try:
            # Forzamos una búsqueda fresca de la canción base
            # Esto 'despierta' la conexión de Spotify ahora que ya estás en User Management
            busqueda = sp.search(q="Dua Lipa Love Again", limit=1, type='track')
            
            if busqueda['tracks']['items']:
                track_id = busqueda['tracks']['items'][0]['id']
                
                # Pedimos recomendaciones reales basadas en el ID
                recs = sp.recommendations(seed_tracks=[track_id], limit=3)
                
                for r in recs['tracks']:
                    with st.container(border=True):
                        st.markdown(f"🌟 **{r['name']}**")
                        st.caption(f"De: {r['artists'][0]['name']}")
                        
                        # Link de búsqueda corregido para YouTube
                        q = f"{r['name']} {r['artists'][0]['name']}".replace(" ", "+")
                        st.link_button("📺 Ver Video", f"https://www.youtube.com/results?search_query={q}")
            else:
                st.warning("No pude encontrar la canción base para comparar.")
        except Exception as e:
            st.error("Error de sincronización. Dale al botón de 'Reboot' en Streamlit para activar tu nuevo permiso de usuario.")

with st.expander("📁 Mis Carpetas"):
    st.button("🍿 Pop")

