## LSTM Data Preparation:
- DataPrepLSTM is a package, that will prepare the text dataset into the IMDB format. It is the format in which we have to feed the text data to an LSTM model. 

![alt text](https://raw.githubusercontent.com/kkaran0908/LSTM-Data-Preparation/master/imdb.PNG)

### in what format we need to feed data to this package:
- You have to convert entire text data into a single column, and this single column should be pandas core data frame, not a series data frame.
Any row of the dataset should not contain any numerical or NAN value. If it is the case, first convert them into a string, or you may want to remove the nan.


### How you can use this package:

1. Clone the repository using : 'git clone https://github.com/kkaran0908/LSTM-Data-Preparation.git'
2. Write the code in the same repo which contain DataPrepLSTM
3. I have provided the sample ipynb file and dataset, you can use that file to understand the working of the package.

### You can use below methods:

To import the package,
```python
from DataPrepLSTM.DataPrepLSTM import DataPrepLSTM
```

Create the object of the package class and fit the model
```python
obj = DataPrepLSTM(X_train)
obj.fit()
```

- Convert the text into the IMDB format:
```python
X_train_lstm = obj.transform(X_train)
X_test_lstm = obj.transform(X_test)
```

- This function will count the number of words in the dataset

```python
total_word = obj.wordCount()
print("Total Words in the Data-Set:\t",total_word)
```

- This function will count the total number of unique words in the dataset: 

```python
uniquecount = obj.uniqueCounts()
print("Total Number of Unique Words in the Data-Set:\t",uniquecount)
```
- This function will return us the dataset in it's original form means without applying padding to the dataset 

```python
originalSequence = obj.orgSequence()
```

- This function will return the dictionary of the unique words in the dataset where key: Word, and Value : Number of Occurances of That Word in the Entire Dataset

```python
dictionary = returnDict()
```
- This method returns the list with words in the decreasing order of their frequency in the dataset

```python
vocab = returnVocab()
```

### Before using this dataset be careful about the following things:
1. Convert X_train and X_test both into pandas core data frame, not in series dataframe
2. There must not be any numerical or NAN value either in X_train or X_test.
3. Please make sure all the libraies specified in requirement.txt are installed in your system

- Hope it will work for you. If you want to contribute, just make a pull request.

