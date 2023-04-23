
import spacy

def lemmatize(language, text):
    nlp_en = spacy.load("en_core_web_sm")
    nlp_fr = spacy.load("fr_core_news_sm")

    if language == "EN":
        doc = nlp_en(text)
    elif language == "FR":
        doc = nlp_fr(text)

    lemmas = [token.lemma_ for token in doc if not (token.is_stop or token.is_punct) and token.lemma_.isalpha()]
    return lemmas



 
