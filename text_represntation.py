from gensim.models import Word2Vec
!pip install -U sentence-transformers
from sentence_transformers import SentenceTransformer
import gensim 
from gensim.models import Word2Vec
from nltk.tokenize import sent_tokenize, word_tokenize 

class Text_Represntation:

  def onehot(data):
    cv=CountVectorizer()
    data = cv.fit_transform(data)
    return data
  
  def TFIDF(data):
    tv=TfidfVectorizer(use_idf=True)
    data = tv.fit_transform(data)
  
  def wordembedding(data):
    embeddings = []
    embeddings_dictionary = dict()
    EMBEDDING_FILE = '/content/drive/My Drive/dataset/glove.6B.100d.txt'
    with  open(EMBEDDING_FILE, encoding="utf8") as glove_file:
      for line in glove_file:
          records = line.split()
          word = records[0]
          vector_dimensions = np.asarray(records[1:], dtype='float32')
          embeddings_dictionary[word] = vector_dimensions

    num_features = 10
    featureVec = np.zeros((num_features,), dtype="float32")
    nwords = 0
    for sentences in data:
      for word in sentences:
          nwords = nwords+1
          featureVec = np.add(featureVec, embeddings_dictionary[word])
      if nwords>0:
          featureVec = np.divide(featureVec, nwords)
      
      embeddings.append(featureVec)
    
    return embeddings
  
  def customembeddings(data):
     model = Word2Vec(data, min_count=1 ,size=10)#training the model
    def avg_sentence_vector(words, model, num_features):
      #function to average all words vectors in a given paragraph
      featureVec = np.zeros((num_features,), dtype="float32")
      nwords = 0
      for word in words:
          nwords = nwords+1
          featureVec = np.add(featureVec, model[word])
      if nwords>0:
          featureVec = np.divide(featureVec, nwords)
      return featureVec

    embeddings = []
    for sen in data:
      x = avg_sentence_vector(sen.split(), model=Word2Vec.load('college_bot/smalltalk_model.bin'), num_features=10)
      embeddings.append(x)
    
    return embeddings
  
  def bertembddings(data):
    model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')
    embeddings = []
    for sen in data:
      sentence_embeddings = model.encode(sen)
      embeddings.append(sentence_embeddings)

    return embeddings




