import string
import math
import sys
import TextSimilarityExecise.SimilarityConfig as cfg

"""
    Gets cosine similarity of two documents
"""
def GetCosineSimilarity(doc1, doc2):
    # wrapper function to clean documents and return jaccard similarity

    cleanDoc1 = __cleanDocument__(doc1)
    cleanDoc2 = __cleanDocument__(doc2)

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

    return sum(p * q for p, q in zip(vec1, vec2))

"""
    Uses Bag of Words to turn document iterables into numeric vectors. Note that we normalize the vectors before
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
    Takes two vectors and normalizes them using L2
"""
def __L2__(vec):
    # Given a vector, the L2 norm of that vector is the sqrt of the sum of its squares
    # we divide the vector by this norm to normalize it
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

"""
    Prepares a document for processing, performing common operations such as removing stop words and punctuation,
    tokenizing, etc.
"""
def __cleanDocument__(doc):

    docRet = doc.lower()
    docRet = __removePunctuation__(docRet)
    docRet = __tokenizeDocument__(docRet)
    docRet = __removeStopwords__(docRet)

    return docRet

"""
    Removes punctutation as defined by string.punctuation
"""
def __removePunctuation__(doc):
    return doc.translate(str.maketrans('', '', string.punctuation))

"""
    Tokenizes document with punctuation removed
"""
def __tokenizeDocument__(doc):
    return doc.split(' ')

"""
    Removes stopwords from tokenized document, as defined in stopwords.txt
"""
def __removeStopwords__(doc):

    # grab list of stopwords
    stopwords = []
    with open(cfg.STOPWORD_FILE_NAME, 'r') as f:
        for word in f:
            word = word.split('\n')
            stopwords.append(word[0])

    # remove from doc and return doc
    return [word for word in doc if word not in stopwords]