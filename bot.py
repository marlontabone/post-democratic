from config import getApi
from generate import generate_seq
from cleandoc import clean_doc
from numpy import loadtxt
import tensorflow
import random as rand
import sys
import os
import h5py
import nltk
import collections
from nltk.corpus import stopwords
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical
from nltk.tokenize import word_tokenize
nltk.download('wordnet')
nltk.download('punkt')
from nltk.stem import 	WordNetLemmatizer

# load model
model = load_model('modelTEST.h5')
# summarize model.
#print(model.summary())
print("loaded model succesfully")


# loading .txt file
path = 'nopunc2.txt'
text = open(path).read().lower() # reading text
#print('Corpus length:', len(text)) #printing length of text
#print(text)

#cleaning text data set from puctuation
token=clean_doc(text)


#lemmatization
wd = WordNetLemmatizer()
newDict = []

for w in token:
    newDict.append(wd.lemmatize(w))

#creating vocabulary

sequence_len=30
seq=[]

for i in range(0,len(token)-sequence_len):
    seq.append(token[i:i+sequence_len])

tokenizer = Tokenizer()
tokenizer.fit_on_texts(seq)
sequence = tokenizer.texts_to_sequences(seq)
print(sequence[2])

vocab_size = len(tokenizer.word_index)
print(vocab_size)

import numpy as np
arr=np.array(sequence)

# Length of extracted word sequences
maxlen = 30

# We sample a new sequence every `step` words
step = 1

# This holds our extracted sequences
sentences = []

for i in range(0, len(token) - maxlen, step):
    sentences.append(token[i: i + maxlen])

#choosing seeding sentence

tokenised_text = sentences[rand.randrange(len(sentences))]

from nltk.tokenize.treebank import TreebankWordDetokenizer
seed_text = TreebankWordDetokenizer().detokenize(tokenised_text)

#print(seed_text)

X, Y = arr[:,:-1], arr[:,-1]

Y=to_categorical(Y,num_classes=vocab_size+1)

seq_length = X.shape[1]

generated = generate_seq(model, tokenizer, seq_length, seed_text, rand.randrange(5,35))

api = getApi()

def postStatus(update):

    status = api.PostUpdate(update)
generated = generated+"."
postStatus(generated)
print(generated)
