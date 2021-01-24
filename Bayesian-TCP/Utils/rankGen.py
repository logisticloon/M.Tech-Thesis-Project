import numpy as np
import Utils.helper as helper

def generate(ListofLines):
    totalNumberOfTestCases,totalNumberOfBugs = map(int,ListofLines[0])
    faultMatrix = ([list( map(int,row) ) for row in ListofLines[1:][:]])
    modifiableFaultMatrix = np.array(faultMatrix)
    print(modifiableFaultMatrix)
    probabilityValueListofTestCases = []
    for i in range(totalNumberOfTestCases):
        probabilityValueListofTestCases.append(
            helper.calculateAverageProbability(
                modifiableFaultMatrix,
                totalNumberOfBugs,
                totalNumberOfTestCases,
                i
            )
        )
    probabilityValueListofTestCases = np.array(probabilityValueListofTestCases)
    rankList = np.argsort(-probabilityValueListofTestCases) # negate array to sort in descending order
    rankList = [x+1 for x in rankList]

    return rankList



