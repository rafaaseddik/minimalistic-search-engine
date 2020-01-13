from Compression import *
from IndexingData import *
import sys
import nltk
if __name__ == "__main__":
    
    corpus_keys = nltk.corpus.reuters.fileids()
    corpus = [nltk.corpus.reuters.raw(id) for id in corpus_keys]

    allData = loadIndex('Test.bin')
    index = DecompressIndex(allData['index'])
    print(index)
    """DocId.ID = allData['totalDoc']
    query = ' '.join(sys.argv[1:])
    print(query)
    processedQuery = preProcessor.process(query)
    print(processedQuery)
    queryMetrics = calculateTfIdf(processedQuery, index)

    docs = calculateSimilarity(queryMetrics, index)
    print(docs)

    for docID in docs:
        print("\n\n-------------------DOC ID : "+str(docID)+"\n"+corpus[docID-1])"""