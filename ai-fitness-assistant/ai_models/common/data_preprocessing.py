import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler


class DataPreprocessor:

    def __init__(self):
        self.label_encoders = {}
        self.scaler = StandardScaler()

    def encode_columns(self, df: pd.DataFrame, columns: list):
        """
        Encode categorical columns
        """
        for col in columns:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            self.label_encoders[col] = le
        return df

    def scale_features(self, df: pd.DataFrame, columns: list):
        """
        Normalize numerical columns
        """
        df[columns] = self.scaler.fit_transform(df[columns])
        return df

    def preprocess(self, df: pd.DataFrame, cat_cols: list, num_cols: list):
        df = self.encode_columns(df, cat_cols)
        df = self.scale_features(df, num_cols)
        return df