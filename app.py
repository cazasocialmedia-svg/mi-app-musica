import streamlit as st
import random

st.set_page_config(page_title="My Music App", layout="centered")

st.title("🎧 MOOD")
yt_link = st.text_input("YouTube Link", placeholder="Pega el link aquí...")

# Base de datos simulada (Luego la conectaremos a una real)
generos = {
    "Rock": ["https://www.youtube.com/watch?v=v2AC41dglnM", "https://www.youtube.com/watch?v=Pb9pS2pA7-U"],
    "Pop": ["https://www.youtube.com/watch?v=JGwWNGJdvx8", "https://www.youtube.com/watch?v=09R8_2nJtjg"],
    "World": ["https://www.youtube.com/watch?v=6mYw5D_XfZA", "https://www.youtube.com/watch?v=v7K4vT6S678"]
}

if yt_link:
    st.video(yt_link)
    st.divider()
    
    st.header("Playlist & Recomendaciones")
    st.write("¿Te gusta este ritmo? Guarda o busca más:")
    
    col1, col2 = st.columns(2)
    
    # Lógica de los botones que dibujaste
    with col1:
        if st.button("🎸 Guardar en Rock", use_container_width=True):
            st.success("¡Añadido a tu lista de Rock!")
            
        if st.button("🔄 Nueva recomendación", type="primary", use_container_width=True):
            nueva = random.choice(generos["Rock"]) # Aquí elegirá una similar
            st.session_state.recomendacion = nueva
            st.rerun()

    with col2:
        if st.button("🍿 Guardar en Pop", use_container_width=True):
            st.toast("Guardado en Pop")

# Si hay una recomendación activa, la muestra
if 'recomendacion' in st.session_state:
    st.write("---")
    st.write("✨ Te recomendamos esta por su ritmo:")
    st.video(st.session_state.recomendacion)
