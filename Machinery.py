from Libraries import*

def MenuDisplayer():
    while True:
        print("------------------------MAIN MENU-------------------- \n Choose your library: \n 1. English \n 2. French \n 3.Exit")
        library = int(input("Type the number of the option: "))

        if library == 1:
            launch_Library("EN")

            
        elif library == 2:
            pass
        elif library == 3:
            print("Bye!")
            break
        else:
            print("Not valid, try again")


MenuDisplayer()

'''
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
n = 4
sFormula = "cosine"
dFormula = "euc"

scores = find_bestDocs(query, n, preprocessed_docs, sFormula, dFormula)
similar_docs, dissimilar_docs = scores

print(f"Top N similar documents calculates using {sFormula}:")
for index, score in similar_docs:
    print(f"doc {index}: similarity = {score}")

print(f"Top N dissimilar documents calculates using {dFormula}:")
for index, score in dissimilar_docs:
    print(f"doc {index}: dissimilarity = {score}")
'''