import streamlit as st

# 1. Configuración Visual
st.set_page_config(page_title="MOOD - YouTube Edition", page_icon="🎧")

st.markdown("""
    <style>
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎧 MOOD")
st.write("Crea tu propia experiencia musical sin bloqueos.")

# 2. Entrada de Usuario
yt_link = st.text_input("Pega el link de YouTube aquí:", placeholder="https://youtu.be/...")

if yt_link:
    tab1, tab2 = st.tabs(["🎵 Mi Base", "✨ Sugerencias Directas"])
    
    with tab1:
        st.video(yt_link)
        st.caption("Tu video base está listo.")

    with tab2:
        st.subheader("Explorar música similar")
        st.write("Como Spotify está bloqueado, aquí tienes accesos directos para encontrar el mismo ritmo:")
        
        # Definimos una lista de géneros para que elijas según el video que pegues
        generos = ["Pop / Dance", "Lo-Fi / Relax", "Rock / Indie", "Reggaeton / Urbano"]
        seleccion = st.selectbox("¿Qué vibra buscas hoy?", generos)
        
        # Creamos 3 recomendaciones inteligentes basadas en el género
        # Esto simula el ADN musical de forma manual y segura
        
        col1, col2, col3 = st.columns(3)
        
        # Diccionario de sugerencias rápidas
        sug = {
            "Pop / Dance": ["Dua Lipa Mix", "Future Nostalgia Full", "Dance Pop 2026"],
            "Lo-Fi / Relax": ["Lofi Girl Live", "Chillhop Essentials", "Study Beats"],
            "Rock / Indie": ["Arctic Monkeys Radio", "Indie Rock Classics", "New Rock 2026"],
            "Reggaeton / Urbano": ["Bad Bunny Mix", "Karol G Hits", "Reggaeton Antiguo"]
        }

        for i, tema in enumerate(sug[seleccion]):
            with [col1, col2, col3][i]:
                st.markdown(f"**{tema}**")
                query = tema.replace(" ", "+")
                # Link de búsqueda directo que abre YouTube
                url = f"https://www.youtube.com/results?search_query={query}"
                st.link_button("🔍 Buscar", url)

st.divider()
with st.expander("📁 Mis Carpetas"):
    st.write("Guarda tus descubrimientos aquí.")
    st.button("➕ Crear Nueva Carpeta")
