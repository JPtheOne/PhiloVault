
import spacy
def lemmatize(language, text):
    nlp_en = spacy.load("en_core_web_sm")
    nlp_fr = spacy.load("fr_core_news_sm")

    if language == "en":
        doc = nlp_en(text)
    elif language == "fr":
        doc = nlp_fr(text)

    lemmas = [token.lemma_ for token in doc if not (token.is_stop or token.is_punct) and token.lemma_.isalpha()]
    return lemmas

#Testing lemmatizer function
text1 = "Dinosaurs dinosaurs dinosaurs are a diverse group of reptiles[note 1] of the clade Dinosauria. They first appeared during the Triassic period, between 245 and 233.23 million years ago (mya), although the exact origin and timing of the evolution of dinosaurs is a subject of active research. They became the dominant terrestrial vertebrates after the Triassic–Jurassic extinction event 201.3 mya and their dominance continued throughout the Jurassic and Cretaceous periods. "
text2 = "La classification standard des dinosaures distingue deux grands clades selon la morphologie de leur bassin : les Ornithischia et les Saurischia. Les Ornithischia (ou Ornithischiens) ne comprennent que des dinosaures herbivores que les paléontologues divisent en trois groupes majeurs "

preprocess = print(lemmatize("fr", text2))


 
