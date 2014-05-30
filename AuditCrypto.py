import os
import ConfigParser
from optparse import OptionParser

def displayResults(results):
    for result in results:
        print(result)

def scanDirectory(directory, scanItems):
    # go through all files/sub-directories from the root directory
    results = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            # only look at Python code
            if file.endswith('.py'):
                # open the file and set the current line counter to 1
                curFile = open(os.path.join(root, file), 'r')
                curLine = 1

                # go through the file line by line, and check if it is in each scan item
                for line in curFile:
                    for item in scanItems:
                        (keywords, outFile, procComments) = scanItems[item]
                        # remove comments if told to do so
                        scanLine = getCodeFromLine(line, procComments)
                        foundKeyword=False
                        if item == 'libs':
                            # for libs, only check lines with import in them
                            for keyword in keywords:
                                if keyword.lower() in scanLine.lower() and 'import' in scanLine.lower():
                                    foundKeyword=True
                        else:
                            for keyword in keywords:
                                # if the keyword matches in the line, add it to the results for this item
                                if keyword.lower() in scanLine.lower():
                                    foundKeyword=True
                        if foundKeyword:
                            result = '(' + str(curLine) + ')' + file + ':' + scanLine
                            if item not in results.keys():
                                results[item] = []
                            results[item].append(result)
                    curLine += 1
    return results

def parseConfigFile(configFile):
    config = ConfigParser.ConfigParser()
    config.read(configFile)

    scanItems = {}

    for section in config.sections():
        keywords = []
        outFile = ''
        procComments = True

        # if section doesn't contain keywords, it doesn't do anything, skip it
        if config.get(section, 'keywords') is not None:
            # get all keywords listed in the section, remove any spaces, and convert to a list
            keywords = config.get(section, 'keywords').replace(' ', '').split(',')

            # set output file to what is listed in the file if it exists, otherwise default to
            #    section_name.txt
            if config.has_option(section, 'output_file'):
                outFile = config.get(section, 'output_file')
            else:
                outFile = section + '.txt'

            if not config.has_option(section, 'process_comments'):
                procComments = True
            elif config.get(section, 'process_comments') == 'False':
                procComments = False
            else:
                procComments = True

            # each section has the section name, the keywords list, the output file, and whether to process comments
            scanItems[section]=(keywords, outFile, procComments)
    return scanItems

def getCodeFromLine(curLine, includeComments):
    # This function is to remove single line comments from a line of code.  Anything after the '#' is not returned
    # TODO: Add some support for recognizing multi-line comments
    if not includeComments and not curLine.find('#') == -1:
        returnValue = curLine[:curLine.find('#')]
    else:
        returnValue = curLine
    return returnValue

def writeResults(scanItems, results):
    for key in results.keys():
        (keywords, outFile, procComments) = scanItems[key]
        curFile = open(outFile, 'w')
        for result in results[key]:
            curFile.write(result)
        curFile.close()

def main():
    parser = OptionParser()
    parser.add_option('-c', '--conf', dest='configFile', help='file which contains config of what to look for',
                      default='cryptoConfig.txt')
    parser.add_option('-d', '--directory', dest='checkDir', help='root directory of code to scan',
                      default='./')
    (options, args) = parser.parse_args()

    scanItems = parseConfigFile(options.configFile)
    results = scanDirectory(options.checkDir, scanItems)
    writeResults(scanItems, results)

if __name__ == "__main__":
    main()
