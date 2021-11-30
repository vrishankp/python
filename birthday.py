import random

numInter = int(input("Enter how many iterations: "))
birthday = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

def checkIfDuplicates1(listOfElems):
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True

numMatch = 0

for i in range(0, numInter - 1):
    for j in range(0,23):
        birthday[j] = random.randint(1,365)



    isTrue = checkIfDuplicates1(birthday)
    #print(birthday)
    #print(isTrue)
    if (isTrue):
        numMatch = numMatch + 1
    else:
        numMatch = numMatch
print(numMatch / numInter)
