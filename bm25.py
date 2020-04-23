import numpy as np
import math
from multiprocessing import Pool, cpu_count
from bm25_bi import BM25_bi
 
#print("5")
class BM25():
  def __init__(self, corpus,tokenizer=None, k1=1.2, b=0, epsilon=0.25):
    self.k1 = k1
    self.b = b
    self.epsilon = epsilon
    self.corpus_size = len(corpus)
    self.avgdl = 0
    self.doc_freqs = []
    self.idf = {}
    self.doc_len = []
    self.tokenizer = tokenizer
    
    if tokenizer:
      corpus = self._tokenize_corpus(corpus)
    nd = self._initialize(corpus)
    self._calc_idf(nd)

  def _initialize(self, corpus):
    nd = {}  # word -> number of documents with word
    num_doc = 0
    for document in corpus:
      self.doc_len.append(len(document))
      num_doc += len(document)
      frequencies = {}
      for word in document:
          if word not in frequencies:
            frequencies[word] = 0
          frequencies[word] += 1
      self.doc_freqs.append(frequencies)

      for word, freq in frequencies.items():
          if word not in nd:
              nd[word] = 0
          nd[word] += 1
    self.avgdl = num_doc / self.corpus_size
    return nd

  def _tokenize_corpus(self, corpus):
    #print(corpus)
    tokenized_corpus = pool.map(self.tokenizer, corpus)
    return tokenized_corpus                      

  def _calc_idf(self, nd):

    """
    Calculates frequencies of terms in documents and in corpus.
    This algorithm sets a floor on the idf values to eps * average_idf
    """
    # collect idf sum to calculate an average idf for epsilon value
    idf_sum = 0
    # collect words with negative idf to set them a special epsilon value.
    # idf can be negative if word is contained in more than half of documents
    negative_idfs = []
    for word, freq in nd.items():
      idf = math.log(self.corpus_size - freq + 0.5) - math.log(freq + 0.5)
      self.idf[word] = idf
      idf_sum += idf
      if idf < 0:
        negative_idfs.append(word)
    self.average_idf = idf_sum / len(self.idf)
    eps = self.epsilon * self.average_idf
    for word in negative_idfs:
      self.idf[word] = eps

  def get_scores(self, query):
    #print(self. corpus_size)
    score = np.zeros(self.corpus_size)
    doc_len = np.array(self.doc_len)
    #print(query)
    for q in query:
      if q == "":
        continue
      #print("query  " ,q) 
      q_freq = np.array([ (doc.get(q) or 0) for doc in self.doc_freqs])
     #print("q_freq ",q_freq)
      score += (self.idf.get(q) or 0) * ((q_freq * (self.k1 + 1))/(q_freq + self.k1 * (1 - self.b + self.b * doc_len / self.avgdl)))
    print("score ",score)

    return score

    
  def get_top_n(self, query, documents, n):
    assert self.corpus_size == len(documents), "The documents given don't match the index corpus!"
    scores = self.get_scores(query)
    top_n = np.argsort(scores)[::-1][:n]
    return [documents[i] for i in top_n]

