import nltk
# Download Reuters database
nltk.download('reuters')
# Download English Stop Words
nltk.download('stopwords')
# Download Sentence Tokenizer
nltk.download('punkt')
# Download wordnet lemmitizer
nltk.download('wordnet')
# Download word Tagger
nltk.download('averaged_perceptron_tagger')

# Displaying file names
print("\n\nDisplaying file names")
print(nltk.corpus.reuters.fileids())

# Displaying categories
print("\n\ndisplaying categories")
print(nltk.corpus.reuters.categories())

# Displaying 'jobs' files
print("\n\ndisplaying 'jobs' files")
print(nltk.corpus.reuters.fileids('jobs'))

# Displying certain file categories
print("\n\ndisplying certain file categories")
print(nltk.corpus.reuters.categories('test/14828'))