from tensorflow.keras.preprocessing.sequence import pad_sequences

def generate_seq(model,tokenizer,seq_length,seed_text,n_words):

     result = []
     in_text =seed_text
     for i in range(n_words):
          encoded = tokenizer.texts_to_sequences([in_text])[0]
          encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
          yhat = model.predict_classes(encoded)
          out_word = ''
          for word,index in tokenizer.word_index.items():
               if index==yhat:
                  out_word = word
                  break
          in_text+=' ' + out_word
          result.append(word)
     return ' '.join(result)
