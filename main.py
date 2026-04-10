from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.model import train_model
from src.visualization import plot_confusion_matrix

def main():
    data = load_data("data/kdd.csv")

    data = preprocess_data(data)

    model, X_test, y_test, y_pred = train_model(data)

    plot_confusion_matrix(y_test, y_pred)

    print("🚨 Threat Detection System Completed!")

if __name__ == "__main__":
    main()