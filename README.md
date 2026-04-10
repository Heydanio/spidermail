# 🕷️ SpiderMail

**SpiderMail** is a lightweight AI-powered phishing detection project built to analyze suspicious emails and estimate whether a message is likely to be phishing.

## Features

- phishing vs safe email classification
- FastAPI backend
- Streamlit web interface
- local model training pipeline
- automated tests with pytest

## Tech Stack

- Python 3.11
- FastAPI
- scikit-learn
- pandas
- Streamlit
- pytest

## Project Structure

```text
spidermail/
├─ data/
│  └─ raw/
├─ models/
├─ src/
│  └─ spidermail/
│     ├─ api/
│     ├─ ml/
│     └─ ui/
├─ tests/
├─ README.md
└─ requirements.txt
```

## Setup

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

## Train the model

```bash
python src/spidermail/ml/train.py
```

## Run the API

```bash
fastapi dev src/spidermail/api/main.py
```

API docs:

```text
http://127.0.0.1:8000/docs
```

## Run the UI

```bash
streamlit run src/spidermail/ui/app.py
```

## Run tests

```bash
pytest
```

## Example

Input:

> Urgent: verify your password immediately using this secure link.

Output:

- label: phishing
- phishing_score: high

## Why this project

SpiderMail was built as a cybersecurity portfolio project to demonstrate practical skills in:

- machine learning
- phishing detection
- API development
- testing
- clean project structure

## Roadmap

- improve the dataset
- support multilingual email analysis
- explain suspicious indicators
- extract risky keywords and links
- add Docker support
- add GitHub Actions CI
- improve UI and branding

## Disclaimer

This project is for educational and portfolio purposes only.
