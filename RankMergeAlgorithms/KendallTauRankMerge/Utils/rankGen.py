import numpy as np
import Utils.APFDcalc as apfdCalc
def generate(ListofLines):
    totalNumberOfTestCases,totalNumberOfBugs = map(int,ListofLines[0])
    firstRankList = list(map(int,ListofLines[1]))
    secondRankList = list(map(int,ListofLines[2]))
    print(firstRankList , secondRankList)
    faultMatrix = ([list( map(int,row) ) for row in ListofLines[2:][:]])
    modifiableFaultMatrix = np.array(faultMatrix)
    print(apfdCalc.calcAPFD(totalNumberOfBugs,totalNumberOfTestCases,firstRankList,modifiableFaultMatrix))
    return [0,1,4]


