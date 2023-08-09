NestedList = [[1, 2, 3],[4, 5],[6, 7 ,8, 9]]

import projectLibrary

lenths = int(input('Enter the length you think this list has'))

while lenths != len(NestedList):
    if lenths == len(NestedList):
         print('correct')
         sum = 0
         count = 0
         for SubList in NestedList:
             for x in SubList:
                 count += 1
                 sum += x

         print(sum)
         print(count)
         average = sum / count

         print("The average of all the elements present in list are", average)

         NestedList = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
         for i in NestedList:
             for j in i:
               print(j)
    else:
         print('incorrect')
    lenths = int(input('Enter the length you think this list has'))

    if lenths == len(NestedList):
         print('correct')
         sum = 0
         count = 0
         for SubList in NestedList:
             for x in SubList:
                 count += 1
                 sum += x

         print(sum)
         print(count)
         average = sum / count

         print("The average of all the elements present in list are", average)

         NestedList = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
         for i in NestedList:
             for j in i:
               print(j)