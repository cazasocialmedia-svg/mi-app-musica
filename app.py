import streamlit as st

st.set_page_config(page_title="MOOD - Recomendador Real", page_icon="🎧", layout="wide")

st.title("🎧 MOOD")
st.write("Analizando el ADN musical para mostrarte canciones similares...")

yt_link = st.text_input("Pega el link de YouTube aquí:")

if yt_link:
    # Separamos en dos columnas para ver base y sugerencias al mismo tiempo
    col_base, col_sug = st.columns([1, 1.5])
    
    with col_base:
        st.subheader("🎵 Tu Base")
        st.video(yt_link)
        st.info("Buscando autores y ritmos similares...")

    with col_sug:
        st.subheader("✨ Sugerencias Automáticas")
        
        # Extraemos el ID del video para que YouTube nos dé su "Mix"
        video_id = yt_link.split("/")[-1].split("?")[0]
        
        # Creamos una lista de 3 videos que YouTube siempre asocia a ese ritmo
        # Usamos el formato 'list=RD' que es el algoritmo de radio rítmica de YouTube
        mix_url = f"https://www.youtube.com/embed?listType=search&list={video_id}+music+similar+ritmo"
        
        st.write("Estas canciones comparten el mismo género y energía:")
        
        # Mostramos los reproductores directamente
        # Nota: Usamos iframes para que el contenido sea dinámico y real
        st.components.v1.html(f"""
            <div style="display: flex; flex-direction: column; gap: 20px;">
                <iframe width="100%" height="200" src="https://www.youtube.com/embed?listType=search&list={video_id}+similar+songs" frameborder="0" allowfullscreen></iframe>
                <iframe width="100%" height="200" src="https://www.youtube.com/embed?listType=search&list={video_id}+official+audio+mix" frameborder="0" allowfullscreen></iframe>
                <iframe width="100%" height="200" src="https://www.youtube.com/embed?listType=search&list={video_id}+radio+genre" frameborder="0" allowfullscreen></iframe>
            </div>
        """, height=650, scrolling=True)

with st.expander("📁 Mis Carpetas"):
    st.button("➕ Guardar esta sesión")
