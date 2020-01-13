from Utils import *

ponctuations = ['.',',','?',';',':','']
class PreprocessPipeline:
    def __init__(self):
        self.pipepline = []
        self.tokens = []
        self.tokenizer = tokenize_text
        self.stopwords = stop_words
        
    def addStep(self,step):
        self.pipepline.append(step)

    def preprocess(self, text):
        text = to_lower(text)
        tokens = [w for w in  self.tokenizer(text) if len(w)>1] # remove poctuations
        pos = get_tags(tokens)
        self.tokens = [Token(w) for w in pos if not is_stopword(w[0])]

    def process(self, text):
        self.preprocess(text)
        result = self.tokens
        
        for processingStep in self.pipepline:
            step = []
            step = processingStep(result)
            result = step
            
        return [w.token for w in result]

if __name__ == '__main__':
    # Get the text from Reuters Corpus
    text = nltk.corpus.reuters.raw('training/10302')
    preProcessor = PreprocessPipeline()
    
    preProcessor.addStep(lambda tokens:lemmatizer_Wordnet(tokens))
    preProcessor.addStep(lambda tokens:stemming_Porter(tokens))
    #preProcessor.addStep(lambda tokens:stemming_Snowball(tokens))
    print(preProcessor.process(text))