import joblib
import os


def save_model(model, path: str):
    """
    Save trained model
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump(model, path)


def load_model(path: str):
    """
    Load trained model
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model not found: {path}")
    return joblib.load(path)