
# coding: utf-8

# # text summarization 
# 

# In[1]:


#importing dataset

from nltk.corpus import state_union
text = state_union.raw("2006-GWBush.txt")


# In[2]:


#importing necessary nltk methods from nltk library 
from nltk.tokenize import sent_tokenize, word_tokenize 
from nltk.corpus import stopwords
import string

#creating list of stopwords
stop = stopwords.words('english')
punctuations = list(string.punctuation)
stops = stop + punctuations

#creating the list of sentences out of the text
sentence_list = sent_tokenize(text)


# In[3]:


#counting the frequency of non-stopwords in the whole text

word_frequencies = {}  

for word in word_tokenize(text):  
    if word not in stops:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1


# In[4]:


#calculating the weighted frequency of each word

max_frequency = max(word_frequencies.values())

for word in word_frequencies.keys():  
    word_frequencies[word] = (word_frequencies[word]/max_frequency)


# In[5]:


#calculating the score of each sentence based on word frequencies and storing it in a dictionary

sent_scores = {}  

for sentence in sentence_list:  
    
    # creating list of words from a single sentence 
    tokenized_words = word_tokenize(sentence.lower())
    
    #going through every word one by one
    for word in tokenized_words:
        
        if word in word_frequencies.keys():
            """ 
               we dont want to take very long sentences in the summary 
               therfore we are taking sentences with less than 25 words.
            """
            if len(tokenized_words) < 25:
                
                # this is for the first time we add the sentence to sent_scores
                if sentence not in sent_scores.keys():
                    sent_scores[sentence] = word_frequencies[word]
                    
                #for subsequent turns when sentence is already present, just update 
                else:
                    sent_scores[sentence] += word_frequencies[word]


# In[6]:


"""
To create the summary , now we can adopt two approaches 
1. we can take all those sentences with score greater than some value 
2. wee can take some top scoring sentences say 50 sentences
"""


# In[7]:


#Approach 1

final_list1 = []
for (sentence,score) in sent_scores.items() :
    if score >= 0.5:
        final_list1.append(sentence)

summary1 = " ".join(final_list1)
print("THE SUMMARY OF TEXT IS :")
print("\n")
print(summary1)


# In[8]:


#Approach 2

import heapq  
summary2 = heapq.nlargest(50, sent_scores, key = sent_scores.get)

summary2 = " ".join(summary2)
print("THE SUMMARY OF TEXT IS :")
print("\n")
print(summary2)

