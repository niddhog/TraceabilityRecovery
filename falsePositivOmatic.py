#@Christian Aeberhard
import csv


def calculatePrecision(c,r):
    return abs(c) / abs(r)

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
        except (IndexError):
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
    newFile.writerow (x)


for i in falsePositiveContainer:
    retrieved += 1
    if(i[3] == "1"):
        totalCorrect += 1
    #print(i)

#Adjust to change precision and recall

for iteration in range(0,1410):
    correct = 0
    for r in range(0,iteration):
        if(falsePositiveContainer[r][3] == "1"):
            correct += 1
    precisionRecallContainer.append([calculatePrecision(correct, retrieved),calculateRecall(correct, totalCorrect)])
    #print("precision: " + str(calculatePrecision(correct, retrieved)))
    #print("recall: " + str(calculateRecall(correct, totalCorrect)))




#Precision, Recall
for n in precisionRecallContainer:
    print(n)

print("correct: " + str(correct))
print("totalcorrect: " + str(totalCorrect))
print("retrieved: " + str(retrieved))

#print("precision: " + str(calculatePrecision(correct,retrieved)))
#print("recall: " + str(calculateRecall(correct,totalCorrect)))






