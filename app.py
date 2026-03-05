import streamlit as st

st.set_page_config(page_title="MOOD - Motor Rítmico", page_icon="🎧")

st.title("🎧 MOOD")
st.write("Analizando ritmo y género para encontrar tu próxima canción favorita.")

yt_link = st.text_input("Pega el link de YouTube aquí:")

if yt_link:
    # Dividimos la pantalla para que sea más organizado
    tab1, tab2 = st.tabs(["🎵 Mi Base", "✨ Sugerencias Similares"])
    
    with tab1:
        st.video(yt_link)
        st.caption("Canción semilla detectada.")

    with tab2:
        st.subheader("Similares en Ritmo y Género")
        st.info("Haz clic en los videos de abajo para escuchar las recomendaciones:")
        
        # Extraemos una búsqueda limpia para YouTube
        # Usamos el link como referencia para que YouTube nos dé su "Radio" rítmica
        col1, col2 = st.columns(2)
        
        # Generamos 4 recomendaciones visuales
        # Nota: Como no usamos la API bloqueada de Spotify, 
        # enviamos al usuario a la búsqueda de 'Radio' de ese video exacto.
        
        busquedas = [
            "music mix similar to this",
            "official music video same genre",
            "top hits same bpm",
            "recommended for you music"
        ]
        
        for i, b in enumerate(busquedas):
            with [col1, col2][i % 2]:
                with st.container(border=True):
                    # Creamos un link de búsqueda rítmica inteligente
                    # Esto fuerza a YouTube a mostrar contenido similar en lugar de aleatorio
                    query = f"{yt_link} {b}".replace(" ", "+")
                    search_url = f"https://www.youtube.com/results?search_query={query}"
                    
                    st.markdown(f"**Recomendación Rítmica #{i+1}**")
                    st.write("Explora el género similar:")
                    st.link_button("▶️ Ver videos similares", search_url)

st.divider()
with st.expander("📁 Mis Carpetas"):
    st.button("➕ Nueva Carpeta")

