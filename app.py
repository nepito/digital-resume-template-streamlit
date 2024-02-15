from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "cv_nepo-rojas.pdf"
profile_pic = current_dir / "assets" / "para_cv.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "CV | Nepo Rojas"
PAGE_ICON = ":wave:"
NAME = "Nepo Rojas"
DESCRIPTION = """
Científico de Datos y apasionado del fútlbol.
"""
EMAIL = "nepo@nies.futbol"
SOCIAL_MEDIA = {
#    "YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://www.linkedin.com/in/nepo-rojas-7a528823b/",
    "GitHub": "https://github.com/niesfutbol",
    "Twitter": "https://twitter.com/niesfutbol",
}
PROJECTS = {
    "🏆 Análisis de fútbol y mercados de apuestas": "https://www.nies.futbol/",
    "🏆 Tipster": "https://predictions-nies.streamlit.app/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experiencia y habilidades")
st.write(
    """
- ✔️ 7 años de experiencia profesional extrayendo información de los datos
- ✔️ 20 años de experiencia programando en Python, R, Fortran y MATLAB
- ✔️ 20 años de experiencia en modelación estadística
- ✔️ Excelente conocimiento de estadística y sus aplicaciones
- ✔️ Excelente habilidades en trabajo colaborativo
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Habilidades técnicas")
st.write(
    """
- 👩‍💻 Programacón: Python y R
- 📊 Visualización de datos: Plotly, Bokeh, ggplot y LockerStudio
- 📚 Simulación computacional y aprendizaje automatizado
- 🗄️ CI/CD: TDD, Pruebas automáticas, Docker y Entrega continua 
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Proyectos")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

st.write('\n')
st.subheader("Cursos de Visorías y Análisis de Datos")
st.write("---")
st.write(
    """
    ### Professional Football Scouts Association (PFSA)
    - ⚽ **Introduction Into Football Scouting** | PFSA (2023)
    - ⚽ **Level 1 Technical Scouting In Football** | PFSA (2023)
    - ⚽ **Level 1 Opposition Analysis In Football** | PFSA (2023)
    - ⚽ **Level 1 Data Analysis In Football** | PFSA (2023)
    - ⚽ **Level 1 Talent Identification In Football** | PFSA (2023)
    ### edX
    - ⚽ **Valoración de Futbolistas con el Método AHP** | UPValenciaX (2022)
    """
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Experiencia Laboral")
st.write("---")

# --- JOB 1
st.write("👩🏿‍🔬", "**Científico de Datos | GECI**")
st.write("Feb/2017 - Presente")
st.write(
    """
- ► Predicción del efecto de diferentes escenarios sobre las poblaciones de especies que protegemos
- ► Evaluación cuantitativa del desempeño de los proyectos de restauración
- ► Optimización los recursos para la conservación
"""
)

# --- JOB 2
st.write('\n')
st.write("👩🏿‍🏫", "**Profesor por asignaturas | Universidad Autónoma del Estado de Morelos**")
st.write("Ene/2014 - Ene/2017")
st.write(
    """
- ► Física 1, Termodinámica
- ► Probabilidad y estadística, Transformadas integrales
"""
)

st.write('\n')
st.subheader("Educación")
st.write("---")
st.write(
    """
    - 🎓 **Maestro en Ciencias Físicas** | Universidad Nacional Autónoma de México (2011-2013)
    - 🎓 **Licenciado en Física** | Universidad de Sonora (2014-2010)
    """
)
