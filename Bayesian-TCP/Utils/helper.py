def calculateProbabilityForEachBug(FaultMatrix, BugsCount, TestCaseCount, currentTestCase,currentBug):
    ProbTestCaseDetectsBug = FaultMatrix[currentTestCase][currentBug]/(BugsCount*TestCaseCount)
    if(ProbTestCaseDetectsBug == 0 ):
        return 0
    ProbBugDetected = 0
    for item in FaultMatrix.transpose()[currentBug][:]:
        if(item == 1):
            ProbBugDetected += item 
    ProbBugDetected = ProbBugDetected/(BugsCount*TestCaseCount)
    finalProbValue = ProbTestCaseDetectsBug/ProbBugDetected
    return finalProbValue
    return 0


def calculateAverageProbability(FaultMatrix, BugsCount, TestCaseCount, currentTestCase):
    averageProbability = 0
    for i in range(BugsCount):
        averageProbability += calculateProbabilityForEachBug(
            FaultMatrix,
            BugsCount,
            TestCaseCount,
            currentTestCase,
            i
        )
    averageProbability = averageProbability/BugsCount
    return averageProbability
    
