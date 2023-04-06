import csv

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Importing the Opinion Lexicon's positive and negative word lists
file1 = open("opinion-lexicon-English/positive-words.txt", "r", encoding="utf8")
bing_pos = file1.read()
file1.close()

file2 = open("opinion-lexicon-English/negative-words.txt", "r", encoding="utf8")
bing_neg = file2.read()
file2.close()

# Creating counter variables for calculating positive and negative accuracy
pos_analyzed = 0
neg_analyzed = 0

pos_correct = 0
neg_correct = 0

# Analyzing each file in the "pos" directory using the Opinion Lexicon / Printing file name and Correct or Incorrect
with open("pos.csv", encoding="utf-8") as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    for row in csvReader:

        # Printing file information to show progress
        pos_analyzed = pos_analyzed + 1
        print("Analyzing positive row ", pos_analyzed, end="        ")

        # Converting text into a list of separated tokens
        tokens = word_tokenize(row[5])

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

        # Creating variables for storing sentiment scores
        score = 0

        # Beginning testing by analyzing each token
        for word in lem_tokens:
            if word in bing_pos:
                score = score + 1
            elif word in bing_neg:
                score = score - 1
        if score > 0:
            pos_correct = pos_correct + 1
            print("Correct", score)
        else:
            print("Incorrect", score)

# Analyzing each file in the "neg" directory using the Opinion Lexicon / Printing file name and Correct or Incorrect
with open("neg.csv", encoding="utf-8") as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    for row in csvReader:

        # Printing file information to show progress
        neg_analyzed = neg_analyzed + 1
        print("Analyzing negative row ", neg_analyzed, end="        ")

        # Converting text into a list of separated tokens
        tokens = word_tokenize(row[5])

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

        # Creating variable for storing sentiment scores
        score = 0

        # Beginning testing by analyzing each token
        for word in lem_tokens:
            if word in bing_pos:
                score = score + 1
            elif word in bing_neg:
                score = score - 1
        if score < 0:
            neg_correct = neg_correct + 1
            print("Correct", score)
        else:
            print("Incorrect", score)

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