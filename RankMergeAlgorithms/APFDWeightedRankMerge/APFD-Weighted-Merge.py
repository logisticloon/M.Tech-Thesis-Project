""" 

    This is the main python file which initiates the program.

"""

import sys
import Utils.rankGen as GenRank
import Utils.readFile as ReadFile
from configparser import ConfigParser


if __name__=="__main__":
    config_object = ConfigParser()
    config_object.read('config.ini')
    FilePath = config_object["PATHS"]['InputFilePath']
    print("Reading Fault matrix from file at : ",FilePath)
    formattedLinesList = ReadFile.ReadAndFormatFile()
    rankList = GenRank.generate(formattedLinesList) # contains final Rank List
    print("\n\n______________________________________________\n\n")
    print("The Ranking of " + str(len(rankList)) + " Test Cases is as follows:\n")
    for i in range (len(rankList)):
        print("Rank", (i+1),"-> Test Case",rankList[i])
    print("\n______________________________________________\n\n")
    print (" ".join(map(str,rankList)))

    

