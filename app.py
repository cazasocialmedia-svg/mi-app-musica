import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# 1. Conexión
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
            # PASO A: Buscamos "Dua Lipa Love Again" en Spotify para tener la base
            # (En el futuro esto puede ser automático, por ahora fijamos la base)
            base_search = sp.search(q="Dua Lipa Love Again", limit=1, type='track')
            
            if base_search['tracks']['items']:
                track = base_search['tracks']['items'][0]
                track_id = track['id']
                
                # PASO B: Spotify analiza el ritmo y nos da algo similar
                recs = sp.recommendations(seed_tracks=[track_id], limit=3)
                
                for r in recs['tracks']:
                    with st.container(border=True):
                        st.markdown(f"🌟 **{r['name']}**")
                        st.caption(f"De: {r['artists'][0]['name']}")
                        
                        # Link de YouTube corregido
                        q = f"{r['name']} {r['artists'][0]['name']}".replace(" ", "+")
                        st.link_button("📺 Ver Video", f"https://www.youtube.com/results?search_query={q}")
            else:
                st.warning("No pude encontrar la canción base en Spotify.")
        except:
            st.error("Spotify bloqueó la búsqueda. Revisa el User Management.")

st.divider()
with st.expander("📁 Mis Carpetas"):
    c1, c2, c3 = st.columns(3)
    c1.button("🎸 Rock")
    c2.button("🍿 Pop")
    c3.button("🌍 World")
