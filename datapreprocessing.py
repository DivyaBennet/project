#import regex
import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 
import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
#start process_tweet

def processTweet(tweet):
    # process the tweets
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    #tokenization
    tweet = word_tokenize(tweet)
    tweet = nltk.pos_tag(tweet)
    return tweet
#end
#Read the tweets one by one and process it
fp = open('hate.txt', 'r')
line = fp.readline()

newline =[]
lemmatizer = WordNetLemmatizer() 
while line:
    processedTweet = processTweet(line)
    L = processedTweet
    for l in range (0,len(L)):
	T = L[l]
	#print(lemmatizer.lemmatize(T[0]))
	newline.append(lemmatizer.lemmatize(T[0]))
    tweet = nltk.pos_tag(newline)
    line = fp.readline()
fp1 = open('outputhate.txt','w')
for i in tweet:
        #print ':'.join(i) 
        fp1.write(':'.join(i)+'\n')
#end loop

print 'Success!!!'
fp.close()
fp1.close()
#Read the tweets one by one and process it
fp2 = open('clean.txt', 'r')
line = fp2.readline()

newline =[]
lemmatizer = WordNetLemmatizer() 
while line:
    processedTweet = processTweet(line)
    L = processedTweet
    for l in range (0,len(L)):
	T = L[l]
	#print(lemmatizer.lemmatize(T[0]))
	newline.append(lemmatizer.lemmatize(T[0]))
    tweet = nltk.pos_tag(newline)
    line = fp2.readline()
fp3 = open('outputclean.txt','w')
for i in tweet:
        #print ':'.join(i) 
        fp3.write(':'.join(i)+'\n')
#end loop

print 'Success!!!'
fp2.close()
fp3.close()
