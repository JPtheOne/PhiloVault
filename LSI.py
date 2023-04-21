from gensim import corpora, models

# Assume you have a list of preprocessed documents called preprocessed_docs
preprocessed_docs = [
    ['human', 'interface', 'computer'],
    ['survey', 'user', 'computer', 'system', 'response', 'time'],
    # More preprocessed documents here...
]

# Create a dictionary based on the preprocessed documents
dictionary = corpora.Dictionary(preprocessed_docs)

# Convert the preprocessed documents to a bag-of-words representation
corpus = [dictionary.doc2bow(doc) for doc in preprocessed_docs]

# Print the Document-Term Matrix
print("Document-Term Matrix:")
for doc in corpus:
    print([dictionary[id] for id, _ in doc], doc)

# Create and apply the LSI model
lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)
corpus_lsi = lsi[corpus]

# Print the topics and their corresponding weights
print("\nLSI Topics:")
print(lsi.print_topics(num_topics=2))

# Print the LSI representation for each document
print("\nLSI Representation:")
for doc, as_text in zip(corpus_lsi, preprocessed_docs):
    print(doc, as_text)


