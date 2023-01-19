def transpose(arr):
   result = []
   for listIndex, listObj in enumerate(arr):
       for numIndex, num in enumerate(listObj):
           try:
               result[numIndex]
           except IndexError:
               result.append([])
          
           try:
               result[numIndex][listIndex]
           except IndexError:
               result[numIndex].append([])

           result[numIndex][listIndex] = num
   return result

print(transpose( [ [1,2], [3,4] ] ))
print(transpose( [ [1,2,3,4], [5,6,7,8] ] ))