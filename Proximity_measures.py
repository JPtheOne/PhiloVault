import numpy as np
from  scipy.spatial.distance import *

def calculate_similarity(formula, matrix, col1,col2):
    vec1 = matrix[:, col1]
    vec2 = matrix[:, col2]

    if formula == "cosine":
        distance = 1-cosine(vec1, vec2)
    elif formula == "dice":
        distance = dice(vec1, vec2)
    elif formula == "Jac":
        distance = jaccard(vec1, vec2)  
    elif formula == "inner" :
        distance = np.inner(vec1, vec2)
    return distance

def calculate_dissimilarity(formula, matrix, col1,col2):
    vec1 = matrix[:, col1]
    vec2 = matrix[:, col2]

    if formula == "cosine":
        distance = cosine(vec1, vec2)
    elif formula == "euc":
        distance = euclidean(vec1, vec2)
    elif formula == "man":
        distance = cityblock(vec1,vec2)
    return distance

