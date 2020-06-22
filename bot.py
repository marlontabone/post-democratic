from cleandoc import clean_doc #import cleandoc function from clean_doc.py
from numpy import loadtxt
from generate import generate_seq #import generate_seq function from generate
from twython import Twython #importing Twython library
from config import getApi #import getApi function from config.py
import tensorflow
import random as rand
import string
import nltk
from tensorflow.keras.models import load_model #to be able to load tensorflow pre-trained ML models
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical
from nltk.stem import WordNetLemmatizer
from nltk.tokenize.treebank import TreebankWordDetokenizer
import sched, time

def postStatus(update): #function to post a status update
    api = getApi()
    status = api.PostUpdate(update)

twObj = Twython( #api credentials object for the postStatusMedia function which uses Twython
    app_key = '5JD1Xl8zz0vFu9URaCh6oJ5Os',
    app_secret= 'JJ8txIr1mPAKdFRrFkwPUQvitaN2X9aiCddxWbPqDcvUuwwKT1',
    oauth_token= '1270840961954873344-JAa7Qn9TeFHUIRqiDB3SInlgKD5u4v',
    oauth_token_secret = 'YcdlCJ4Cg30qstQhSNvCjViMytDGmwh39lycwkhhvZHoq')

def postStatusMedia(update): #function to post a status update + media
    photo = open('img/'+str(rand.randrange(1,87))+'.jpg', 'rb')
    response = twObj.upload_media(media=photo)
    twObj.update_status(status=update, media_ids=[response['media_id']])

modNum = str(rand.randrange(0,3))

model = load_model('models/'+modNum+'.h5') #loading machine learning model
print("loaded model succesfully"+" "+modNum)

# loading .txt file and some text processing/formatting
path = ('datasets/'+modNum+'.txt') #loading the dataset used to train the loaded model (to generate seed sentences)
text = open(path).read().lower() # reading text and making everything lower case
#cleaning text data set from puctuation
token=clean_doc(text)

#lemmatization
wd = WordNetLemmatizer()
newDict = []

#lemmatize loaded text (which has been tokenized) to make for a smaller vocabulary eliminating words of similar meaning.
for w in token:
    newDict.append(wd.lemmatize(w))
    #creating vocabulary

    sequence_len=30
    seq=[]

for i in range(0,len(newDict)-sequence_len):
    seq.append(newDict[i:i+sequence_len])

tokenizer = Tokenizer()
tokenizer.fit_on_texts(seq)
sequence = tokenizer.texts_to_sequences(seq)
vocab_size = len(tokenizer.word_index)

arr=np.array(sequence)

# Length of extracted word sequences
maxlen = 10

# We sample a new sequence every `step` words
step = 1

# This holds our extracted sequences
sentences = []

#putting together sequences and seed sentences
for i in range(0, len(newDict) - maxlen, step):
    sentences.append(newDict[i: i + maxlen])

X, Y = arr[:,:-1], arr[:,-1]

Y=to_categorical(Y,num_classes=vocab_size+1)

seq_length = X.shape[1]

s = sched.scheduler(time.time, time.sleep)

def post():
    size = rand.randrange(20,35) #size of the generated words/texts

    tokenised_text = sentences[rand.randrange(len(sentences))] #picking a random seed from the seed sentences
    seed_text = TreebankWordDetokenizer().detokenize(tokenised_text)
    generated = generate_seq(model, tokenizer, seq_length, seed_text, size) #calling the generate_seq function to generate text

    output = seed_text + " " + generated +"..." #output consists of the seed along with the generated text
    tweet = output.capitalize() #first letter is capitalized.
    print(tweet) #tweet printed to console.

    time = 60*rand.randrange(0,10) #randomized output between 0 to 10 minutes intervals

    print(time)

    if (time/60)<2: # if time is under 2 minutes then status tweet is posted with a randomly picked image from the img folder
        #postStatus(tweet)
        postStatusMedia(tweet)
    else:
        postStatus(tweet) #if time is greater or equal to two minutes then only status will be posted.
    s.enter(time, 1, post)

time = 60*rand.randrange(0,10)
print(time)
s.enter(time, 1, post)
s.run()
