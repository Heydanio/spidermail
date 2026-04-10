import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="SpiderMail", page_icon="🕷️")
st.title("🕷️ SpiderMail")
st.write("Analyse un email et estime s’il ressemble à un phishing.")

email_text = st.text_area("Colle ici le contenu de l'email", height=220)

if st.button("Analyser"):
    if not email_text.strip():
        st.warning("Le texte est vide.")
    else:
        response = requests.post(API_URL, json={"text": email_text}, timeout=10)

        if response.status_code == 200:
            result = response.json()
            st.subheader("Résultat")
            st.write(f"**Label :** {result['label']}")
            st.write(f"**Phishing score :** {result['phishing_score']}")
        else:
            st.error(f"Erreur API : {response.text}")
