import pandas as pd
import numpy as np
from gensim import corpora
from Proximity_measures import*

def FreqT_generation(docs): #Takes a set of tokenized words to create a FreqT
    # Create a dictionary based on the preprocessed documents
    dictionary = corpora.Dictionary(docs)

    # Convert the preprocessed documents to a bag-of-words representation
    corpus = [dictionary.doc2bow(doc) for doc in docs]

    # Calculate the term-frequency matrix
    term_frequency_matrix = []

    for doc in corpus:
        row = [0] * len(dictionary)
        for word_id, frequency in doc:
            row[word_id] = frequency
        term_frequency_matrix.append(row)

    # Convert the term-frequency matrix to a Pandas DataFrame
    term_frequency_df = pd.DataFrame(term_frequency_matrix, columns=[dictionary[id] for id in dictionary])
    term_frequency_df_transposed = term_frequency_df.T
    return term_frequency_df_transposed

def apply_svd(tf_matrix, k=2): #Receives a FreqT and a k to apply SVD 
    # Convert the term-frequency DataFrame to a NumPy array
    tf_matrix_np = tf_matrix.to_numpy()

    # Perform SVD on the term-frequency matrix
    U, Sigma, Vt = np.linalg.svd(tf_matrix_np, full_matrices=False)

    # Truncate the U, Sigma, and Vt matrices based on the desired number of components (k)
    U_k = U[:, :k]
    Sigma_k = np.diag(Sigma[:k])
    Vt_k = Vt[:k, :]

    # Compute the reduced matrix by multiplying the truncated U, Sigma, and Vt matrices
    reduced_matrix = U_k @ Sigma_k @ Vt_k

    return reduced_matrix

def find_bestDocs(query, n, preprocessed_docs, sFormula, dFormula):
    similarity_scores = []
    disimilarity_scores = []

    preprocessed_docs.append(query)

    New_FreqT = FreqT_generation(preprocessed_docs)
    print("NEW FREQT WITH Q IS: \n", New_FreqT)

    New_reducedMatrix = apply_svd(New_FreqT, 3)
    printable_new_reduced_matrix_df = pd.DataFrame(New_reducedMatrix, index=New_FreqT.index, columns=New_FreqT.columns)
    print("Reduced Frequency Table (With Query): \n ", printable_new_reduced_matrix_df)

    New_Doc = New_reducedMatrix[:,-1]
    print("NEW DOC IS: ",New_Doc)


    for i, doc in enumerate(range(New_reducedMatrix.shape[1]-1)):
        similarity = calculate_similarity(sFormula,New_reducedMatrix, doc, -1)
        disimilarity = calculate_dissimilarity(dFormula, New_reducedMatrix, doc, -1)

        similarity_scores.append((i,similarity))
        disimilarity_scores.append((i, disimilarity))
    
    similarity_scores.sort(key=lambda x: x[1], reverse=True)
    disimilarity_scores.sort(key=lambda x: x[1])

    N_similarDocs = similarity_scores[:n:]
    N_disimilarDocs = disimilarity_scores[:n:]

    return N_similarDocs, N_disimilarDocs
