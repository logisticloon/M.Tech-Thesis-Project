import numpy as np
import Utils.APFDcalc as apfdCalc


def generate(ListofLines):

    ###### Formatting data
    totalNumberOfTestCases,totalNumberOfBugs = map(int,ListofLines[0])
    ###### In RankLists, index represents the rank and the value at the index represent the test case number at that rank. 
    firstRankList = list(map(int,ListofLines[1]))
    secondRankList = list(map(int,ListofLines[2]))

    faultMatrix = ([list( map(int,row) ) for row in ListofLines[3:][:]])
    modifiableFaultMatrix = np.array(faultMatrix)
    
    firstRankMap = [0]*(totalNumberOfTestCases +1) # maps testcase(index) -> rank
    for i in range(totalNumberOfTestCases):
        firstRankMap[firstRankList[i]] = i+1
    secondRankMap = [0]*(totalNumberOfTestCases +1) # maps testcase(index) -> rank
    for i in range(totalNumberOfTestCases):
        secondRankMap[secondRankList[i]] = i+1

    ## object creation for APFD calculation
    #  see the constructor in Utils/APFDcalc.py file 
    #   
    calculator = apfdCalc.APFDCalculator(totalNumberOfBugs,totalNumberOfTestCases,modifiableFaultMatrix)
    #
    #
    ## use calculator object for calculating APFD vaues from here on out

    

    ###### Algorithm Starts here ##################

    firstAPFD = calculator.calcAPFD(firstRankList)
    secondAPFD = calculator.calcAPFD(secondRankList)

    weightedScoreList = [0]*len(firstRankList)
    for testcase in range(1,len(firstRankMap)):
        weightedScoreList[testcase-1] = (firstAPFD*firstRankMap[testcase] + secondAPFD*secondRankMap[testcase])
    return [x+1 for x in ((np.argsort(weightedScoreList)))]

    
    

    





