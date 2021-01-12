#ohamilton79
#13/12/2020
#Quicksort

def quicksort(items, start, end):
    #Base case - an empty list is sorted
    if start >= end:
        return

    #Stores the pivot value (at the start of the list)
    pivotValue = items[start]

    #Low pointer - initially directly after pivot position
    lowPointer = start + 1
    #High pointer - initially at end of list
    highPointer = end
    #Stores whether the correct position for the pivot has been found
    pivotPosFound = False

    #While the correct pivot position hasn't been found
    while not pivotPosFound:
        #Move the low pointer over values less than the pivot
        while lowPointer <= end and items[lowPointer] < pivotValue:
            #Increment low pointer
            lowPointer += 1

        #Move the high pointer down over values greater than the pivot
        while highPointer >= start and items[highPointer] > pivotValue:
            #Decrement high pointer
            highPointer -= 1

        #If the low mark and high mark haven't crossed each other, swap their values
        if lowPointer < highPointer:
            temp = items[lowPointer]
            items[lowPointer] = items[highPointer]
            items[highPointer] = temp

        #Otherwise, the correct pivot position has been found
        else:
            pivotPosFound = True

    #Swap the pivot with the value at the high pointer
    items[start] = items[highPointer]
    items[highPointer] = pivotValue

    #Perform the algorithm on the two partitions either side of the pivot
    quicksort(items, start, highPointer - 1)
    quicksort(items, highPointer + 1, end)

myList = [2, 8, 4, 5, 3, 1, 27, 54, 17, 19, 58, 61, 99, 72, 1, 3]
quicksort(myList, 0, len(myList)-1)
print(myList)
