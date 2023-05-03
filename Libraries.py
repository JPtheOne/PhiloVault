from DB.SQL_methods import get_docContent
from Preprocess import lemmatize
from FreqT_methods import*

def launch_Library(language):
    # 1.Retrieving doc content from DB
    retrieved_Docs = get_docContent(language)

    # 2. Process language for indexing purposes
    processedDocs = [lemmatize(language, doc) for doc in retrieved_Docs]
    print("Amount of processed and retrieved docs in this language: ", len(processedDocs))
    
    #3. Create FreqT and reduce it through SVD
    FreqT = (FreqT_generation(processedDocs))
    print("The FreqT of those docs is: \n",FreqT)

    reduced_FreqT = apply_svd(FreqT, 3)
    print("The FreqT has been reduced through SVD to apply LSI. Ready to query")

    return retrieved_Docs, processedDocs, FreqT, reduced_FreqT

def launch_visualLibrary(language):
    # 1.Retrieving doc content from DB
    retrieved_Docs = get_docContent(language)

    # 2. Process language for indexing purposes
    processedDocs = [lemmatize(language, doc) for doc in retrieved_Docs]
    
    #3. Create FreqT and reduce it through SVD
    FreqT = (FreqT_generation(processedDocs))

    reduced_FreqT = apply_svd(FreqT, 3)

    return retrieved_Docs, processedDocs, FreqT, reduced_FreqT

