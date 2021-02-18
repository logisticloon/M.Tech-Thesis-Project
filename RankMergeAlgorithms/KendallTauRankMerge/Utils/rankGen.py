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

    ###### Algorithm Starts here ##################

    conflictingPairs = [] ##### list of pairs of conflicting ranks, the pair again is a list of size 2

    for i in range(1,totalNumberOfTestCases):
        for j in range(i+1,totalNumberOfTestCases+1):
            if((firstRankMap[i] - firstRankMap[j]) * (secondRankMap[i] - secondRankMap[j]) < 0): #checking conflict
                conflictingPairs.append([i,j])
    totalNumberOfConflicts = len(conflictingPairs)
    
    ##object creation for APFD calculation 
    calculator = apfdCalc.APFDCalculator(totalNumberOfBugs,totalNumberOfTestCases,modifiableFaultMatrix)
    ## use calculator object for calculating APFD vaues from here on out

    bestAPFDSoFar  = 0
    bestRankListSoFar = firstRankList
    Data = {
        "calculator"        : calculator,
        "rankList"          : firstRankList,
        "rankMap"           : firstRankMap,
        "conflicts"         : conflictingPairs,
        "#conflicts"        : totalNumberOfConflicts,
        "bestAPFDSoFar"     : bestAPFDSoFar,
        "bestRankListSoFar" : bestRankListSoFar
    }
    bestOfAllPossiblePermuations(Data,0)
    return Data["bestRankListSoFar"],Data["bestAPFDSoFar"]


def bestOfAllPossiblePermuations(Data,currentIndex):
    calculator = Data["calculator"]
    rankList = Data["rankList"]
    rankMap = Data["rankMap"]
    conflictPairList = Data["conflicts"]
    lengthOfConflictingPairList = Data["#conflicts"]
    if(currentIndex == lengthOfConflictingPairList):
        return
    #check if ignoring the swap yeilds better results
    currentAPFD = calculator.calcAPFD(rankList)
    if( currentAPFD > Data["bestAPFDSoFar"]):
        Data["bestAPFDSoFar"] = currentAPFD
        Data["bestRankListSoFar"] = rankList
        
        ##recursive call
    bestOfAllPossiblePermuations(Data,currentIndex+1)


    #do the swap and backtrack also
    conflictingPair = conflictPairList[currentIndex]
    conflictingTestCaseOne = conflictingPair[0]
    conflictingTestCaseTwo = conflictingPair[1]
    rankMap[conflictingTestCaseOne],rankMap[conflictingTestCaseTwo] = rankMap[conflictingTestCaseTwo],rankMap[conflictingTestCaseOne] 
    rankList[rankMap[conflictingTestCaseOne]-1] = conflictingTestCaseOne
    rankList[rankMap[conflictingTestCaseTwo]-1] = conflictingTestCaseTwo
    currentAPFD = calculator.calcAPFD(rankList)
    if( currentAPFD > Data["bestAPFDSoFar"]):
        Data["bestAPFDSoFar"] = currentAPFD
        Data["bestRankListSoFar"] = rankList 
    bestOfAllPossiblePermuations(Data,currentIndex+1)

        ##backtrack
    rankMap[conflictingTestCaseOne],rankMap[conflictingTestCaseTwo] = rankMap[conflictingTestCaseTwo],rankMap[conflictingTestCaseOne] 
    rankList[rankMap[conflictingTestCaseOne]-1] = conflictingTestCaseOne
    rankList[rankMap[conflictingTestCaseTwo]-1] = conflictingTestCaseTwo

    return



