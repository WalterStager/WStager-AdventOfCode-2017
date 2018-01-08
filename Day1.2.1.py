def sumOfMatchingHalfAround(inString):
    sum = 0
    # useful values if the program was longer
    inStrLen = len(inString)
    jumpDist = int(inStrLen/2)
    print("jdist %i, len %i" % (jumpDist, inStrLen))
    
    for i in range(0, inStrLen):
        #print(print("%c @ %i\n" % (inString[(i)%inStrLen], i%inStrLen))
        # if current char matches the character jumpDist away (with wrapping)
        if inString[i] == inString[(i + jumpDist) % inStrLen]:
            sum += int(inString[i])

    # output result
    print(sum)
        
