import pickle
import os
import numpy as np

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'habit_model.pkl')
_model = None

def load_model():
    global _model
    if _model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model file not found at {MODEL_PATH}. Run train_model.py first.")
        with open(MODEL_PATH, 'rb') as f:
            _model = pickle.load(f)
    return _model

def predict_skip_probability(features: dict) -> dict:
    """
    Expects dict with keys: sleep_hours, stress_level, previous_workout, hydration, consistency.
    Returns prediction probabilities and risk label.
    """
    model = load_model()
    
    # Format input as 2D array for sklearn
    X = np.array([[
        features.get("sleep_hours", 7),
        features.get("stress_level", 5),
        features.get("previous_workout", 1),
        features.get("hydration", 6),
        features.get("consistency", 50)
    ]])
    
    # predict_proba returns array of shape (n_samples, n_classes) => [[prob_0, prob_1]]
    probabilities = model.predict_proba(X)[0]
    skip_prob = probabilities[1] # Probability of class '1' (skip)
    
    if skip_prob > 0.65:
        risk = "high"
        rec = "High risk of skipping tomorrow. Try to go to sleep 30 mins earlier, hydrate well, and prep your gym bag tonight!"
    elif skip_prob > 0.4:
        risk = "medium"
        rec = "Moderate risk. You might feel sluggish tomorrow. Plan a somewhat lighter or shorter workout to ensure you maintain consistency."
    else:
        risk = "low"
        rec = "Low risk. Keep up the great habits! You are primed to crush your next session."
        
    return {
        "skip_probability": float(skip_prob),
        "risk": risk,
        "recommendation": rec
    }
