#ohamilton79
#13/12/2020
#Merge sort

#Recursive algorithm to perform a merge sort
def mergeSort(items):
    #If array length is not less than or equal to 1
    if len(items) > 1:
        #Get them midpoint of the list
        midPoint = len(items) // 2
        #Take the left and right sublists
        leftList = items[:midPoint]
        rightList = items[midPoint:]

        #Recursively sort the two sublists, split at the midpoint
        mergeSort(leftList)
        mergeSort(rightList)

        #Counter variables
        leftPointer = 0
        rightPointer = 0
        newListPointer = 0

        #While there are still items to insert into the sorted list
        while leftPointer < len(leftList) and rightPointer < len(rightList):
            #If the item in the left list is smaller than the one in the right list, insert it
            if leftList[leftPointer] < rightList[rightPointer]:
                items[newListPointer] = leftList[leftPointer]
                #Increment left pointer
                leftPointer += 1

            #Otherwise, the item in the right list is smaller and can be inserted
            else:
                items[newListPointer] = rightList[rightPointer]
                #Increment the right pointer
                rightPointer += 1

            #Increment new list pointer for next item to be inserted into sorted list
            newListPointer += 1

        #Insert any remaining items, in order, in the left list
        while leftPointer < len(leftList):
            items[newListPointer] = leftList[leftPointer]
            #Increment left pointer and new list pointer for next item to be inserted
            leftPointer += 1
            newListPointer += 1

        #Insert any remaining items in the right list
        while rightPointer < len(rightList):
            items[newListPointer] = rightList[rightPointer]
            #Increment right pointer and new list pointer for next item to be inserted
            rightPointer += 1
            newListPointer += 1


items = [2, 7, 9, 13, 2, 3, 4, 5, 9, 7, 61, 32, 1, 3, 7, 8, 9, 91]
mergeSort(items)
print(items)

                
