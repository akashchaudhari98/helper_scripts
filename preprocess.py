class preprocess:

  #def __init__(self,data):
  #  self.data = data
  
  def remove_stopwords(self,data):
    stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you",
                  "your", "yours", "yourself", "yourselves", "he", "him", "his", 
                  "himself", "she", "her", "hers", "herself", "it", "its", "itself",
                  "they", "them", "their", "theirs", "themselves", "what", "which", 
                  "who", "whom", "this", "that", "these", "those", "am", "is", "are",
                  "was", "were", "be", "been", "being", "have", "has", "had", "having",
                  "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if",
                  "or", "because", "as", "until", "while", "of", "at", "by", "for", 
                  "with", "about", "against", "between", "into", "through", "during",
                  "before", "after", "above", "below", "to", "from", "up", "down", "in",
                  "out", "on", "off", "over", "under", "again", "further", "then", "once",
                  "here", "there", "when", "where", "why", "how", "all", "any", "both", 
                  "each", "few", "more", "most", "other", "some", "such", "no", "nor",
                  "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", 
                  "can", "will", "just", "don", "should", "now"]
    sentence = []
    for words in data.split( ):
      if words in stop_words:
        pass
      else: sentence.append(words)

    sentence = " ".join(sentence)
    return sentence

  def stemming(self,data):
    import nltk
    nltk.download('punkt')
    from nltk.stem import PorterStemmer
    from nltk.tokenize import sent_tokenize, word_tokenize
    words = word_tokenize(data)
    ps = PorterStemmer()
    sentence = [ps.stem(w) for w in words]
    sentence = " ".join(sentence)
    return sentence
  
  def lemmatizing(self,data):
    import nltk
    nltk.download('wordnet')
    nltk.download('punkt')
    from nltk.stem import 	WordNetLemmatizer
    wordnet_lemmatizer = WordNetLemmatizer()
    tokenization = nltk.word_tokenize(data)
    sentence = [wordnet_lemmatizer.lemmatize(w) for w in tokenization]
    sentence = " ".join(sentence)
    return sentence

  def unigrams(self,data):
    sentence = [word for word in data.split(' ')]
    return sentence
  
  def bigrams(self,data):
    sentence = [i for i in zip(data.split(" ")[:-1], data.split(" ")[1:])] 
    return sentence

  def rem_non_alphaumeric(self,data):
    import re
    data = re.sub(r'\W+', ' ', data)
    return data
