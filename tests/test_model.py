from src.spidermail.ml.predict import SpiderMailPredictor


def test_predict_returns_expected_keys():
    predictor = SpiderMailPredictor()
    result = predictor.predict("Verify your password immediately using this urgent link.")

    assert "label" in result
    assert "phishing_score" in result


def test_predict_label_is_valid():
    predictor = SpiderMailPredictor()
    result = predictor.predict("Hello, please find the meeting notes attached.")

    assert result["label"] in {"safe", "phishing"}
