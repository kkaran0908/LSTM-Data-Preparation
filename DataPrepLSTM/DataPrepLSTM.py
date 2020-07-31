import warnings
warnings.filterwarnings("ignore")
import operator  #for dictionary
from keras.preprocessing import sequence #for padding
import numpy as np
class DataPrepLSTM:
    
    final_words = [] # contain the words in the decreasing order of their frequency in the dataset
    all_words = [] #it will store all the words in the dataset
    words = []  # this list will contain all the unique words in the dataset
    dictionary = {}    #dictionary to store the count of all words in the dataset
    new_data = []       #it will store the data after transformation
    feature_length = None
    
    
    def __init__(self, data):
        self.data = data.values.tolist()

    def fit(self):
        
        for k in self.data:
            for word in k[0].split(' '):
                if word not in self.words:
                    self.words.append(word)    #it will contain all the unique word in the dataset
                self.all_words.append(word)  #it will containing all the words in the dataset

                
        for k in self.all_words:
                self.dictionary[k] = 0 #initializing the dictionary with 0
        
        
        for k in self.all_words:
            self.dictionary[k] = self.dictionary[k]+1   # creating the dictionary from the dataset
        sorted_dict = sorted(self.dictionary.items(), key=operator.itemgetter(1))  # sorting the dictionary according to the number of times a word has occured
        sd = sorted_dict[::-1]   # containing all the words count in dec order
        #final_words = []
        for word in sd:
            self.final_words.append(word[0])
        
    def transform(self, data, feature_length=None):
        
                data = data.values.tolist()
                self.feature_length = feature_length
                self.new_data = []
            
                for f in data:
                    l = []
                    for k in f[0].split(' '):
                        if k in self.final_words:
                            #finding the index of the word
                            ind = self.final_words.index(k)
                            l.append(ind+1)
                    #updating the text sentence
                    self.new_data.append(l)
                    
                #if the length of the features not given, use length of unique words for padding     
                if self.feature_length ==None:
                    transformed_data = sequence.pad_sequences(self.new_data)
                #use given feature length to for padding 
                else:
                    transformed_data = sequence.pad_sequences(self.new_data,maxlen = self.feature_length)
                return transformed_data
            
            
    #this method will return count of all the unique words in the dataset
    def uniqueCounts(self):
        return len(self.words)
    
    
    #this method will return number of words in the dataset
    def wordCount(self):
        #print(self.all_words)
        return len(self.all_words)
    
    #this method will return the transformed data in its original form i.e. without padding the sequence
    def orgSequence(self):
        return (self.new_data)
    
    # this method returns the dictionary dict{word : frequency_of_word}
    def returnDict(self):
        return (self.dictionary)
    
    #this method returns the list with words in the decreasing order of their frequency in the dataset
    def returnVocab(self):
        return (self.final_words)
    
"""if __name__=="__main__":
    data = pd.read_csv('clean_text.csv')
    data = data['Text']
    obj = DataPrepLSTM(data)
    obj.fit()
    total_word = obj.wordCount()
    print("Total Words in the Data-Set:\t",total_word)
    print("**********************************************")
    uniquecount = obj.uniqueCounts()
    print("Total Number of Unique Words in the Data-Set:\t",uniquecount)
    print("**********************************************")
    wordcount = obj.wordCount()
    print("Total Number of Unique Words in the Data-Set:\t",wordcount)
    print("**********************************************")
    transformed_data = obj.transform(data,600)
    print("Dimensions of the transformed data:\t",transformed_data.shape)
    print("**********************************************")
    print("Transformed Data:\n")
    print(transformed_data.shape)"""
