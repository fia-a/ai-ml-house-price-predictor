import streamlit as st
from PIL import Image
import os

# Set Streamlit page configuration
st.set_page_config(page_title="My Projects", page_icon="📂")

# Function to display a single project
def display_project(title, description, link, image_path, skills):
    with st.container():
        st.subheader(title)
        st.write(description)
        if link:
            st.markdown(f"[Access Project]({link})")
        # Handle image display and missing file errors
        if image_path:
            if os.path.exists(image_path):
                st.image(image_path, use_container_width=True)
            else:
                st.error(f"Image not found: {image_path}")
        if skills:
            st.write(f"**Skills:** {', '.join(skills)}")
        st.markdown("---")

# List of projects
projects = [
    {
        "title": "Alchatbot (Chatbot Development)",
        "description": "Created a chatbot leveraging NLP techniques to provide automated customer support. The chatbot improved response time and user engagement while reducing the workload of support agents.",
        "link": "https://drive.google.com/file/d/1LhLXN4fatHRtUoYbd8WoBBzczsD4hU2j/view?usp=drive_link",
        "image_path": "static/img/chatbotpink.png",  # Ensure this path is valid
        "skills": ["NLP", "Python", "Machine Learning", "Flask"]
    },
    {
        "title": "Movie Recommendation System",
        "description": "Developed a personalized movie recommendation system using content-based and collaborative filtering, leveraging similarity measures to improve user experience.",
        "link": "https://drive.google.com/file/d/1eFgMbHxceCSP3vbTfqjOgaynScc23Fdn/view?usp=drive_link",
        "image_path": "static/img/recsystem.jpg",
        "skills": ["Python", "Pandas", "Collaborative Filtering", "Content-Based Filtering"]
    },
    {
        "title": "Advertisement Analysis (Supervised & Unsupervised Learning)",
        "description": "Applied supervised and unsupervised learning to analyze ad performance, optimize targeting, and uncover customer behavior insights, driving improvements in ad strategies.",
        "link": "https://drive.google.com/file/d/1VyfWaabeCpYej0m0sNLpAgI6LPUevHOO/view?usp=drive_link",
        "image_path": "static/img/advert.jpg",
        "skills": ["Python", "Scikit-learn", "Clustering", "Regression"]
    },
    {
        "title": "CNN Garbage Classifier (Image Classification - CNN)",
        "description": "Developed a custom Convolutional Neural Network (CNN) using TensorFlow and Keras to classify waste categories (cardboard, glass, metal, paper, plastic, trash). Achieved 75% accuracy with strong performance in cardboard, paper, and metal categories.",
        "link": "https://drive.google.com/file/d/1ZAAwiFTRblGfOwbXk8x475oEDoECeszG/view?usp=drive_link",
        "image_path": "static/img/garbage.jpg",
        "skills": ["TensorFlow", "Keras", "CNN", "Image Processing"]
    },
    {
        "title": "California Housing - Hyperparameter Tuning",
        "description": "Optimized machine learning models for predicting housing prices using hyperparameter tuning techniques, improving model performance through grid search and random search methods.",
        "link": "https://drive.google.com/file/d/1Y4bNy3_FaQnhNu_GJCHmJx3bVuGemReL/view?usp=drive_link",
        "image_path": "static/img/modernhouse.jpg",
        "skills": ["Python", "XGBoost", "Grid Search", "Random Search"]
    },
    {
        "title": "OCR Passport Information Extraction",
        "description": "Developed an OCR-based solution to extract relevant information from scanned passport images, enhancing data entry processes and improving accuracy in passport processing systems.",
        "link": "https://drive.google.com/file/d/1jWJfY8g2RfPqxOWw899vfwMfwDjFiTwC/view?usp=drive_link",
        "image_path": "static/img/passportextraction.jpg",
        "skills": ["OCR", "Python", "Tesseract", "Image Processing"]
    },
    {
        "title": "Students Performance - Ensemble Techniques",
        "description": "Utilized ensemble techniques to build a model predicting student performance, providing insights into factors influencing academic success and improving educational outcomes.",
        "link": "https://drive.google.com/file/d/1lY6IHVUHZO1FpM25z4pKiaSQ5mRAziZC/view?usp=drive_link",
        "image_path": "static/img/students.jpg",
        "skills": ["Python", "Random Forest", "Boosting", "EDA"]
    }
]

# Streamlit App
st.title("My Projects")
st.write("Here are some of the projects I've worked on, showcasing my skills and experience in AIML.")

for project in projects:
    display_project(
        title=project["title"],
        description=project["description"],
        link=project["link"],
        image_path=project["image_path"],
        skills=project["skills"]
    )
