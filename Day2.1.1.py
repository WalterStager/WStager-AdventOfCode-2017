# Advent of Code
# Day 2 part 1
# Walter Stager

def computeChecksum(inFilePath):
    inFile = open(inFilePath, 'r')
    checkSum = 0
    for line in inFile:
        #print(line)
        
        # produces a list of integers for the line
        intsList = [int(s) for s in lineParser(line)]
        
        #print("%i - %i = %i" % (max(intsList), min(intsList), max(intsList) - min(intsList)))

        # adds current lines value to checksum
        checkSum += max(intsList) - min(intsList)

    # print result
    print(checkSum)
    inFile.close()

# strips leading, trailing whitespace and splits the string
# tailored to this input (aka not a good function for the general use)
def lineParser(line):
    line = line.strip()
    line = line.replace("  ", "")
    return line.split('\t')
