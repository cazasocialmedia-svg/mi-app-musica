import streamlit as st

st.set_page_config(page_title="Music Discovery", layout="centered")

# Estilo para que se vea más como una App de móvil
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #f0f2f6;}
    .main { background-color: #fafafa; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎧 MOOD")

# --- ENTRADA ---
yt_link = st.text_input("YouTube Link", placeholder="Pega aquí tu canción base...")

if yt_link:
    # Usamos pestañas para ahorrar espacio en el celular
    tab1, tab2 = st.tabs(["🎵 Mi Base", "✨ Sugerencia"])
    
    with tab1:
        st.video(yt_link)
        st.caption("Esta es la canción que define tu ritmo actual.")

    with tab2:
        # Aquí es donde pondremos la lógica real de búsqueda
        st.subheader("Basado en tu ritmo...")
        
        # Simulamos una búsqueda que "sí tiene que ver" (Ejemplo: Mood Chill)
        # Nota: En el siguiente paso conectaremos esto a YouTube Search real
        st.video("https://www.youtube.com/watch?v=5qap5aO4i9A") 
        
        # Botones de acción rápidos
        c1, c2 = st.columns(2)
        with c1:
            if st.button("✅ Guardar"):
                st.toast("¡Añadido a Playlist!")
        with c2:
            if st.button("⏭️ Otra"):
                st.rerun()

    # --- TUS PLAYLISTS (Abajo y discretas) ---
    with st.expander("📁 Mis Carpetas de Playlist"):
        st.write("Selecciona dónde guardar la sugerencia:")
        st.button("🎸 Rock")
        st.button("🌍 World")
        st.button("🍿 Pop")
