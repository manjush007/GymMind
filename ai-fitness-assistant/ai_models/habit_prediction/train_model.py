import pandas as pd
import numpy as np
import pickle
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'habit_model.pkl')

def create_synthetic_data(num_samples=1000):
    np.random.seed(42)
    # Features: sleep_hours (3-12), stress_level (1-10), previous_workout (0 or 1), hydration (0-12), consistency (0-100)
    sleep = np.random.uniform(3, 11, num_samples)
    stress = np.random.randint(1, 11, num_samples)
    prev_workout = np.random.randint(0, 2, num_samples)
    hydration = np.random.randint(0, 13, num_samples)
    consistency = np.random.randint(0, 101, num_samples)

    # Target: skip_next_workout (1 = skip, 0 = do workout)
    # Higher chance to skip if: low sleep, high stress, didn't workout previously, low hydration, low consistency
    prob_skip = (
        (10 - sleep) * 0.1 +
        (stress) * 0.05 +
        (1 - prev_workout) * 0.15 +
        (12 - hydration) * 0.02 +
        (100 - consistency) * 0.003
    )
    # Add some noise
    prob_skip += np.random.normal(0, 0.1, num_samples)
    
    # Normalize probabilities roughly to 0-1
    prob_skip = np.clip(prob_skip, 0, 1)
    
    # Convert probabilities to binary outcomes
    skip_next = np.random.binomial(1, prob_skip)

    df = pd.DataFrame({
        'sleep_hours': sleep,
        'stress_level': stress,
        'previous_workout': prev_workout,
        'hydration': hydration,
        'consistency': consistency,
        'skip_next_workout': skip_next
    })
    return df

def train_and_save_model():
    print("Generating synthetic data...")
    df = create_synthetic_data(2000)
    
    X = df[['sleep_hours', 'stress_level', 'previous_workout', 'hydration', 'consistency']]
    y = df['skip_next_workout']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Training RandomForest model...")
    model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
    model.fit(X_train, y_train)
    
    score = model.score(X_test, y_test)
    print(f"Model accuracy on test set: {score:.2f}")
    
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)
    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    train_and_save_model()
