from nltk.tokenize import word_tokenize
import re
from nltk.corpus import gutenberg,nps_chat
import nltk
nltk.download('gutenberg')
moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
# Search Every word contains substring ‘pen’ or ‘men’
data = []
for w in moby:
    if(re.search("^\w*(pen|men)\w*$",w)):
        data.append(w)
mylist = list(dict.fromkeys(data)) # remove duplication words
print(sorted(mylist))

# Search Every word ends with ‘ess’
data = []
for w in moby:
    if(re.search("^\w*ess$",w)):
        data.append(w)
mylist = list(dict.fromkeys(data)) # remove duplication words
print(sorted(mylist))

# Every word with 4 length 
data = []
for w in moby:
    if(re.search("^\w{4}$",w)):
        data.append(w)
mylist = list(dict.fromkeys(data)) # remove duplication words
print(sorted(mylist))



# Every word presents only 2-digit numbers
data = []
for w in moby:
    if(re.search("^\D*\d\d\D*$",w)):
        data.append(w)
mylist = list(dict.fromkeys(data)) # remove duplication words
print(sorted(mylist))

# Every word contains substrings started by ‘un’ or ‘pre’ 
data = []
for w in moby:
    if(re.search("^(un|pre)\w*$",w)):
        data.append(w)
mylist = list(dict.fromkeys(data)) # remove duplication words
print(sorted(mylist))




