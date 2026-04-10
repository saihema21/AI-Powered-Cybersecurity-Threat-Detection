import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    print("Preprocessing data...")

    # Convert label: normal = 0, attack = 1
    df['label'] = df['label'].apply(lambda x: 0 if x == 'normal' else 1)

    # Encode categorical columns
    for col in df.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])

    print("Preprocessing complete!")
    print(df.head())
    print("\nLabel Distribution:")
    print(df['label'].value_counts())

    return df