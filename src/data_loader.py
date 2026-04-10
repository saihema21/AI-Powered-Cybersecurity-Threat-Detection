import pandas as pd

def load_data(path):
    print("Loading dataset...")

    # 41 features + 1 label
    columns = [f"feature_{i}" for i in range(41)] + ["label"]

    data = pd.read_csv(path, names=columns)

    print("Dataset Loaded Successfully!")
    print("Shape:", data.shape)
    print(data.head())

    return data