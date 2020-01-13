from Utils import *
from Compression import *
import os
from PreprocessingData import PreprocessPipeline
from nltk.stem import WordNetLemmatizer, SnowballStemmer
import math
import sys



preProcessor = PreprocessPipeline()
preProcessor.addStep(lambda tokens:lemmatizer_Wordnet(tokens))
#preProcessor.addStep(lambda tokens:stemming_Porter(tokens))
# Calculates The tf, iDf and tf*Idf for each token in document
# params : text : [string]
#          posting : [string]
# returns : [string]
def calculateTfIdf(tokens, posting):
    metrics = {}
    freqDist = tokens_frequencies(tokens)
    for key in freqDist:
        # calculate the tf.idf coefficient per ratio
        tf = 1 + math.log10(freqDist[key])
        idf = math.log10(DocId.ID/posting[key][1])
        metrics[key] = [tf, idf, tf*idf]
    return metrics

# Calculates The tf, iDf and tf*Idf for each token in all documents
# params : corpus : [[string]]
# returns : [string]
def globalTfIdf(corpus):
    termFreq = {}
    for text in corpus:
        txt = preProcessor.process(text)
        freqDist = tokens_frequencies(txt)
        termFreq = mergeDict(termFreq, freqDist)
    return termFreq

# Merges two dictionnaries
# params : dict1 : dict
#          dict2 : dict
# returns : [string]
def mergeDict(dict1, dict2):
    id = DocId.assign()
    for key, value in dict2.items():
        if not key in dict1.keys():
            dict1[key] = [value, 1, (id, value)]
        else:
            dict1[key][0] += value
            dict1[key][1] += 1
            dict1[key].append((id, value))
    return dict1


def calculateSimilarity(query, posting):
    total = {}
    for key in query:
        widf = query[key][1]
        tagInfo = posting[key][2:]
        tagMetrics = [(x[0], query[key][2] * (x[1] * widf)) for x in tagInfo]
        for x in tagMetrics:
            if x[0] in total.keys():
                total[x[0]] += x[1]
            else:
                total[x[0]] = x[1]
    print(total)
    return sorted(total, reverse=True)

def compressIndex(posting):
    pass

if __name__ == "__main__":
    limit = 10788
    try:
        limit = int(sys.argv[1])
    except:
        print("[Warning] : No limit is provided, using all dataset")
    corpus_keys = nltk.corpus.reuters.fileids()[:limit]
    corpus = [nltk.corpus.reuters.raw(id) for id in corpus_keys]
    freq = globalTfIdf(corpus)
    # Compress and store Posting
    encodePostingToFile({'totalDoc':DocId.ID,'index':freq},'Test.bin')

    #print(freq)
    #query = "crisis"

    #processedQuery = preProcessor.process(query)
    #print(processedQuery)
    #queryMetrics = calculateTfIdf(processedQuery, freq)

    #docs = calculateSimilarity(queryMetrics, freq)
    #print(docs)

    #for docID in docs:
        #print("\n\n-------------------\n"+corpus[docID-1])