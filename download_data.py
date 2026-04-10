from sklearn.datasets import fetch_kddcup99
import pandas as pd

print("Downloading dataset...")

data = fetch_kddcup99(percent10=True, as_frame=True)

df = data.frame

print("Download complete!")

# Save as CSV
df.to_csv("data/kdd.csv", index=False)

print("Dataset saved to data/kdd.csv")