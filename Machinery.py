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
            dFormula = (input("Type euc or man to obtain dissimilarity: "))

            similarity_2Docs = calculate_similarity(sFormula, reduced_FreqT, d0, d1)
            print(f"The similarity of the two documents using {sFormula} is: ",  similarity_2Docs)

            dissimilarity_2Docs = calculate_dissimilarity(dFormula, reduced_FreqT, d0, d1)
            print(f"The dissimilarity of the two documents using {dFormula} is: ",  dissimilarity_2Docs)

            
        
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


