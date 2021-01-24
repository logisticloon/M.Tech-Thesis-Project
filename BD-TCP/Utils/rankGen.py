import numpy as np

def generate(ListofLines):
    totalNumberOfTestCases,totalNumberOfBugs = map(int,ListofLines[0])
    faultMatrix = ([list( map(int,row) ) for row in ListofLines[1:][:]])
    modifiableFaultMatrix = np.array(faultMatrix)
    numberOfTestCasesUsed = 0
    numberOfBugsCovered = 0
    rankList = []
    isTestCaseUsed = [0]*totalNumberOfTestCases
    while( numberOfTestCasesUsed != totalNumberOfTestCases):
        maxbugscovered = -1
        indexCoveringMaxBugs = -1; 
        for i in range(totalNumberOfTestCases):
            if(isTestCaseUsed[i]==0):
                bugsCovered = 0
                for x in modifiableFaultMatrix[i]:
                    if(x==1): 
                        bugsCovered += 1
                if(maxbugscovered < bugsCovered):
                    
                    maxbugscovered = bugsCovered
                    indexCoveringMaxBugs = i
        
        
        coveredBugsIndexList  = []
        for i in range(len(modifiableFaultMatrix[indexCoveringMaxBugs])):
            if(modifiableFaultMatrix[indexCoveringMaxBugs][i]==1):
                coveredBugsIndexList.append(i)
        modifiableFaultMatrix =  np.delete(modifiableFaultMatrix,coveredBugsIndexList,axis=1)
        rankList.append((indexCoveringMaxBugs+1))
        isTestCaseUsed[indexCoveringMaxBugs]=1
        numberOfTestCasesUsed += 1
        numberOfBugsCovered += maxbugscovered
    
    return rankList


