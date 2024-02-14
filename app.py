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
EMAIL = "nepo.rojas@gmail.com"
SOCIAL_MEDIA = {
#    "YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://www.linkedin.com/in/nepo-rojas-7a528823b/",
    "GitHub": "https://github.com/niesfutbol",
    "Twitter": "https://twitter.com/niesfutbol",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
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
- ✔️ 20 años de experiencia programando y modelando en Fortran, MatLab, Python y R
- ✔️ Excelente conocimiento de estadística y sus aplicaciones
- ✔️ Excelente habilidades del trabajo collaborativo
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programacón: Python y R
- 📊 Visualización de datos: Plotly, Bokeh, ggplot y LockerStudio
- 📚 Modelación: sí (Regresión Lineal, Logistic regression, linear regression, decition trees)
- 🗄️ CI/CD: TDD, Pruebas automáticas, Docker, Canales de entrega continua 
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
- ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
- ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
- ► Redesigned data model through iterations that improved predictions by 12%
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
