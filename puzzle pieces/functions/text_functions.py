#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# In[1]:


import re
import string
import nltk

from nltk.corpus import stopwords


# In[2]:


mispell_dict = {"aren't" : "are not",
"can't" : "cannot",
"couldn't" : "could not",
"couldnt" : "could not",
"didn't" : "did not",
"doesn't" : "does not",
"doesnt" : "does not",
"don't" : "do not",
"hadn't" : "had not",
"hasn't" : "has not",
"haven't" : "have not",
"havent" : "have not",
"he'd" : "he would",
"he'll" : "he will",
"he's" : "he is",
"i'd" : "I would",
"i'd" : "I had",
"i'll" : "I will",
"i'm" : "I am",
"isn't" : "is not",
"it's" : "it is",
"it'll":"it will",
"i've" : "I have",
"let's" : "let us",
"mightn't" : "might not",
"mustn't" : "must not",
"shan't" : "shall not",
"she'd" : "she would",
"she'll" : "she will",
"she's" : "she is",
"shouldn't" : "should not",
"shouldnt" : "should not",
"that's" : "that is",
"thats" : "that is",
"there's" : "there is",
"theres" : "there is",
"they'd" : "they would",
"they'll" : "they will",
"they're" : "they are",
"theyre":  "they are",
"they've" : "they have",
"we'd" : "we would",
"we're" : "we are",
"weren't" : "were not",
"we've" : "we have",
"what'll" : "what will",
"what're" : "what are",
"what's" : "what is",
"what've" : "what have",
"where's" : "where is",
"who'd" : "who would",
"who'll" : "who will",
"who're" : "who are",
"who's" : "who is",
"who've" : "who have",
"won't" : "will not",
"wouldn't" : "would not",
"you'd" : "you would",
"you'll" : "you will",
"you're" : "you are",
"you've" : "you have",
"'re": " are",
"wasn't": "was not",
"we'll":" will",
"didn't": "did not",
"c'mon":"come on",
"'cause": "because"}


# In[3]:


def clean_text(text):
    
    # Step 1. Drop special characters and keep just the alpha
    text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", text) #remove all except A-Z, a-z, 0-9 
    text = re.sub('[^a-zA-Z]',' ',text)
    text = re.sub('\s+',' ',text)
    text = re.sub(r'\W*\b\w{1,3}\b',' ', text)
    
    #Step 2. Transform them into lower case
    text = text.lower().split()

    #Step 3. Delete stop words
    stops = set(stopwords.words("english"))
    stops2 = set(stopwords.words("spanish"))
    stops3 = set(stopwords.words("italian"))
    text = [w for w in text if not w in stops]
    text = [w for w in text if not w in stops2]
    text = [w for w in text if not w in stops3]
    text = " ".join(text)
    return(text)

def _get_mispell(mispell_dict):
    """
    Find the typical_misspelling mistakes
    """
    mispell_re = re.compile('(%s)' % '|'.join(mispell_dict.keys()))
    return mispell_dict, mispell_re

def replace_typical_misspell(text):
    """
    Find the typical_misspelling mistakes and replace them
    """
    mispellings, mispellings_re = _get_mispell(mispell_dict)

    def replace(match):
        return mispellings[match.group(0)]

    return mispellings_re.sub(replace, text)

def clean_data(title):
    print("Data cleaning started........")
    clean_title = clean_text(title)
    clean_title = replace_typical_misspell(clean_title)
    print("Data cleaning Done........")
    return clean_title

