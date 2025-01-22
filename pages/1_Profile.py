import streamlit as st
import pandas as pd
from utils.styling import load_css
import base64

#make cv download able
def get_pdf_download_link(pdf_path, filename):
    """Generate download link for PDF file"""
    with open(pdf_path, "rb") as f:
        bytes_data = f.read() #encode process to base64(readable link)
    b64 = base64.b64encode(bytes_data).decode()
    href = f'<a href="data:application/pdf;base64,{b64}" download="{filename}" class="download-button">📥 Download CV</a>'
    return href

st.set_page_config(page_title="Profile", page_icon="👤", layout="wide")

load_css()

# Custom CSS
st.markdown("""
    <style>
    .css-1v0mbdj.etr89bj1 {
        text-align: center;
    }
    .profile-img {
        border-radius: 50%;
        margin: 0 auto;
        display: block;
    }
    .social-links {
        text-align: center;
        padding: 1rem 0;
    }
    .experience-card {
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 5px;
        border-left: 3px solid #0366d6;
    }
    </style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    # Profile Image
    st.image("static/img/profile.jpg.jpg", width=200, output_format="auto")
    
    # Contact Information
    st.markdown("""
    ### Contact
    - 📧 fia.ulanova@gmail.com
    - 📱 +61
    """)
    
    # Social Links
    st.markdown("""
    ### Social Links
    - [GitHub](https://github.com/fia-a)
    - [LinkedIn](http://linkedin.com/in/fia-a-4836a5294)
    """)

with col2:
    st.title("Fia")
    st.subheader("Data Scientist")
    st.markdown(get_pdf_download_link("cv/Fia-Resume-2025.pdf", "fia_cv.pdf"), unsafe_allow_html=True)

    
    st.markdown("""
    ### Summary
    Data Science graduate with expertise in AI, machine learning, and analytics, leveraging Python,
    data analysis, and visualization skills to deliver impactful solutions. Proven ability to address
    complex business challenges with insights from data, supported by excellent communication and
    collaboration across multicultural teams in Japan, Singapore, Indonesia, and Australia.
    """)

# Experience Section
st.header("Professional Experience")

experiences = [
    {
        "role": "Junior Data Scientist/Engineer",
        "company": "Various Projects",
        "period": "2023 – Present",
        "points": [
            "Built an NLP-based chatbot for customer support (Alchatbot, Dec 2024)",
            "Developed a movie recommendation system using content-based & collaborative filtering (Dec 2024)",
            "Optimized housing price prediction models with GridSearchCV & RandomSearchCV (California Housing, Nov 2024)",
            "Created an OCR solution for passport data extraction using Python (Nov 2024)",
            "Applied machine learning for advertisement performance analysis & targeting (Dec 2024)"
        ]
    },
    {
        "role": "Japanese Interpreter & Executive Assistant",
        "company": "Kashiwabara, Indonesia Branch",
        "period": "05/2022 – 08/2023",
        "points": [
            "Supported the launch of the World’s Largest Smelter project in Gresik",
            "Recovered outstanding receivables via cross-cultural communication"
        ]
    },
    {
        "role": "English/Japanese Interpreter",
        "company": "ANA All Nippon Airways, Tokyo, Japan",
        "period": "08/2019 – 09/2020",
        "points": [
            "Enhanced customer experience through precise Japanese-English interpretation",
            "Resolved passenger issues, ensuring smooth communication"
        ]
    }
]
for exp in experiences:
    with st.expander(f"{exp['company']} - {exp['role']}", expanded=True):
        st.markdown(f"**Period:** {exp['period']}")
        for point in exp['points']:
            st.markdown(f"- {point}")
            
# Skills Section
st.header("Skills & Expertise")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Hard Skills")
    hard_skills = [
        "Python", "SQL", "Flask", "Swagger UI", "Jupyter", "Scikit-learn", 
        "TensorFlow", "Keras", "XGBoost", "EDA", "Data Cleaning", 
        "Hypothesis Testing", "A/B Testing", "Logistic Regression", 
        "Decision Trees", "Clustering", "Random Forest", "Neural Networks (ANN, DNN, CNN, RNN)", 
        "Model Tuning (GridSearchCV, BayesSearchCV)", "Chatbot Development (spaCy, Transformers)", 
        "Generative AI", "Prompt Engineering", "RAG", "Model Deployment (Docker, Flask APIs)"
    ]
    for skill in hard_skills:
        st.markdown(f"- {skill}")

with col2:
    st.subheader("Tools & Technologies")
    tools = [
        "Python", "Flask", "SQL", "Jupyter", "TensorFlow", "Keras", "XGBoost", 
        "spaCy", "Transformers", "Docker", "Flask APIs", "Scikit-learn", "Swagger UI"
    ]
    for tool in tools:
        st.markdown(f"- {tool}")
        
with col3:
    st.subheader("Languages")
    languages = [
        "Indonesian (Native)",
        "English (Professional working proficiency)",
        "Japanese (Professional working proficiency)",
        "Korean (Limited working proficiency)"
    ]
    for language in languages:
        st.markdown(f"- {language}")

# Education Section
st.header("Education")
st.markdown("""
#### University of Texas at Austin, United States
- **Degree:** Postgraduate in Data Science & Business Analytics
- **GPA:** 4.19/4.33
- **Period:** Graduated in 2024 with Excellent Performance
- **Focus Areas:** Statistics, Data Analysis, Machine Learning, Predictive Modeling, Business Insights

#### Pamulang University, Indonesia
- **Degree:** Bachelor of Law
- **GPA:** 3.40/4.00
- **Period:** Graduated in 2015 with a Strong Academic Record
- **Focus Areas:** Legal principles, critical thinking, and analytical problem-solving
""")

# Nonformal & Specialized Training Section
st.header("Nonformal & Specialized Training")
st.markdown("""
#### DibimbingId – AI/ML Engineering (10/2024 – Present)
- **Specialization:** Feature Engineering, Supervised & Unsupervised Learning, Hyperparameter Tuning, Ensemble Learning, ANN, DNN, CNN, RNN, OCR, RAG, GenAI, Chatbot, Recommendation Systems, Dockerized Deployment, and MLOps.
- **Achievement:** Top 5 Student (Oct 2024), Overall Score: 92/100

#### Binar Academy – Data Science (8/2023 – 3/2024)
- **Focus Areas:** Database, SQL, Deployment, API Flask, NLP, CNN, RNN, LSTM
- **Project Grade:** Python for Machine Learning (Flask, Swagger UI, SQL, NLP) – 96/100

#### Human Academy Tokyo – Advanced Japanese Language (2/2020 – 12/2020)
- **Certification:** JLPT N2 Certified in 2021
""")

# Certifications Section
st.header("Certifications")
certifications = [
    "SQL: (Introduction SQL with MySQL) – GreatLearning 2025",
    "Postgrad in Data Science & Business Analytics – UT Austin 2024",
    "Data Science – Binar Academy 2024",
    "Data Science – MySkill 2022",
    "Website Development – MySkill 2022",
    "N2 Japanese Language Proficiency – Japan Foundation 2021",
    "TOEIC: Score 855 – IIBC 2020",
    "Korean Sejong 4 – Korean Culture Center 2016",
    "Bachelor of Law – Pamulang University 2015"
]

for cert in certifications:
    st.markdown(f"- {cert}")
