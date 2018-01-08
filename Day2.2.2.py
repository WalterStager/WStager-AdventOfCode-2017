# Advent of Code
# Day 2 part 2
# Walter Stager

def computeDivisibileChecksum(inFilePath):
    inFile = open(inFilePath, 'r')
    checkSum = 0
    for line in inFile:
        #print(line)
        
        # produces a list of integers for the line
        intsList = [int(s) for s in lineParser(line)]

        # adds current lines value to checksum
        checkSum += quotientOfDivisibleElements(intsList)

    # print result
    print(checkSum)
    inFile.close()

# return true if num1 is divisible by num2 or the other way around
def areDivisible(num1, num2):
    # if divisible to whole number
    if ((num1 % num2) == 0 or(num2 % num1) == 0):
        return True
    else:
        return False

# get the difference of the 1st set of two divisible elements in the list of integers
# more efficient in its own function since 'return' breaks out of the for loops easily
def quotientOfDivisibleElements(integerList):
    for i in integerList:
        for j in integerList:
            if areDivisible(i, j) and i != j:
                #print("%i - %i = %i" % (i, j, int(max({i, j})/min({i, j}))))
                return int(max({i, j})/min({i, j}))

# strips leading, trailing whitespace and splits the string
# tailored to this input (aka not a good function for the general use)
def lineParser(line):
    line = line.strip()
    line = line.replace("  ", "")
    return line.split('\t')
