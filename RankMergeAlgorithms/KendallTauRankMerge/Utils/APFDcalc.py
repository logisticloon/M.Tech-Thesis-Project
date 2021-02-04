def calcAPFD(totalNumberOfBugs,totalNumberOfTestCases,rankList,modifiableFaultMatrix):
    rankMap = [0]*(len(rankList)+1) # this maps test case to its rank i.e testCaseNumber -> rank
    for i in range (len(rankList)):
        rankMap[rankList[i]] = i+1

    # print(rankList)
    # print(rankMap)
    APFD = 1 + (1/(2*totalNumberOfTestCases))
    for i in range (totalNumberOfBugs):
        for j in range(totalNumberOfTestCases):
            testcaseNo = rankList[j]
            if(modifiableFaultMatrix[testcaseNo-1][i]==1):
                APFD -= (j+1)/(totalNumberOfTestCases*totalNumberOfBugs)
                # print(APFD)
                break
    
    return APFD
