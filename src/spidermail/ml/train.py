from pathlib import Path
import joblib
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


BASE_DIR = Path(__file__).resolve().parents[3]
DATA_PATH = BASE_DIR / "data" / "raw" / "emails.csv"
MODEL_DIR = BASE_DIR / "models"
MODEL_PATH = MODEL_DIR / "spidermail_model.joblib"


def train() -> None:
    df = pd.read_csv(DATA_PATH)

    if "text" not in df.columns or "label" not in df.columns:
        raise ValueError("Le CSV doit contenir les colonnes 'text' et 'label'.")

    model = Pipeline([
        ("vectorizer", TfidfVectorizer(lowercase=True, stop_words="english", ngram_range=(1, 2))),
        ("classifier", LogisticRegression(max_iter=1000))
    ])

    model.fit(df["text"], df["label"])

    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print(f"Model saved to: {MODEL_PATH}")


if __name__ == "__main__":
    train()
