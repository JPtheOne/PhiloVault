from FreqT_methods import *
from Proximity_measures import*

#-----------------------Testing Methods--------------------------#
preprocessed_docs = [
    ['survey',"god"],
    ['survey',"god"], 
    ['survey', 'user', 'computer', 'cat', 'cat', 'bird','bird'],
    ['survey', 'user', 'computer', 'system', 'response', 'time']
                    ]

FreqT = (FreqT_generation(preprocessed_docs))
print("Frequency Table: \n",FreqT)

# Call your FreqT_generation method to obtain the term-frequency matrix
term_frequency_matrix = FreqT_generation(preprocessed_docs)

# Apply SVD to the term-frequency matrix and get the reduced matrix
reduced_matrix = apply_svd(term_frequency_matrix, 3)

# Convert the reduced matrix back to a Pandas DataFrame with the same format as the input term-frequency matrix
printable_reduced_matrix_df = pd.DataFrame(reduced_matrix, index=term_frequency_matrix.index, columns=term_frequency_matrix.columns)

print("Reduced Frequency Table: \n ", printable_reduced_matrix_df)

mtx = reduced_matrix
formula = "inner"
#print(f"{formula} similarity: ", calculate_similarity(formula, mtx, 0,1))

formula = "cosine"
#print(f"{formula} disimilarity: ", calculate_dissimilarity(formula, mtx, 0,1))


query  = ["survey","god"]
print("Query is: ", query)
n = 2

def find_bestDocs(query, n, preprocessed_docs):
    similarity_scores = []

    preprocessed_docs.append(query)

    New_FreqT = FreqT_generation(preprocessed_docs)
    print("NEW FREQT WITH Q IS: \n", New_FreqT)

    New_reducedMatrix = apply_svd(New_FreqT, 3)
    printable_new_reduced_matrix_df = pd.DataFrame(New_reducedMatrix, index=New_FreqT.index, columns=New_FreqT.columns)
    print("Reduced Frequency Table (With Query): \n ", printable_new_reduced_matrix_df)

    New_Doc = reduced_matrix[:,-1]
    print("NEW DOC IS: ",New_Doc)


    for i, doc in enumerate(range(New_reducedMatrix.shape[1]-1)):
        similarity = calculate_similarity("Jac",New_reducedMatrix, doc, -1)
        similarity_scores.append(similarity)
    
    return similarity_scores


scores = (find_bestDocs(query, n, preprocessed_docs))
print("Comparisons with New doc and other docs are: ", scores)