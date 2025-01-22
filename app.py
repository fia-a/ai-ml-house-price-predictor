from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np
import pandas as pd
from config.config import Config
from utils.logger import setup_logger
from fastapi.middleware.cors import CORSMiddleware

logger = setup_logger('api')

class FeatureInput(BaseModel):
    LSTAT: float
    RM: float
    CRIM: float
    PTRATIO: float
    INDUS: float
    TAX: float
    NOX: float
    B: float

    class Config:
        schema_extra = {
            "example": {
                "LSTAT": 10.0,
                "RM": 6.0,
                "CRIM": 0.1,
                "PTRATIO": 15.0,
                "INDUS": 10.0,
                "TAX": 300.0,
                "NOX": 0.5,
                "B": 300.0
            }
        }

# FastAPI instance
app = FastAPI(
    title=Config.API_TITLE,
    description=Config.API_DESCRIPTION,
    version=Config.API_VERSION
)

# CORS middleware (for cross-origin requests, e.g., from Streamlit)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as needed
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Load model and scaler at startup
try:
    with open(Config.MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    with open(Config.SCALER_PATH, 'rb') as f:
        scaler = pickle.load(f)
    logger.info("Model and scaler loaded successfully")
except Exception as e:
    logger.error(f"Error loading model or scaler: {str(e)}")
    raise HTTPException(status_code=500, detail=f"Error loading model or scaler: {str(e)}")

@app.post("/predict")
async def predict(features: FeatureInput):
    try:
        # Validate input features
        for feature, value in features.dict().items():
            if not Config.is_valid_feature_value(feature, value):
                raise HTTPException(
                    status_code=400,
                    detail=f"Invalid value for {feature}: {value}. Expected between {Config.get_feature_range(feature)['min']} and {Config.get_feature_range(feature)['max']}."
                )
        
        # Prepare input for prediction
        feature_dict = features.dict()
        input_df = pd.DataFrame([feature_dict])[Config.FEATURE_COLUMNS]
        
        # Scale the features
        input_scaled = scaler.transform(input_df)
        
        # Make prediction
        prediction = model.predict(input_scaled)
        final_prediction = float(np.exp(prediction[0]))  # Ensure prediction is in the correct format
        
        logger.info(f"Prediction made for input: {feature_dict}")
        return {"prediction": final_prediction}
    
    except Exception as e:
        logger.error(f"Error making prediction: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=Config.HOST, port=Config.PORT)
