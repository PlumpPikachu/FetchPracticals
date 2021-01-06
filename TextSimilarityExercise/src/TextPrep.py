import string
import sys
import os
import SimilarityConfig as cfg

"""
    Prepares a document for processing, performing common operations such as removing stop words and punctuation,
    tokenizing, etc.
"""
def CleanDocument(doc):

    docRet = doc.lower()
    docRet = RemovePunctuation(docRet)
    docRet = TokenizeDocument(docRet)
    docRet = RemoveStopwords(docRet)

    return docRet

"""
    Removes punctutation as defined by string.punctuation
"""
def RemovePunctuation(doc):
    return doc.translate(str.maketrans('', '', string.punctuation))

"""
    Tokenizes document with punctuation removed
"""
def TokenizeDocument(doc):
    return doc.split(' ')

"""
    Removes stopwords from tokenized document, as defined in stopwords.txt
"""
def RemoveStopwords(doc):

    # grab list of stopwords
    stopwords = []
    with open(os.path.join(sys.path[0], cfg.STOPWORD_FILE_NAME), 'r') as f:
        for word in f:
            word = word.split('\n')
            stopwords.append(word[0])

    # remove from doc and return doc
    return [word for word in doc if word not in stopwords]