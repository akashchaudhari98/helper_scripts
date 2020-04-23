import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer 
import nltk
import os
import string
import numpy as np
import copy
import re
import math
import re

def convert_lower_case(data):
  data = data.lower()
  return data

def remove_stop_words(data):
  stop_words = stopwords.words('english')
  words = word_tokenize(str(data))
  new_text = ""
  for w in words:
      if w not in stop_words and len(w) > 1:
        new_text = new_text + " " + w
  return new_text

def remove_punctuation(data):
  data = re.sub(r'\W+', '', data)

  #symbols = "!\"#$%&()*+-/.:;<=>?@[\]^_`{|}~\n"
  #for i in range(len(symbols)):
  #    data = data.replace(data, symbols[i], ' ')
  #    data = np.char.replace(data, "  ", " ")
  #data = np.char.replace(data, ',', '')
  return data

def remove_apostrophe(data):
  return np.char.replace(data, "'", "")

def stemming(data):
  stemmer= PorterStemmer()
  tokens = word_tokenize(str(data))
  new_text = ""
  for w in tokens:
    new_text = new_text + " " + stemmer.stem(w)
  return new_text

def lemetisation(data):
  lmtzr = WordNetLemmatizer()
  word_list = nltk.word_tokenize(data)
  lemmatized_output = ' '.join([lmtzr.lemmatize(w) for w in word_list])

  return lemmatized_output

def convert_numbers(data):
  tokens = word_tokenize(str(data))
  new_text = ""
  for w in tokens:
    try:
        w = num2words(int(w))
    except:
        a = 0
    new_text = new_text + " " + w
  new_text = np.char.replace(new_text, "-", " ")
  return new_text

def remove_extra_spaces(data):
   data = data.replace("  ", "")
   return data

def word_count(str):
  length = len(str)
  counts = dict()
  words = str.split()
  no = 0
  for word in words:
    no = no+1
    if word in counts:
        counts[word] += 1/length
    else:
        counts[word] = 1/length
  return counts

def preprocess(data):
  data = convert_lower_case(data)
  data = remove_extra_spaces(data)
  data = remove_stop_words(data)
  data = remove_punctuation(data)
  #data = lemetisation(data)
  return data
'''
def final():
  book_data = []
  book_name = os.listdir("D:/projects/ZInc/New folder/book_txt")
  for books in book_name:
    with open("D:/projects/ZInc/New folder/book_txt/" + books , "r",encoding='utf=8' ) as f :
      data = f.readlines() 
      data = " ".join(data)
      data = preprocess(data)
      book_data.append(data)
  print(type(book_data))
  return book_data
final()
'''