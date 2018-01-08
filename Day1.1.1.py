def sumOfMatch(inString):
    sum = 0
    # for range 0 to length of string
    for i in range(0, len(inString)):
        #print("%c %i\n" % (inString[(i)%len(inString)], i))
        # if current char matcher next char (with wrapping at end of string)
        if inString[(i+1)%len(inString)] == inString[i]:
            sum += int(inString[i])
    # print result
    print(sum)
            

