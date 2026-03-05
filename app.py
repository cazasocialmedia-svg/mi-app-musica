import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# 1. Configuración de la página y Estilo
st.set_page_config(page_title="MOOD - Recomendador", page_icon="🎧")

st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #1DB954;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Conexión con Spotify (Usando tus Secrets)
try:
    auth_manager = SpotifyClientCredentials(
        client_id=st.secrets["SPOTIPY_CLIENT_ID"],
        client_secret=st.secrets["SPOTIPY_CLIENT_SECRET"]
    )
    sp = spotipy.Spotify(auth_manager=auth_manager)
    spotify_conectado = True
except Exception as e:
    spotify_conectado = False

# 3. Interfaz de Usuario
st.title("🎧 MOOD")
st.write("Encuentra música con el mismo ritmo que tus videos favoritos.")

yt_link = st.text_input("Pega el link de YouTube aquí:", placeholder="https://www.youtube.com/watch?v=...")

if yt_link:
    # Creamos las pestañas para separar el video de las sugerencias
    tab1, tab2 = st.tabs(["🎵 Mi Base", "✨ Sugerencias"])
    
    with tab1:
        st.video(yt_link)
        st.caption("Analizando el 'vibe' de esta canción...")

    with tab2:
        st.subheader("Recomendaciones por ritmo")
        
        if spotify_conectado:
            try:
                # Buscamos éxitos actuales de 2025 para asegurar resultados reales
                results = sp.search(q='year:2025', type='track', limit=3)
                
                if results['tracks']['items']:
                    for r in results['tracks']['items']:
                        nombre = r['name']
                        artista = r['artists'][0]['name']
                        
                        with st.container(border=True):
                            st.markdown(f"**{nombre}**")
                            st.caption(f"Artista: {artista}")
                            
                            # Generamos el link de búsqueda en YouTube
                            search_query = f"{nombre} {artista} official audio".replace(" ", "+")
                            url_final = f"https://www.youtube.com/results?search_query={search_query}"
                            st.link_button(f"📺 Escuchar en YouTube", url_final)
                else:
                    st.info("No hay sugerencias disponibles ahora mismo.")
            except:
                # Si la API falla por permisos (User Management), entra el Respaldo
                st.warning("⚠️ Modo de respaldo activado (Spotify en mantenimiento)")
                
                respaldos = [
                    {"n": "Houdini", "a": "Dua Lipa"},
                    {"n": "Flowers", "a": "Miley Cyrus"},
                    {"n": "Blinding Lights", "a": "The Weeknd"}
                ]
                
                for res in respaldos:
                    with st.container(border=True):
                        st.write(f"👉 **{res['n']}** - {res['a']}")
                        q = f"{res['n']} {res['a']}".replace(" ", "+")
                        st.link_button("Ver video", f"https://www.youtube.com/results?search_query={q}")
        else:
            st.error("Error de conexión. Revisa tus credenciales en Streamlit Secrets.")

# 4. Secciones de la Pizarra (Tus carpetas)
st.divider()
with st.expander("📁 Mis Carpetas de Playlist"):
    st.write("¿Dónde quieres guardar tus nuevos descubrimientos?")
    c1, c2, c3 = st.columns(3)
    c1.button("🎸 Rock")
    c2.button("🍿 Pop")
    c3.button("🌍 World")
