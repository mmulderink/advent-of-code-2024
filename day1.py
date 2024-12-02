# Part 1
totalDiff = 0 # to submit

content = ""
leftCodes = []
rightCodes = []

with open('day 1/data.txt', 'r') as file:
    for i in range(1000):
        leftCodes.append(int(file.read(5)))
        file.read(3)
        rightCodes.append(int(file.read(5)))
        file.read(1)

    #print(content)
    file.close()

#print(leftCodes)
#print(rightCodes)

leftCodes.sort()
rightCodes.sort()

for leftCode, rightCode in zip(leftCodes, rightCodes):
    totalDiff += abs(leftCode - rightCode)
    #print(leftCode, rightCode)

# Part 1 Solution
print("Total Diff (P1):", totalDiff)



# Part 2 Solution
similarityScore = 0 # to submit

rightMap = dict()

for rightCode in rightCodes:
    if rightCode in rightMap:
        rightMap.update({rightCode: rightMap[rightCode] + 1})
    else:
        rightMap[rightCode] = 1

#for rightCode, occurances in rightMap.items():
    #if occurances > 1:
        #print(rightCode, occurances)


for leftCode in leftCodes:
    if leftCode in rightMap:
        similarityScore += rightMap[leftCode] * leftCode
    
print("Similarity Score (P2):", similarityScore)
