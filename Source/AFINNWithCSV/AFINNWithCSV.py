import csv
from afinn import Afinn
import string

# Creating counter variables for calculating positive and negative accuracy
pos_analyzed = 0
neg_analyzed = 0

pos_correct = 0
neg_correct = 0

# Analyzing each file in the "pos" directory using AFINN / Printing file name, Correct or Incorrect, and score
with open("pos.csv", encoding="utf-8") as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    for row in csvReader:
        pos_analyzed = pos_analyzed + 1
        print("Analyzing positive row ", pos_analyzed, end="        ")
        afinn = Afinn()
        score = afinn.score(row[5])
        if score > 0:
            pos_correct = pos_correct + 1
            print("Correct         ", score)
        else:
            print("Incorrect       ", score)

# Analyzing each file in the "neg" directory using AFINN / Printing file name, Correct or Incorrect, and score
with open("neg.csv", encoding="utf-8") as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    for row in csvReader:
        neg_analyzed = neg_analyzed + 1
        print("Analyzing negative row ", neg_analyzed, end="        ")
        afinn = Afinn()
        score = afinn.score(row[5])
        if score < 0:
            neg_correct = neg_correct + 1
            print("Correct         ", score)
        else:
            print("Incorrect       ", score)

# Creating variables for calculating accuracy
total_correct = pos_correct + neg_correct
total_analyzed = pos_analyzed + neg_analyzed

# Printing positive, negative, and total accuracy
print("\n\n")
print("Testing Complete")
print("-------------------------------------------------")
print("Positive Correct: ", pos_correct, " / ", pos_analyzed, "  ", ((pos_correct / pos_analyzed) * 100), "%")
print("Negative Correct: ", neg_correct, " / ", neg_analyzed, "  ", ((neg_correct / neg_analyzed) * 100), "%")
print("Total Correct: ", total_correct, " / ", total_analyzed, "  ", ((total_correct / total_analyzed) * 100), "%")
