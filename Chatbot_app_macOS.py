#########Library Improts
import pandas as pd
import os
import sys
import random
random.seed()

import spacy
nlp = spacy.load("en_core_web_sm")

import gensim
from gensim.models import Word2Vec
import Cython

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

#########Model Initiallizer
#Import CSV + Clean input

print("Hello, this is SmallTalkBot, I am booting up, please be patient.")

print("....reading....")
cluster_raw = pd.read_csv(os.path.dirname(__file__) + '//cluster_model.csv', sep=',')

#Lemmas
data_cleaned = cluster_raw
data_cleaned = data_cleaned.text.apply(lambda text: " ".join(token.lemma_ for token in nlp(text)))


#Transform into data useable by Word2Vec
data_model = data_cleaned.apply(lambda line: line.split())

data_model =  data_model.to_numpy().tolist()


#Train Model
# min_count = minimum # of instances of a word to create a vector, vector_size = degrees of freedom 

# workers = Core parallelization, speeds up training, sg = Training algorythm (here 1 is skip-gram)
print("....learning speech....")
model_base = Word2Vec(data_model, min_count=10, vector_size=325, workers=4, sg=1 )


# Create Feature Matrix
docs_vectors = pd.DataFrame()

for line in cluster_raw['text']:
    
    temp = pd.DataFrame() 
    
    for word in line.split(' '):  
    
        try:
            word_vec = model_base.wv[word] 
            temp = temp.append(pd.Series(word_vec), ignore_index = True) 
        except:
            pass
          
    doc_vector = temp.mean() 
    docs_vectors = docs_vectors.append(doc_vector, ignore_index = True) 

    


docs_vectors['cluster'] = cluster_raw['cluster']
docs_vectors = docs_vectors.dropna()


# Split train / test data
train_x, test_x, train_y, test_y = train_test_split(docs_vectors.drop('cluster', axis = 1),
                                                   docs_vectors['cluster'],
                                                   test_size = 0.2,
                                                   random_state = 1)



#Create KNN Model
neigh = KNeighborsClassifier(n_neighbors=5)
neigh.fit(train_x, train_y)


#### Chatbot Protocol

#import responses
print("....formulating answers....")
response_df = pd.read_csv(os.path.dirname(__file__) + '//Answers.csv', sep=';')

def GetCluster(user_input):

    #convert to predictable
    temp = pd.DataFrame() 
    
    for word in user_input.split(' '):  
        try:
            word_vec = model_base.wv[word] 
            temp = temp.append(pd.Series(word_vec), ignore_index = True) 
        except:
            pass
          
    input_value = temp.mean() 

    #predict cluster
    cluster = neigh.predict([input_value])[0]

    return cluster


def GetResponse(user_input):

    try:
        cluster = GetCluster(user_input)
    except:
        #No feature present, usually answer to short
        return("I'm not sure I understand, could you elaborate?")

    # retrieve responses for cluster
    selection = response_df[response_df.Cluster == cluster].reset_index()
    
    #random response from selection
    rand_number = random.randrange(0,len(selection))

    response = selection.loc[0, ['Answer']]

    return response

def ChatRoutine():
    print("Hello, my name is SmallTalkBot, nice to meet you.")

    while True:

        user_input = str(input("Say Something: "))
        
        print(GetResponse(user_input))
        #Programmer Note: I didn't write the responses, please don't blame me for them.

print("I'm ready. Thank you for waiting.")
ChatRoutine()

