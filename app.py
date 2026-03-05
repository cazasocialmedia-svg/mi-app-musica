import streamlit as st

# Configuración para celular
st.set_page_config(page_title="My Music App", layout="centered")

# --- SECCIÓN MOOD (Tu boceto 2) ---
st.title("🎧 MOOD")
yt_link = st.text_input("YouTube Link", placeholder="Pega el link aquí...")

if yt_link:
    st.video(yt_link) # Reproductor funcional
    st.divider()

    # --- SECCIÓN PLAYLIST (Tu boceto 1) ---
    st.header("Playlist")
    
    # Creamos botones grandes fáciles de tocar en el celular
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎸 Rock", use_container_width=True):
            st.success("Guardado en Rock")
        if st.button("🌍 World", use_container_width=True):
            st.success("Guardado en World")
            
    with col2:
        if st.button("🍿 Pop", use_container_width=True):
            st.success("Guardado en Pop")
        if st.button("➕ Etc", use_container_width=True):
            st.info("Añadido a 'Etc'")

    if st.button("🔄 Actualizar Recomendaciones", type="primary", use_container_width=True):
        st.write("Buscando música similar basada en el ritmo...")
