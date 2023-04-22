import pandas as pd
import numpy as np
from gensim import corpora

def FreqT_generation(docs):
    # Create a dictionary based on the preprocessed documents
    dictionary = corpora.Dictionary(preprocessed_docs)

    # Convert the preprocessed documents to a bag-of-words representation
    corpus = [dictionary.doc2bow(doc) for doc in preprocessed_docs]

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


preprocessed_docs = [
    ['survey', 'user', 'computer', 'cat', 'cat', 'bird','bird'],
    ['survey', 'user', 'computer', 'system', 'response', 'time'],
    ['survey']

    # More preprocessed documents here...
]

FreqT = (FreqT_generation(preprocessed_docs))
print("Frequency Table: \n",FreqT)

def apply_svd(tf_matrix, k=2):
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

# Call your FreqT_generation method to obtain the term-frequency matrix
term_frequency_matrix = FreqT_generation(preprocessed_docs)

# Choose the desired number of components (k)
k = 3

# Apply SVD to the term-frequency matrix and get the reduced matrix
reduced_matrix = apply_svd(term_frequency_matrix, k)

# Convert the reduced matrix back to a Pandas DataFrame with the same format as the input term-frequency matrix
printable_reduced_matrix_df = pd.DataFrame(reduced_matrix, index=term_frequency_matrix.index, columns=term_frequency_matrix.columns)

print("Reduced Frequency Table: ")
print(printable_reduced_matrix_df)
