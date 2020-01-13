import pickle
## GAP
def GapEncoding(decoded):
    result = {}
    for key in decoded.keys():
        # Get The token's posting
        toEncode = decoded[key]
        # Initialise token's result
        encoded = [toEncode[0],toEncode[1],[]]
        encoded[2] = toEncode[2]
        # Gap Encoding Algorithm
        lastIndex = toEncode[2][0]
        for doc in toEncode[3:]:
            encoded.append((doc[0]-lastIndex,doc[1]))
            lastIndex = doc[0]
        result[key] = encoded
    return result

def GapDecoding(encoded):
    result = {}
    for key in encoded.keys():
        # Get The token's posting
        toDecode = encoded[key]
        # Initialise token's result
        decoded = [toDecode[0],toDecode[1],[]]
        decoded[2] = toDecode[2]
        # Gap Encoding Algorithm
        lastIndex = toDecode[2][0]
        for doc in toDecode[3:]:
            decoded.append((doc[0]+lastIndex,doc[1]))
            lastIndex = doc[0]+lastIndex
        result[key] = decoded
    return result

def     PostingToArray(posting):
    result = posting[:2]
    for element in posting[2:]:
        result.append(element[0])
        result.append(element[1])
    return result

def GammaEncoding(number):
    binaryRep = bin(number)[2:]
    length = ''.join(['1' for i in range(len(binaryRep)-1)])+'0'
    return length + binaryRep[1:]
def GammaDecoding(binary):
    result = []
    while(len(binary)):
        firstZeroIndex = binary.find('0')
        decoded = int('1'+binary[firstZeroIndex+1:2*firstZeroIndex+1],2)
        result.append(decoded)
        binary = binary[2*firstZeroIndex+1:]
    return result
    
def EncodeArrayGamma(array):
    return ''.join([GammaEncoding(e) for e in array])

def encodePostingToFile(allData,filename):
    with open('original'+filename, 'wb') as f:
        pickle.dump(allData, f, protocol=pickle.HIGHEST_PROTOCOL)
    result = {}
    for key in allData['index'].keys():
        gapEncoded = GapEncoding( allData['index'])[key]
        binary_encoded = EncodeArrayGamma(PostingToArray(gapEncoded))
        bit_strings = [binary_encoded[i:i + 8] for i in range(0, len(binary_encoded), 8)]
        byte_list = [int(b, 2) for b in bit_strings]
        if(key=="damage"):
            print(key , byte_list)
        result[key]= byte_list
    allData['index'] = result
    with open(filename, 'wb') as f:
        pickle.dump(allData, f, protocol=pickle.HIGHEST_PROTOCOL)
    return result

def encodePostingToFileNew(allData,filename):
    with open('original'+filename, 'wb') as f:
        pickle.dump(allData, f, protocol=pickle.HIGHEST_PROTOCOL)
    result = {}
    for key in allData['index'].keys():
        gapEncoded = GapEncoding( allData['index'])[key]
        binary_encoded = EncodeArrayGamma(PostingToArray(gapEncoded))
        result[key]= binary_encoded
    allData['index'] = result
    with open(filename, 'wb') as f:
        pickle.dump(allData, f, protocol=pickle.HIGHEST_PROTOCOL)
    return result

def fromBinaryToIntArray(binary):
    #binary_coded = ''.join([bin(e)[2:] for e in binary])
    binary_string = ''
    for i in range(len(binary)):
        binary_code = bin(binary[i])[2:]
        if(i is not len(binary)-1 and len(binary_code) <8):
            # must add leading 0
            binary_code = ''.join(['0' for i in range(8-len(binary_code))]) + binary_code
        binary_string = binary_string + binary_code
    return binary_string

def loadIndex(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def DecompressIndex(encodedIndex):
    result = {}
    for key in list(encodedIndex.keys())[:10]:
        decompressedList = GammaDecoding(fromBinaryToIntArray(encodedIndex[key]))
        node = decompressedList[:2]
        decompressedList = decompressedList[2:]
        while(len(decompressedList)>=2):
            node.append((decompressedList[0],decompressedList[1]))
            if(len(decompressedList) is 2):
                break
            else:
                decompressedList = decompressedList[2:]
        result[key] = node
    print(result)
    return GapDecoding(result)
def DecompressIndexNew(encodedIndex):
    result = {}
    for key in list(encodedIndex.keys())[:10]:
        decompressedList = GammaDecoding(encodedIndex[key])
        node = decompressedList[:2]
        decompressedList = decompressedList[2:]
        while(len(decompressedList)>=2):
            node.append((decompressedList[0],decompressedList[1]))
            if(len(decompressedList) is 2):
                break
            else:
                decompressedList = decompressedList[2:]
        result[key] = node
    return GapDecoding(result)