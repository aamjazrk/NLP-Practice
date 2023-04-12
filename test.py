from nltk.probability import FreqDist
from nltk.corpus import stopwords
import re
import nltk
from nltk.corpus import webtext
from nltk.tokenize import sent_tokenize,word_tokenize

nltk.download('punkt')
with open('/Users/hunteraek/Desktop/NLP/WillSmith.txt','r') as file:
    data = file.read()
print(data)

# make its be sentence format
sentences = sent_tokenize(data)

# tokenize sentence to be word and word should be lower case
words = []
for word in sentences:
    words.extend(word_tokenize(word.lower()))

# remove stopwords and get only word that have more than 2 character
nltk.download("stopwords")
sw = nltk.corpus.stopwords.words('english')
words_clear = [word for word in words if word not in sw ]
words_clear = [word for word in words_clear if len(word) > 2]

word_freq = FreqDist(words_clear)
words_list_to_be_dict = dict([(m, n) for m, n in word_freq.items()])
# sorted by value(freq from max to min used)
sorted_word = sorted(words_list_to_be_dict.items(), key=lambda x:x[1], reverse=True)
print("number of sentences : ", len(words_clear))
for key,freq in sorted_word:
    print("%s: %s" % (key, freq))
