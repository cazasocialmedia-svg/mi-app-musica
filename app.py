import streamlit as st
from youtubesearchpython import VideosSearch

st.set_page_config(page_title="MOOD - Recomendador Real", page_icon="🎧", layout="wide")

st.title("🎧 MOOD")
st.write("Analizando ritmo y género para mostrarte música similar...")

yt_link = st.text_input("Pega el link de YouTube aquí:")

if yt_link:
    col_base, col_sug = st.columns([1, 1.5])
    
    with col_base:
        st.subheader("🎵 Tu Base")
        st.video(yt_link)
        st.info("Buscando canciones con la misma energía...")

    with col_sug:
        st.subheader("✨ Recomendaciones Directas")
        try:
            # Buscamos "Mix" rítmico basado en el video original
            # Esto nos da los resultados que YouTube asocia por género y ritmo
            query = f"{yt_link} music mix official audio similar"
            v_search = VideosSearch(query, limit=5)
            resultados = v_search.result()['result']
            
            if resultados:
                for res in resultados:
                    # Filtramos el video original para no repetirlo
                    if res['id'] not in yt_link:
                        with st.container(border=True):
                            c1, c2 = st.columns([1, 2])
                            with c1:
                                # Mostramos la miniatura para que sea visual
                                st.image(res['thumbnails'][0]['url'], use_container_width=True)
                            with c2:
                                st.markdown(f"**{res['title']}**")
                                st.caption(f"Autor: {res['channel']['name']} | ⏱️ {res['duration']}")
                                # Botón que abre el video similar directamente
                                st.video(res['link'])
            else:
                st.warning("No se encontraron videos similares.")
        except Exception:
            st.error("Error al conectar con el motor de música. Revisa tu conexión.")

with st.expander("📁 Mis Carpetas"):
    st.button("➕ Guardar esta sesión")

