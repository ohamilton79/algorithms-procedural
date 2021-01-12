#ohamilton79
#16/12/2020
#Optimised bubble sort
import time

#Sort a list of number by a bubble sort
def bubbleSort(items):
    #Stores the end of the list to be checked - with each pass, one less item at the end needs to be checked
    end = len(items) - 1
    #Stores whether more passes need to be made
    swapsNeeded = True
    #While passes still need to be made
    while swapsNeeded:
        swapsNeeded = False
        #Iterate over each element, so it can be swapped with the adjacent one
        for i in range(0, end):
            #Check if the item at this position is greater than the one to the right
            if items[i] > items[i+1]:
                #Swap the items
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp
                #More passes are needed, as a swap has been made
                swapsNeeded = True

        #Decrement the number of elements that need to be checked in the next iteration
        end -= 1

    #Return the sorted list
    return items

#Get and display the time taken for the algorithm to execute
begin = time.perf_counter()

testList = [2, 4, 3, 7, 9, 16, 13, 8, 1, 3, 5, 20, 17, 13, 12, 11]
print(bubbleSort(testList))

end = time.perf_counter()
print("Time taken: {}".format(end - begin))

            
