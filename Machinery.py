from Libraries import*
from Proximity_measures import*

def QueryChooser(language, retrieved_Docs, processedDocs, FreqT, reduced_FreqT):
    while True:
        print("------CHOOSE QUERY-------- \n What query would you like to perform: \n 1. Compare 2 docs similarity \n 2. Type a query \n 3.Exit")
        qChoice = int(input("Type the number of the option: "))
        
        if qChoice == 1:
            d0 = int(input("Type the indexes of the first doc to compare: "))
            d1 = int(input("Type the indexes of the second doc to compare: "))
            sFormula = (input("Type cosine or jac to obtain similarity: "))
            similarity_2Docs = calculate_similarity(sFormula, reduced_FreqT, d0, d1)
            print(f"The similarity of the two documents using {sFormula} is: ",  similarity_2Docs)
            
        
        elif qChoice == 2:
            n = int(input("Needed documents to retrieve: "))
            natural_q = input("Type the query to lookup: ")

            processed_q = lemmatize(language, natural_q)

            values = find_bestDocs(processed_q, n, processedDocs, "cosine","euc")
            print("Top {} most similar documents:".format(n))
            for idx, score in values[0]:
                print("Document {}: Similarity score = {}".format(idx, score))

            print("\nTop {} most dissimilar documents:".format(n))
            for idx, score in values[1]:
                print("Document {}: Dissimilarity score = {}".format(idx, score))

                
        elif qChoice == 3:
            print("Return")
            break

def LibraryChooser():
    while True:
        print("------------------------MAIN MENU-------------------- \n Choose your library: \n 1. English \n 2. French \n 3.Exit")
        library = int(input("Type the number of the option: "))

        if library == 1:
            language = "EN"
            retrieved_Docs, processedDocs, FreqT, reduced_FreqT = launch_Library(language)
            print(QueryChooser(language, retrieved_Docs, processedDocs, FreqT, reduced_FreqT))
            


        elif library == 2:
            language = "FR"
            retrieved_Docs, processedDocs, FreqT, reduced_FreqT = launch_Library(language)
            print(QueryChooser(language, retrieved_Docs, processedDocs, FreqT, reduced_FreqT))

        elif library == 3:
            print("Bye!")
            break
        else:
            print("Not valid, try again")


LibraryChooser()

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