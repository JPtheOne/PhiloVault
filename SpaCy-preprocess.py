import spacy

nlp_en = spacy.load("en_core_web_sm")
nlp_fr = spacy.load("fr_core_news_sm")

text_en = "Dinosaurs dinosaurs dinosaurs are a diverse group of reptiles[note 1] of the clade Dinosauria. They first appeared during the Triassic period, between 245 and 233.23 million years ago (mya), although the exact origin and timing of the evolution of dinosaurs is a subject of active research. They became the dominant terrestrial vertebrates after the Triassic–Jurassic extinction event 201.3 mya and their dominance continued throughout the Jurassic and Cretaceous periods. "
text_fr = """Je te l’ai dit pour les nuages, Je te l’ai dit pour l’arbre de la mer , Pour chaque vague pour les oiseaux dans les feuilles, Pour les cailloux du bruit, Pour les mains familières"""

doc_en = nlp_en(text_en)
doc_fr = nlp_fr(text_fr)

# Lemmatize and filter out stop words,  punctuation marks, numbers and symbols and punctuation
lemmas_en = [token.lemma_ for token in doc_en if not (token.is_stop or token.is_punct) and token.lemma_.isalpha()]
lemmas_fr = [token.lemma_ for token in doc_fr if not (token.is_stop or token.is_punct) and token.lemma_.isalpha()]


print("LEMMATIZED, STOP WORDS AND PUNCTUATION REMOVED ENGLISH TEXT: ", lemmas_en)
print("LEMMATIZED, STOP WORDS AND PUNCTUATION REMOVED FRENCH TEXT: ", lemmas_fr)