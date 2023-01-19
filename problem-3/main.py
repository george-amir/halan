def runLengthEncode(string):
   counter = 1
   currentChar = None
   finalString = ''
   strLen = len(string)
   for index, char in enumerate(string):
       if currentChar == None:
           currentChar = char
       elif currentChar == char:
           counter += 1
       else:
           finalString += currentChar+str(counter)
           currentChar = char
           counter = 1
           if (index+1) == strLen:
               finalString += currentChar+str(counter)
   return finalString

def runLengthDecode(string):
   currentChar = None
   currentNumber = None
   finalString = ''
   strLen = len(string)
   for index, char in enumerate(string):
       if not char.isdigit():
           if currentNumber != None:
               finalString += currentChar * int(currentNumber)
               currentNumber = None
           currentChar = char
       else:
           if currentNumber == None:
               currentNumber = char
           else:
               currentNumber += char
           if (index+1) == strLen:
               finalString += currentChar * int(currentNumber)
   return finalString

print(runLengthEncode("aaaaaaaaaabbbaxxxxyyyzyx"))
print(runLengthDecode("a10b3a1x4y3z1y1x1"))