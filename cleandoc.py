from nltk.tokenize import word_tokenize
import string

def clean_doc(text):

     clean_words= []

     words = word_tokenize(text)
     for word in words:
           word = word.strip(string.punctuation)
           if len(word)>=1 and word.isdigit()==False:
                      word = word.lower()
                      clean_words.append(word)
     return clean_words
