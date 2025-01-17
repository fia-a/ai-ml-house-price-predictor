import os
from pathlib import Path

class Config:
    # Base paths
    BASE_DIR = Path(__file__).parent.parent
    ARTIFACTS_DIR = BASE_DIR / "artifacts"
    LOGS_DIR = BASE_DIR / "logs"
    STATIC_DIR = BASE_DIR / "static"
    
    # Data paths
    DATA_PATH = ARTIFACTS_DIR / "boston.csv"
    MODEL_PATH = ARTIFACTS_DIR / "best_model.pkl"
    SCALER_PATH = ARTIFACTS_DIR / "scaler.pkl"
    METRICS_PATH = ARTIFACTS_DIR / "metrics.json"
    FEATURE_IMPORTANCE_PATH = ARTIFACTS_DIR / "feature_importance.json"
    
    # Model parameters
    RANDOM_STATE = 42
    TEST_SIZE = 0.3
    NUM_FEATURES = 8
    TARGET_COLUMN = "MEDV"
    
    # Feature columns for model
    FEATURE_COLUMNS = [
        "LSTAT", "RM", "CRIM", "PTRATIO",
        "INDUS", "TAX", "NOX", "B"
    ]
    
    # Model hyperparameters
    PARAMS = {
        'regressor__max_depth': [3, 4, 5, 6, 7, 8, 9, 10],
        'regressor__learning_rate': [0.001, 0.01, 0.1],
        'regressor__n_estimators': [100, 200, 300],
        'regressor__min_child_weight': [1, 3, 5],
        'regressor__gamma': [0, 0.1, 0.2],
        'regressor__subsample': [0.8, 0.9, 1.0]
    }
    
    # Cross validation settings
    CV_FOLDS = 5
    
    # Logging configuration
    LOG_FILE = LOGS_DIR / "app.log"
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    LOG_LEVEL = "INFO"
    
    # FastAPI settings
    API_TITLE = "House Price Prediction API"
    API_DESCRIPTION = "API for predicting house prices using the Boston Housing Dataset"
    API_VERSION = "1.0.0"
    HOST = "0.0.0.0"
    PORT = 8000
    
    # Streamlit settings
    STREAMLIT_PORT = 8501
    PAGE_TITLE = "House Price Prediction"
    PAGE_ICON = "🏠"
    LAYOUT = "wide"
    
    # Cache settings
    CACHE_TTL = 3600  # 1 hour
    
    # Feature descriptions for documentation
    FEATURE_DESCRIPTIONS = {
        "CRIM": "Per capita crime rate by town",
        "ZN": "Proportion of residential land zoned for large lots",
        "INDUS": "Proportion of non-retail business acres",
        "CHAS": "Charles River dummy variable",
        "NOX": "Nitric oxides concentration",
        "RM": "Average number of rooms per dwelling",
        "AGE": "Proportion of owner-occupied units built prior to 1940",
        "DIS": "Weighted distances to employment centres",
        "RAD": "Index of accessibility to radial highways",
        "TAX": "Full-value property-tax rate",
        "PTRATIO": "Pupil-teacher ratio by town",
        "B": "Black population ratio",
        "LSTAT": "% lower status of the population",
        "MEDV": "Median value of owner-occupied homes"
    }
    
    # Model performance thresholds
    METRIC_THRESHOLDS = {
        'r2_score': 0.8,
        'mae': 3.0,
        'rmse': 4.0
    }
    
    # Data validation rules
    DATA_VALIDATION = {
        'CRIM': {'min': 0, 'max': 100},
        'RM': {'min': 3, 'max': 9},
        'LSTAT': {'min': 0, 'max': 40},
        'PTRATIO': {'min': 12, 'max': 22},
        'INDUS': {'min': 0, 'max': 30},
        'TAX': {'min': 150, 'max': 800},
        'NOX': {'min': 0.3, 'max': 0.9},
        'B': {'min': 0, 'max': 400}
    }
    
    @classmethod
    def create_directories(cls):
        """Create necessary directories if they don't exist."""
        directories = [cls.ARTIFACTS_DIR, cls.LOGS_DIR, cls.STATIC_DIR]
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
    
    @classmethod
    def get_feature_range(cls, feature):
        """Get the valid range for a feature."""
        return cls.DATA_VALIDATION.get(feature, {'min': float('-inf'), 'max': float('inf')})
    
    @classmethod
    def is_valid_feature_value(cls, feature, value):
        """Check if a feature value is within valid range."""
        ranges = cls.get_feature_range(feature)
        return ranges['min'] <= value <= ranges['max']

# Create directories on import
Config.create_directories()