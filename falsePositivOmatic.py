#@Christian Aeberhard
import csv
import matplotlib.pyplot as plt
import itertools



def calculatePrecision(c, r):
    try:
        return abs(c) / abs(r)
    except ZeroDivisionError:
        pass

def calculateRecall(c,t):
    return abs(c) / abs(t)


oracleContainer = []
falsePositiveContainer = []
precisionRecallContainer = []

#make sure to place these two files in the root directory
oracle2Data = open("./oracle2.txt", 'r')
listNData = open("./ranked_listN.txt", 'r')

counter = -1
retrieved = 0
correct = 0
totalCorrect = 0


#Prepare and Slice Oracle Data and store it in an 2D Array
for line in oracle2Data:
    lineSplit = line.split(",")
    oracleContainer.append([lineSplit[0][0:-4],lineSplit[1][0:-5]])

#Prepare Ranked_Dataset
for line in listNData:
    if counter == -1:
        pass
    else:
        lineSplit = line.split(",")
        try:
            falsePositiveContainer.append([lineSplit[0][0:-4],lineSplit[1][0:-4],lineSplit[2][0:-1]])
        except IndexError:
            pass
    counter += 1


#Assign False Positive values
for i in falsePositiveContainer:
    i.append("0")
    for j in oracleContainer:
        if i[0] == j[0] and i[1] == j[1]:
            i[3] = "1"
newFile = csv.writer(open ("FalsePositiveData.csv","w"), delimiter =",", lineterminator = '\n')
for x in falsePositiveContainer:
    newFile.writerow(x)


for i in falsePositiveContainer:
    #retrieved += 1
    if i[3] == "1":
        totalCorrect += 1
    #print(i)
#Adjust to change precision and recall

for iteration in range(0, 1410):
    correct = 0
    retrieved = iteration
    sentinel = 0
    if(iteration==0):
        if falsePositiveContainer[0][3] == "1":
            correct += 1

    for r in range(0, iteration):
        if falsePositiveContainer[r][3] == "1":
            correct += 1

    if(iteration != 0):
        if(calculatePrecision(correct, retrieved) != precisionRecallContainer[sentinel-1][0] and
        calculateRecall(correct, totalCorrect) != precisionRecallContainer[sentinel-1][1] and
        str(calculateRecall(correct, totalCorrect))[::-1].find('.') == 1):
            precisionRecallContainer.append([calculatePrecision(correct, retrieved),
                                             calculateRecall(correct, totalCorrect)])
            sentinel += 1

    else:
        print("correct: " + str(correct) + " " + "retrieved: " + str(retrieved))
        precisionRecallContainer.append(
            [calculatePrecision(correct, retrieved + 1), calculateRecall(correct, totalCorrect)])
        sentinel += 1
    #print("precision: " + str(calculatePrecision(correct, retrieved)))
    #print("recall: " + str(calculateRecall(correct, totalCorrect)))


def extract_key(v):
    return v[0]


#Precision, Recall
precisionContainer = []
recallContainer = []
tempContainer = precisionRecallContainer

for n in tempContainer:
    precisionContainer.append(n[0])
    recallContainer.append((n[1]))
    print(n)

print("correct: " + str(correct))
print("totalcorrect: " + str(totalCorrect))
print("retrieved: " + str(retrieved))

#print("precision: " + str(calculatePrecision(correct,retrieved)))
#print("recall: " + str(calculateRecall(correct,totalCorrect)))


plt.plot(recallContainer,precisionContainer, linestyle='-', marker='X', color="b",
         markerfacecolor="red", markersize=9)
plt.ylabel('precision')
plt.xlabel('recall')
plt.ylim(0, 1.1)
plt.xticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
plt.yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.title("Precision Recall Graph HS20")


plt.show()






