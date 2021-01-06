import math
import TextSimilarityExercise.src.TextPrep as prep

"""
    Gets cosine similarity of two documents
"""
def GetCosineSimilarity(doc1, doc2):
    # wrapper function to clean documents and return jaccard similarity

    cleanDoc1 = prep.CleanDocument(doc1)
    cleanDoc2 = prep.CleanDocument(doc2)

    docVec1, docVec2 = __bagOfWords__(cleanDoc1, cleanDoc2)

    return __cosineSimilarity__(docVec1, docVec2)

"""
    Calculates cosine similarity of two L2 normed, equal length document vectors
"""
def __cosineSimilarity__(vec1, vec2):
    # just a wrapper for good naming because in the case where vectors are L2 normed, cosine similarity is just
    # their dot product according to:
    # https://stackoverflow.com/questions/51290969/is-there-any-reason-to-not-l2-normalize-vectors-before-using-cosine-similarity

    return __dotProduct__(vec1, vec2)

"""
    Uses vanilla Python to get the dot product of two vectors
"""
def __dotProduct__(vec1, vec2):

    if len(vec1) != len(vec2):
        raise Exception("Vectors must be equal length to take dot product")

    return sum(i * j for i, j in zip(vec1, vec2))

"""
    Uses Bag of Words to turn word vectors into numeric vectors. Note that we normalize the vectors before
    returning them, using L2
"""
def __bagOfWords__(doc1, doc2):

    # unique words across both docs
    voc = set(doc1).union(set(doc2))

    # word count vectors
    bagVector1 = __countWords__(doc1, voc)
    bagVector2 = __countWords__(doc2, voc)

    # normalize the vectors so that big differences in length between documents
    normVector1 = __L2__(bagVector1)
    normVector2 = __L2__(bagVector2)

    return normVector1, normVector2

"""
    Takes vector and returns an L2 normalized copy
"""
def __L2__(vec):
    # Given a vector, the L2 norm of that vector is: sqrt(sum(vector**vector))
    # to normalize the vector, we calculate: vector / L2norm
    sqrt = math.sqrt(sum(vec))

    return [i / sqrt for i in vec]

"""
    Quick method for counting the number of times a word in a given corpus appears in a document
"""
def __countWords__(doc, voc):

    count = dict.fromkeys(voc, 0)
    for word in doc:
        count[word] += 1

    return count.values()

