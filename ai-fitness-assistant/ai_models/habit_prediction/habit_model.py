import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from ..common.model_utils import save_model


MODEL_PATH = "ai_models/habit_prediction/habit_model.pkl"


def train_habit_model(dataset_path):

    df = pd.read_csv(dataset_path)

    X = df.drop("target", axis=1)
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100)

    model.fit(X_train, y_train)

    save_model(model, MODEL_PATH)

    accuracy = model.score(X_test, y_test)

    return {
        "accuracy": accuracy,
        "model_path": MODEL_PATH
    }