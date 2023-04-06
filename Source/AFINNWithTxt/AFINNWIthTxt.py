from afinn import Afinn
import os

# Creating counter variables for calculating positive and negative accuracy
pos_analyzed = 0
neg_analyzed = 0

pos_correct = 0
neg_correct = 0

# Analyzing each file in the "pos" directory using AFINN / Printing file name, Correct or Incorrect, and score
for filename in sorted(os.listdir("pos")):
    f = os.path.join("pos", filename)
    file = open(f, "r", encoding="utf8")
    file_input = file.read()
    file.close()
    pos_analyzed = pos_analyzed + 1
    print("Analyzing positive file: ", filename, "  ", pos_analyzed, end="        ")
    afinn = Afinn()
    score = afinn.score(file_input)
    if score > 0:
        pos_correct = pos_correct + 1
        print("Correct         ", score)
    else:
        print("Incorrect       ", score)

# Analyzing each file in the "neg" directory using AFINN / Printing file name, Correct or Incorrect, and score
for filename in sorted(os.listdir("neg")):
    f = os.path.join("neg", filename)
    file = open(f, "r", encoding="utf8")
    file_input = file.read()
    file.close()
    neg_analyzed = neg_analyzed + 1
    print("Analyzing negative file: ", filename, "  ", neg_analyzed, end="        ")
    afinn = Afinn()
    score = afinn.score(file_input)
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
print("Total Correct: ", total_correct, " / ", total_analyzed,  "  ", ((total_correct / total_analyzed) * 100), "%")
