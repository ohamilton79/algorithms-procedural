#ohamilton79
#13/12/2020
#Insertion sort

myList = [2, 7, 4, 5, 11, 9]

def insertionSort(myList):
    for i in range(1, len(myList)):
        #Get the current list item
        currentItem = myList[i]

        j = i - 1

        while j >= 0 and myList[j] > currentItem:
            #Shift item to right
            myList[j+1] = myList[j]
            #Decrement list index
            j -= 1

        #Insert item into correct position
        myList[j+1] = currentItem

    #Return the sorted list
    return myList

print(insertionSort(myList))
