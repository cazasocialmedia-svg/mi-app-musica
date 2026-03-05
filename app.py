import streamlit as st
import random

st.set_page_config(page_title="Music Discovery", layout="centered")

# --- 1. ENTRADA (Tu dibujo del MOOD) ---
st.title("🎧 MOOD")
yt_link = st.text_input("YouTube Link", placeholder="Pega el link base aquí...")

if yt_link:
    st.subheader("Reproduciendo tu base:")
    st.video(yt_link)
    st.divider()

    # --- 2. GENERADOR DE RECOMENDACIONES ---
    st.header("✨ Recomendación para ti")
    
    # Lista de prueba (Esto lo conectaremos a la API luego para que sea real)
    demo_recs = [
        {"titulo": "Sugerencia 1 (Rock)", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"},
        {"titulo": "Sugerencia 2 (Pop)", "url": "https://www.youtube.com/watch?v=kJQP7kiw5Fk"}
    ]

    # Elegimos una al azar para mostrar
    if 'current_rec' not in st.session_state:
        st.session_state.current_rec = random.choice(demo_recs)

    st.write(f"**Escucha esto:** {st.session_state.current_rec['titulo']}")
    st.video(st.session_state.current_rec['url'])

    # --- 3. ACCIONES (Tus botones de Playlist) ---
    st.write("¿Qué quieres hacer con esta canción?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("✅ Guardar", use_container_width=True):
            st.success("¡Guardada en tu Playlist!")
            # Aquí se guardaría en tu lista personal
            
    with col2:
        if st.button("❌ Descartar", use_container_width=True):
            st.warning("Descartada")
            # Forzamos una nueva recomendación
            st.session_state.current_rec = random.choice(demo_recs)
            st.rerun()

    with col3:
        if st.button("🔄 Nueva", use_container_width=True):
            st.session_state.current_rec = random.choice(demo_recs)
            st.rerun()

    st.divider()
    # --- 4. TUS PLAYLISTS (Donde se van acumulando) ---
    st.subheader("📁 Mis Playlists")
    st.write("Aquí aparecerán las carpetas (Rock, World, Pop, etc.) con lo que guardes.")
