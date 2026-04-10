from pathlib import Path
import joblib


BASE_DIR = Path(__file__).resolve().parents[3]
MODEL_PATH = BASE_DIR / "models" / "spidermail_model.joblib"
PHISHING_THRESHOLD = 0.45


class SpiderMailPredictor:
    def __init__(self) -> None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                "Le modèle n'existe pas encore. Lance d'abord train.py."
            )
        self.model = joblib.load(MODEL_PATH)

    def predict(self, text: str) -> dict:
        if not text or not text.strip():
            raise ValueError("Le texte ne peut pas être vide.")

        phishing_score = float(self.model.predict_proba([text])[0][1])
        label = "phishing" if phishing_score >= PHISHING_THRESHOLD else "safe"

        return {
            "label": label,
            "phishing_score": round(phishing_score, 4),
            "threshold": PHISHING_THRESHOLD
        }
