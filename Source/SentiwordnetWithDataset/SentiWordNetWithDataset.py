import os

import nltk
import numpy as np
from nltk.corpus import sentiwordnet as swn
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Creating counter variables for calculating positive and negative accuracy
pos_analyzed = 0
neg_analyzed = 0

pos_correct = 0
neg_correct = 0

# Creating a dictionary to convert NLTK tags to SentiWordNet compatible tags
nltk_to_sentiwordnet = {
    "NN": "n",
    "VB": "v",
    "JJ": "a",
    "RB": "r",
}

# Analyzing each file in the "pos" directory using SentiWordNet / Printing file name and Correct or Incorrect
for filename in sorted(os.listdir("pos")):
    f = os.path.join("pos", filename)
    file = open(f, "r", encoding="utf8")
    file_input = file.read()
    file.close()

    # Printing file information to show progress
    pos_analyzed = pos_analyzed + 1
    print("Analyzing positive file: ", filename, " ", pos_analyzed, end="        ")

    # Converting text into a list of separated tokens
    tokens = word_tokenize(file_input)

    # Converting the words into lowercase
    lower_tokens = []
    for word in tokens:
        lower_tokens.append(word.lower())

    # Removing stopwords from the list
    sw_tokens = [word for word in lower_tokens if word not in stopwords.words()]

    # Lemmatizing words in the list
    wnl = WordNetLemmatizer()
    lem_tokens = []
    for word in sw_tokens:
        lem_tokens.append(wnl.lemmatize(word))

    # Tagging tokens with relevant grammatical information
    tagged_tokens = nltk.pos_tag(lem_tokens)

    # Creating variables for storing scores for averaging
    pos_scores = []
    neg_scores = []
    subj_scores = []

    # Beginning testing by analyzing each token
    for word, pos in tagged_tokens:

        swn_pos = nltk_to_sentiwordnet.get(pos[:2], None)

        if swn_pos is None:
            continue

        synsets = list(swn.senti_synsets(word, pos=swn_pos))

        if len(synsets) == 0:
            continue

        for synset in synsets[:1]:
            pos_scores.append(synset.pos_score())
            neg_scores.append(synset.neg_score())
            subj_scores.append(1 - synset.obj_score())

    if np.sum(pos_scores) > np.sum(neg_scores):
        pos_correct = pos_correct + 1
        print("Correct         ")
    else:
        print("Incorrect       ")

# Analyzing each file in the "neg" directory using SentiWordNet / Printing file name and Correct or Incorrect
for filename in sorted(os.listdir("neg")):
    f = os.path.join("neg", filename)
    file = open(f, "r", encoding="utf8")
    file_input = file.read()
    file.close()

    # Printing file information to show progress
    neg_analyzed = neg_analyzed + 1
    print("Analyzing negative file: ", filename, " ", neg_analyzed, end="        ")

    # Converting text into a list of separated tokens
    tokens = word_tokenize(file_input)

    # Converting the words into lowercase
    lower_tokens = []
    for word in tokens:
        lower_tokens.append(word.lower())

    # Removing stopwords from the list
    sw_tokens = [word for word in lower_tokens if word not in stopwords.words()]

    # Lemmatizing words in the list
    wnl = WordNetLemmatizer()
    lem_tokens = []
    for word in sw_tokens:
        lem_tokens.append(wnl.lemmatize(word))

    # Tagging tokens with relevant grammatical information
    tagged_tokens = nltk.pos_tag(lem_tokens)

    # Creating variables for storing scores for averaging
    pos_scores = []
    neg_scores = []

    # Beginning testing by analyzing each token
    for word, pos in tagged_tokens:

        swn_pos = nltk_to_sentiwordnet.get(pos[:2], None)

        if swn_pos is None:
            continue

        synsets = list(swn.senti_synsets(word, pos=swn_pos))

        if len(synsets) == 0:
            continue

        for synset in synsets[:1]:
            pos_scores.append(synset.pos_score())
            neg_scores.append(synset.neg_score())

    if np.sum(pos_scores) < np.sum(neg_scores):
        neg_correct = neg_correct + 1
        print("Correct         ")
    else:
        print("Incorrect       ")

# Creating variables for calculating accuracy
total_correct = pos_correct + neg_correct
total_analyzed = pos_analyzed + neg_analyzed

# Printing positive, negative, and total accuracy
print("\n\n")
print("Testing Complete")
print("-------------------------------------------------")
print("Positive Correct: ", pos_correct, " / ", pos_analyzed, "  ", ((pos_correct / pos_analyzed) * 100), "%")
print("Negative Correct: ", neg_correct, " / ", neg_analyzed, "  ", ((neg_correct / neg_analyzed) * 100), "%")
print("Total Correct: ", total_correct, " / ", total_analyzed,  "  ", ((total_correct / total_analyzed) * 100), "%")
