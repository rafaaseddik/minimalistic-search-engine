from Compression import *
from IndexingData import *

posting = {'asian': [2, 1, (1, 2)], 'exporter': [4, 2, (1, 3), (29, 1)], 'fear': [2, 1, (1, 2)], 'damage': [6, 4, (1, 2), (35, 1), (53, 2), (79, 1)]}
result = {}
#Encode IT
for key in posting:
    gapEncoded = GapEncoding(posting)[key]
    binary_encoded = EncodeArrayGamma(PostingToArray(gapEncoded))
    result[key]= binary_encoded
print(result)

# Decode IT
result2 = {}
for key in result.keys():
        decompressedList = GammaDecoding(result[key])
        node = decompressedList[:2]
        decompressedList = decompressedList[2:]
        while(len(decompressedList)>=2):
            node.append((decompressedList[0],decompressedList[1]))
            if(len(decompressedList) is 2):
                break
            else:
                decompressedList = decompressedList[2:]
        result2[key] = node
print(GapDecoding(result2))

