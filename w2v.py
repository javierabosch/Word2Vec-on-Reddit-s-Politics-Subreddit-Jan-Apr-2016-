import pandas as pd
import gensim as gen
import numpy as np
import string
import itertools
import logging
from nltk.tokenize import sent_tokenize, word_tokenize

# Read files
jan = pd.read_csv('C:/Blog/Datasets/Reddit/politics_jan16')
feb = pd.read_csv('C:/Blog/Datasets/Reddit/politics_feb16')
mar = pd.read_csv('C:/Blog/Datasets/Reddit/politics_mar16')
apr = pd.read_csv('C:/Blog/Datasets/Reddit/politics_apr16')

# Combine
four_months = jan.append([feb, mar, apr])
del jan, feb, mar, apr

# Reset indices
four_months.index = np.arange(four_months.shape[0])

# Coerce to unicode
four_months['body'] = four_months['body'].astype('str')

# Tokenize each comment to a list of its constituent sentences
four_months['sentences'] = four_months['body'].map(lambda c: sent_tokenize(c))

# Tokenize each constituent sentences into a list of its constituent words
# Also remove punctuation and convert to lowercase
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
four_months['words'] = four_months['sentences'].map(
    lambda ls: [word_tokenize(s.lower().translate(remove_punctuation_map)) for s in ls])

# Create list of comments, each a list of sentences
comments = list(four_months['words'])

# Remove outermost list structure from comments
sentences_list = list(itertools.chain.from_iterable(comments))

# Create bigrams for commonly occurring words
bigram = gen.models.phrases.Phrases(sentences_list)

# Activate logging for verbose training
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', \
                    level=logging.INFO)

# Initialize and train the model (this will take some time)
model = gen.models.word2vec.Word2Vec(sentences=bigram[sentences_list], size=300, workers=8, window=10, min_count=40,
                                     sg=1)

# Save
model.save('C:/Blog/word2vec/w2v_model')

# Load saved model
model = gen.models.word2vec.Word2Vec.load('C:/Blog/word2vec/w2v_model')

# Explore
model.most_similar(['bernie'])
model.doesnt_match("kelly anderson maddow".split())


