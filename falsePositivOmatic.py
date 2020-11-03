# @Christian Aeberhard, SWM HS20, Exercise01
import csv
import matplotlib.pyplot as plt


# Input: c = True Positive in ranked list; r = number of retrieved links
# Output: Precision Value (float)
def calculatePrecision(c, r):
    try:
        return abs(c) / abs(r)
    except ZeroDivisionError:
        pass


# Input: c = True Positive in ranked list; t = total number of correct links
# Output: Recall Value (float)
def calculateRecall(c, t):
    return abs(c) / abs(t)


# Data Processing Arrays
oracleContainer = []
falsePositiveContainer = []
precisionRecallContainer = []
precisionContainer = []
recallContainer = []
tempContainer = precisionRecallContainer

# make sure to place these two files in the root directory
oracle2Data = open("./oracle2.txt", 'r')
listNData = open("./ranked_listN.txt", 'r')

# Correct = Nr, of correct Links; totalCorrect = Total nr, of correct links, retrieved = nr. of retrieved links
# counter = boundary helper variable
counter = -1
retrieved = 0
correct = 0
totalCorrect = 0

# Prepare and Slice Oracle Data and store it in an 2D Array
for line in oracle2Data:
    lineSplit = line.split(",")
    oracleContainer.append([lineSplit[0][0:-4], lineSplit[1][0:-5]])

# Prepare Ranked_Dataset
for line in listNData:
    if counter == -1:
        pass
    else:
        lineSplit = line.split(",")
        try:
            falsePositiveContainer.append([lineSplit[0][0:-4], lineSplit[1][0:-4], lineSplit[2][0:-1]])
        except IndexError:
            pass
    counter += 1

# Assign False Positive values and output the array as .csv to also validate it in excel
for i in falsePositiveContainer:
    i.append("0")
    for j in oracleContainer:
        if i[0] == j[0] and i[1] == j[1]:
            i[3] = "1"
newFile = csv.writer(open("FalsePositiveData.csv", "w"), delimiter=",", lineterminator='\n')
for x in falsePositiveContainer:
    newFile.writerow(x)

# Count the total nr. of correct links of the entire ranked list
for i in falsePositiveContainer:
    if i[3] == "1":
        totalCorrect += 1

# Iterate over the entire list, calculating precision and recall for 0 to the total number of entries of the list
for iteration in range(0, len(falsePositiveContainer)):
    correct = 0
    retrieved = iteration
    sentinel = 0
    if iteration == 0:
        if falsePositiveContainer[0][3] == "1":
            correct += 1

    for r in range(0, iteration):
        if falsePositiveContainer[r][3] == "1":
            correct += 1

    if iteration != 0:
        if (calculatePrecision(correct, retrieved) != precisionRecallContainer[sentinel - 1][0] and
                calculateRecall(correct, totalCorrect) != precisionRecallContainer[sentinel - 1][1] and
                str(calculateRecall(correct, totalCorrect))[::-1].find('.') == 1):
            precisionRecallContainer.append([calculatePrecision(correct, retrieved),
                                             calculateRecall(correct, totalCorrect)])
            sentinel += 1

    else:
        precisionRecallContainer.append(
            [calculatePrecision(correct, retrieved + 1), calculateRecall(correct, totalCorrect)])
        sentinel += 1


# populate the tempContainer with precision and recall values in order to plot the graph
for n in tempContainer:
    precisionContainer.append(n[0])
    recallContainer.append((n[1]))
    # print(n)

''''' Just for Testing
print("correct: " + str(correct))
print("total Correct: " + str(totalCorrect))
print("retrieved: " + str(retrieved))
print("precision: " + str(calculatePrecision(correct,retrieved)))
print("recall: " + str(calculateRecall(correct,totalCorrect)))
'''''


# Create and Design the Plot
plt.plot(recallContainer, precisionContainer, linestyle='-', marker='X', color="b",
         markerfacecolor="red", markersize=9)
plt.ylabel('precision')
plt.xlabel('recall')
plt.ylim(0, 1.1)
plt.xticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
plt.yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.title("Precision Recall Graph HS20")


# Display the Plot
plt.show()
