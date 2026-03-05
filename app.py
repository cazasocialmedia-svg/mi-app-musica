import streamlit as st
from youtubesearchpython import VideosSearch

st.set_page_config(page_title="MOOD - Recomendador Real", page_icon="🎧")

st.title("🎧 MOOD")
st.write("Pegue un link para encontrar música similar en ritmo y género.")

yt_link = st.text_input("Pega el link de YouTube aquí:")

if yt_link:
    tab1, tab2 = st.tabs(["🎵 Mi Base", "✨ Sugerencias Similares"])
    
    with tab1:
        st.video(yt_link)
    
    with tab2:
        st.subheader("Similares en Ritmo y Género")
        
        # Como no tenemos Premium de Spotify, 
        # usamos el buscador de YouTube para encontrar el "Mix" relacionado.
        # Buscamos el ID del video para encontrar su radio o mix rítmico.
        try:
            query = f"{yt_link} music mix similar"
            v_search = VideosSearch(query, limit=4)
            resultados = v_search.result()['result']
            
            if resultados:
                for res in resultados:
                    # Ignoramos el video original si aparece en los resultados
                    if res['link'] != yt_link:
                        with st.container(border=True):
                            st.markdown(f"🌟 **{res['title']}**")
                            st.caption(f"Canal: {res['channel']['name']} | Duración: {res['duration']}")
                            st.video(res['link'])
            else:
                st.warning("No encontré videos similares en este momento.")
        except Exception:
            st.error("Error al conectar con el motor de búsqueda. Intenta refrescar la página.")

with st.expander("📁 Mis Carpetas"):
    st.button("➕ Guardar en Playlist")

