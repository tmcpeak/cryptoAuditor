import os

def getLibsAndFuncsFromFile(listFile):
    '''
    gets lists of libraries and functions to check for from a dictionary file

    the dictionary file contains two sections [libs] and [funcs], anything before [libs] is ignored
     libs will be checked in any line that contains the import keyword
     functions will be matched anywhere in the source

    function returns two lists: libs and funcs
    '''

    file = open(listFile, 'r')

    currentlyReading = 'none'
    libs = []
    funcs = []

    '''
    step through each line in the crypto dictionary file,
        if the line contains [libs] it marks the start of the libs section, read into the libs list until
        the line contains [funcs], at which point the functions section begins
        while in the libs or funcs section read the library or function into the appropriate list
    '''
    for line in file:
        if '[libs]' in line:
            currentlyReading = 'libs'
        elif '[funcs]' in line:
            currentlyReading = 'funcs'
        # empty lines are ignored, whitespace is stripped out
        elif len(line.strip()) > 0 and currentlyReading == 'libs':
            libs.append(line.strip())
        elif len(line.strip()) > 0 and currentlyReading == 'funcs':
            funcs.append(line.strip())

    file.close()

    return libs, funcs

def displayResults(results):
    for result in results:
        print(result)

def main():
    listFile = 'CryptoDict.txt'
    checkDir = '/Users/travis_mcpeak/Documents/CPE/glance-master/glance'

    libs, funcs = getLibsAndFuncsFromFile(listFile)

    results = []

    # go through all files/sub-directories from the root directory
    for root, dirs, files in os.walk(checkDir):
        for file in files:
            # only look at Python code
            if file.endswith('.py'):
                # open the file and set the current line counter to 1
                curFile = open(os.path.join(root, file), 'r')
                curLine = 1

                # go through the file line by line
                for line in curFile:
                    # if the line has import in it, check it against the libs
                    if 'import' in line:
                        for lib in libs:
                            # ignore case
                            if lib.lower() in line.lower():
                                # the result is the line number and file in which the result was found, along with the
                                # line itself
                                result = '(' + str(curLine) + ') ' + file + ': ' + line
                                results.append(result)
                    # otherwise check it against the functions
                    else:
                        for func in funcs:
                            if func.lower() in line.lower():
                                result = '(' + str(curLine) + ') ' + file + ': ' + line
                                results.append(result)
                    curLine += 1

    displayResults(results)

if __name__ == "__main__":
    main()
