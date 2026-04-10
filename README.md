# SpiderMail

SpiderMail is a lightweight AI-powered phishing detection project.

## Features

- Email text classification
- FastAPI backend
- Streamlit demo UI
- Simple ML pipeline with scikit-learn
- Pytest test suite

## Run

Train the model:

    python src/spidermail/ml/train.py

Run the API:

    fastapi dev src/spidermail/api/main.py

Run the UI:

    streamlit run src/spidermail/ui/app.py

Run tests:

    pytest
