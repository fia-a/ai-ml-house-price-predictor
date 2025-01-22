import streamlit as st
import pandas as pd
import numpy as np
import requests
import plotly.express as px
from config.config import Config
from utils.styling import load_css

st.set_page_config(page_title="Predictions", page_icon="🔮", layout="wide")

# Load CSS
load_css()

# Initialize session state
if 'predictions' not in st.session_state:
    st.session_state.predictions = []

st.title("Prediction")

# Manual Input Section
st.subheader("Manual Prediction")

# Input fields for manual prediction
LSTAT = st.slider("LSTAT (% lower status of the population)", 1.0, 40.0, 10.0)
RM = st.slider("RM (Average number of rooms per dwelling)", 3.0, 9.0, 6.0)
CRIM = st.slider("CRIM (Per capita crime rate by town)", 0.0, 100.0, 1.0)
PTRATIO = st.slider("PTRATIO (Pupil-teacher ratio by town)", 10.0, 30.0, 15.0)
INDUS = st.slider("INDUS (% of non-retail business acres per town)", 0.0, 30.0, 10.0)
TAX = st.slider("TAX (Full-value property tax rate per $10,000)", 100.0, 800.0, 300.0)
NOX = st.slider("NOX (Nitric oxides concentration in ppm)", 0.1, 1.0, 0.5)
B = st.slider("B (1000(Bk - 0.63)^2 where Bk is the proportion of Black residents by town)", 0.0, 400.0, 300.0)

if st.button("Predict for Manual Input"):
    try:
        with st.spinner('Making prediction...'):
            # Prepare input data
            input_data = {
                "LSTAT": LSTAT,
                "RM": RM,
                "CRIM": CRIM,
                "PTRATIO": PTRATIO,
                "INDUS": INDUS,
                "TAX": TAX,
                "NOX": NOX,
                "B": B
            }

            # Send data to API for prediction
            response = requests.post("http://localhost:8000/predict", json=input_data)

            if response.status_code == 200:
                prediction = response.json()["prediction"]
                st.success(f"Predicted Price: ${prediction:.2f}")
            else:
                st.error(f"Error making prediction: {response.text}")
    except requests.exceptions.ConnectionError:
        st.error("Error connecting to the prediction service. Please make sure the API is running.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# CSV Upload Section
st.subheader("Upload CSV for Bulk Prediction")
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"], help="Upload a CSV file with feature columns.")

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)
        st.write("### Preview of Uploaded Data")
        st.dataframe(data.head())

        # Validate columns
        required_columns = ["LSTAT", "RM", "CRIM", "PTRATIO", "INDUS", "TAX", "NOX", "B"]
        if all(col in data.columns for col in required_columns):
            st.success("File format is valid.")
        else:
            st.error(f"File must contain the following columns: {', '.join(required_columns)}")
            uploaded_file = None
    except Exception as e:
        st.error(f"Error reading CSV file: {e}")
        uploaded_file = None

# Button to trigger prediction for uploaded CSV
if uploaded_file is not None:
    if st.button("Predict for Uploaded Data"):
        try:
            with st.spinner('Making predictions...'):
                # Send data to API for bulk prediction
                response = requests.post(
                    "http://localhost:8000/bulk_predict",  # Endpoint for bulk prediction
                    json=data.to_dict(orient="records")
                )

                if response.status_code == 200:
                    predictions = response.json()["predictions"]

                    # Combine predictions with original data
                    data["Predicted Price"] = predictions
                    st.session_state.predictions = data

                    st.success("Predictions completed!")
                    st.write("### Prediction Results")
                    st.dataframe(data)

                    # Option to download predictions
                    st.download_button(
                        label="Download Predictions",
                        data=data.to_csv(index=False).encode('utf-8'),
                        file_name="predictions.csv",
                        mime="text/csv"
                    )
                else:
                    st.error(f"Error making prediction: {response.text}")
        except requests.exceptions.ConnectionError:
            st.error("Error connecting to the prediction service. Please make sure the API is running.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        <p>Built with ❤️ using Streamlit</p>
    </div>
""", unsafe_allow_html=True)
