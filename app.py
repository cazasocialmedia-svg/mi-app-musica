import streamlit as st
from youtubesearchpython import VideosSearch, Video

st.set_page_config(page_title="MOOD - Recomendador Real", page_icon="🎧")

st.title("🎧 MOOD")
st.write("Analizando el ADN musical de tu video...")

yt_link = st.text_input("Pega el link de YouTube aquí:")

if yt_link:
    tab1, tab2 = st.tabs(["🎵 Mi Base", "✨ Sugerencias Similares"])
    
    with tab1:
        st.video(yt_link)
    
    with tab2:
        try:
            # Obtenemos información del video original (Título y Autor)
            video_info = Video.getInfo(yt_link)
            titulo = video_info['title']
            canal = video_info['channel']['name']
            
            st.subheader(f"Basado en: {titulo}")
            st.write(f"Buscando ritmos similares a **{canal}**...")

            # Creamos una búsqueda inteligente basada en el autor y género
            # Buscamos "Mix" o "Similar songs" para obtener variedad de autores
            search_query = f"{titulo} {canal} similar songs mix"
            v_search = VideosSearch(search_query, limit=5)
            resultados = v_search.result()['result']

            for res in resultados:
                # Evitamos mostrar el mismo video que pegaste
                if res['id'] not in yt_link:
                    with st.container(border=True):
                        col_a, col_b = st.columns([1, 2])
                        with col_a:
                            st.image(res['thumbnails'][0]['url'])
                        with col_b:
                            st.markdown(f"**{res['title']}**")
                            st.caption(f"Canal: {res['channel']['name']}")
                            st.video(res['link'])
                            
        except Exception as e:
            st.error("No se pudo analizar el video. Asegúrate de que el link sea válido.")

with st.expander("📁 Mis Carpetas"):
    st.button("➕ Guardar en Playlist")

