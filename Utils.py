import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.stem import SnowballStemmer
from nltk import PorterStemmer
from nltk import WordNetLemmatizer

stop_words = set(stopwords.words('english')) 

# Transform all text to lowercaase
# params : text : string
# returns : string
def to_lower(text):
    return text.lower()

# Transforms text to list of words
# params : text : string
# returns : [string]
def tokenize_text(text):
    return nltk.word_tokenize(text)

# Transforms list of words to dictionnary representing each word's frequency
# params : tokens_list : [string]
# returns : {string:int}
def tokens_frequencies(tokens_list):
    return nltk.FreqDist(tokens_list)

# Returns most frequent word in tokens list and it's frequency
# params : tokens_list : [string]
# returns : [string,int]
def most_frequent_token(tokens_list):
    frequencies_dict = tokens_frequencies(tokens_list)
    result_token,result_frequency  = 'none' , 0
    for token in frequencies_dict.keys():
        frequency = frequencies_dict[token]
        if(len(token)>4 and frequency>result_frequency):
            result_token,result_frequency = token, frequency
    return result_token,result_frequency

# Returns if provided word is a stopword
# params : word : string
# returns : bool
def is_stopword(word):
    return (word in stop_words)

# Returns list of sentences in the provided text
# params : text : string
# returns : [string]
def get_sententences(text):
    return sent_tokenize(text)

# Returns list of tagged tokens
# params : tokens : [string]
# returns : [[string,string]]
def get_tags(tokens):
    return nltk.pos_tag(tokens)

# Returns Stemmed Tokens with Porter Algorithm
# params : tokens : [string]
# returns : [string]
def stemming_Porter(tokens):
    Stemmer = PorterStemmer()
    return [Token(Stemmer.stem(word.token),word.pos,forceToken=True) for word in tokens]

# Returns Stemmed Tokens with Porter Algorithm
# params : tokens : [string]
# returns : [string]
def stemming_Snowball(tokens):
    Stemmer  = SnowballStemmer('english')
    return [Token(Stemmer.stem(word.token),word.pos,forceToken=True) for word in tokens]

# Returns Lemmatized tokens using wordnet lemmatizer
# params : tokens : [string]
# returns : [string]
def lemmatizer_Wordnet(tokens):
    lemmatizer = WordNetLemmatizer() 
    return [Token(lemmatizer.lemmatize(word.token,pos = word.pos),word.pos,forceToken=True) for word in tokens]



# This Class is a wrapper class for Lemmitazers
# It wraps each token and each relative tag
class Token:
    def __init__(self, token,pos='',forceToken=False):
        if(forceToken):
            self.token = token
        else:
            self.token = token[0]
        if(len(pos)):
            self.pos = pos
        else:
            if token[1].lower().startswith('v'): # Verb
                self.pos = 'v'
            elif token[1].lower().startswith('j') or token[1].lower().startswith('r') :# Adjective
                self.pos = 'a'
            else:
                self.pos = 'n'
            pass

    def __str__(self):
        return self.token + ": " + self.pos



class DocId:
    ID = 0
    @staticmethod
    def assign():
        DocId.ID += 1
        return DocId.ID

# this is a simple demo for this file's functions
if __name__ == '__main__':
    # Get the text from Reuters Corpus
    text = nltk.corpus.reuters.raw('training/10302')
    # Print the whole text
    print(text)
    # Tokenize the text (lower case and no stopwords)
    tokenized_text=[w for w in tokenize_text(to_lower(text)) if not is_stopword(w)]
    # Calculate each token's frequency
    freqencies = tokens_frequencies(tokenized_text)
    # Display each token frequency
    for word in freqencies.keys():
        print(word, freqencies[word])
    # Print most frequent token
    print(most_frequent_token(tokenized_text))
    # Print the text sentence by sentence
    for sent in get_sents(text):
        print("--"+sent)

