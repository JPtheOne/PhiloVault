import numpy as np
from  scipy.spatial.distance import *

def calculate_similarity(formula, matrix, col1,col2):   #Takes the formula a reduced matrix and two documents 
                                                        # to return the similarity
    vec1 = matrix[:, col1]
    vec2 = matrix[:, col2]

    if formula == "cosine": #-1 means different, 0 orthogonal, 1 identical
        similarity = 1-cosine(vec1, vec2)
    elif formula == "Jac": #0 different, 1 identical
        similarity = jaccard(vec1, vec2)  
    elif formula == "inner" :#0 different, 1 identical
        vec1_normalized = vec1 / np.linalg.norm(vec1)
        vec2_normalized = vec2 / np.linalg.norm(vec2)
        similarity = np.inner(vec1_normalized, vec2_normalized)
    return similarity

def calculate_dissimilarity(formula, matrix, col1,col2): #Same as above but with dissimilarity
    vec1 = matrix[:, col1]
    vec2 = matrix[:, col2]

    if formula == "cosine":
        distance = cosine(vec1, vec2)
    elif formula == "euc": # Smaller means greater similarity
        distance = euclidean(vec1, vec2)
    elif formula == "man": #Smaller means greater similarity
        distance = cityblock(vec1,vec2)
    return distance
