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
    GenRank.generate(formattedLinesList)
    

