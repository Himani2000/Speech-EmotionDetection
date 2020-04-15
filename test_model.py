from keras.models import Sequential, Model, model_from_json
import matplotlib.pyplot as plt
import keras 
import pickle
import wave  # !pip install wave
import os
import pandas as pd
import numpy as np
import sys
import warnings
import librosa
import librosa.display
import IPython.display as ipd 
#import pyaudio
if not sys.warnoptions:
    warnings.simplefilter("ignore")


def load_model(filename1,filename2):
    json_file = open(filename1, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    # load weights into new model
    loaded_model.load_weights(filename2)
    print("Loaded model..........")

    # the optimiser
    opt = keras.optimizers.rmsprop(lr=0.00001, decay=1e-6)
    loaded_model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
    return loaded_model

def load_file(filename):
    X, sample_rate = librosa.load(filename,res_type='kaiser_fast',duration=2.5,sr=44100,offset=0.5)

    sample_rate = np.array(sample_rate)
    mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=13),axis=0)
    newdf = pd.DataFrame(data=mfccs).T
    return newdf

def get_value(filename='DC_a01.wav'):

    dict1={0:'female_angry',1:'female_disguts',2:'female_fear',3:'female_happy',4:'female_neutral',5:'female_sad',6:'female_suprise',
            7:'male_angry',8:'male_disgust',9:'male_fear',10:'male_happy',11:'male_neutral',12:'male_sad',13:'male_suprise'}
    
    dict2={0:'female',1:'male'}
 
    dict3={0:'angry',1:'disgust',2:'fear',3:'happy',4:'neutral',5:'sad',6:'suprise'}
    
    filename1="SpeechEmotion_Model_json.json"
    filename2="SpeechEmotion_Model.h5"
    
    loaded_model=load_model(filename1,filename2)
    newdf=load_file(filename)
    newdf= np.expand_dims(newdf, axis=2)
    newpred = loaded_model.predict(newdf, batch_size=16,verbose=1)
    final = newpred.argmax(axis=1)
    final_1=dict1[final[0]]

    filename3="SpeechEmotionGender_Model_json.json"
    filename4="SpeechEmotionGender_Model.h5"
    loaded_model=load_model(filename3,filename4)
    newdf=load_file(filename)
    newdf= np.expand_dims(newdf, axis=2)
    newpred = loaded_model.predict(newdf, batch_size=16,verbose=1)
    final = newpred.argmax(axis=1)
    final_2=dict2[final[0]]



    filename5="SpeechEmotionSingle_Model_json.json"
    filename6="SpeechEmotionSingle_Model.h5"
    loaded_model=load_model(filename5,filename6)
    newdf=load_file(filename)
    newdf= np.expand_dims(newdf, axis=2)
    newpred = loaded_model.predict(newdf, batch_size=16,verbose=1)
    final = newpred.argmax(axis=1)
    final_3=dict3[final[0]]






    return final_1,final_2,final_3

