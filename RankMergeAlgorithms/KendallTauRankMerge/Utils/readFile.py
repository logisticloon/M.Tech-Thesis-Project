from configparser import ConfigParser

def ReadAndFormatFile():
    config_object = ConfigParser()
    (config_object.read('config.ini'))
    FilePath = config_object["PATHS"]["InputFilePath"]
    with open(FilePath) as textFile:
        linesList = [line.split() for line in textFile]
    formattedLinesList = []
    for line in linesList:
        if(line != []):
            formattedLinesList.append(line)
    return formattedLinesList
