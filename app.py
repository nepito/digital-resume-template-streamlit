from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "CV | Nepo Rojas"
PAGE_ICON = ":wave:"
NAME = "Nepo Rojas"
DESCRIPTION = """
Científico de Datos.
"""
EMAIL = "nepo@nies.futbol"
SOCIAL_MEDIA = {
#    "YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://www.linkedin.com/in/nepo-rojas-7a528823b/",
    "GitHub": "https://github.com/niesfutbol",
    "Twitter": "https://twitter.com/niesfutbol",
}
PROJECTS = {
    "🏆 Análisis de fútbol y mercados de apuestas - ": "https://www.nies.futbol/",
    "🏆 Tipster": "https://predictions-nies.streamlit.app/",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
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
- ✔️ 7 años de experiencia estrayendo información de los datos
- ✔️ 20 años de experiencia programando en Fortran, MatLab, Python y R
- ✔️ 20 años de experiencia con métodos numéricos y modelación estadística
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
- 📚 Modelación estadística y aprendizaje automatizado
- 🗄️ CI/CD: TDD, Pruebas automáticas, Docker y Entrega continua 
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Experiencia Laboral")
st.write("---")

# --- JOB 1
st.write("🚧", "**Científico de Datos | GECI**")
st.write("Feb/2017 - Presente")
st.write(
    """
- ► Modelado de ecológico bao diferentes escenarios
- ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
- ► Evaluación de la acciones ecológicas implementadas 
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Profesor por asignaturas | Universidad Autónoma del Estodo de Morelos**")
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
    - 🎓 **Licenciado en Física** | Universidad de Sonora (2014-2010)
    - 🎓 **Maestro en Ciencias Físicas** | Universidad Nacional Autónoma de México (2011-2013)
    """
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
