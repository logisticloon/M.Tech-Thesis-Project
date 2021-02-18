class APFDCalculator:
    def __init__(self,totalNumberOfBugs,totalNumberOfTestCases,modifiableFaultMatrix):
        self.totalNumberOfBugs = totalNumberOfBugs
        self.totalNumberOfTestCases = totalNumberOfTestCases
        self.modifiableFaultMatrix = modifiableFaultMatrix

    def calcAPFD(self,rankList):
        rankMap = [0]*(len(rankList)+1) # this maps test case to its rank i.e testCaseNumber -> rank
        for i in range (len(rankList)):
            rankMap[rankList[i]] = i+1
        APFD = 1 + (1/(2.0*self.totalNumberOfTestCases))
        for i in range (self.totalNumberOfBugs):
            for j in range(self.totalNumberOfTestCases):
                testcaseNo = rankList[j]
                if(self.modifiableFaultMatrix[testcaseNo-1][i]==1):
                    APFD -= (j+1)/(self.totalNumberOfTestCases*self.totalNumberOfBugs)
                    break
        
        return APFD
