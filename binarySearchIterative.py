#ohamilton79
#10/01/2021
#Binary search - iterative approach

#Search for an item in an ordered list of items
def binarySearch(items, searchItem):
    #Initialise variables
    index = -1
    found = False
    first = 0
    last = len(items) - 1
    #While the item hasn't been found
    while first <= last and found == False:
        #Find the midpoint, rounding down the result of the division
        midpoint = (first + last) // 2

        #If the item is at the midpoint, the item has been found
        if items[midpoint] == searchItem:
            found = True
            #Set the index of the item to the midpoint
            index = midpoint

        #Otherwise, if this item is less than the desired item, the left half of the list can be discarded
        elif items[midpoint] < searchItem:
            first = midpoint + 1

        #Else, discard the right half of the list (midpoint greater than search item)
        else:
            last = midpoint - 1

    #Return the index of the item
    return index
        
    
print(binarySearch([2, 4, 7, 9, 13, 16], 7))
