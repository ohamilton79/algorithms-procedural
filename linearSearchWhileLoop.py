#ohamilton79
#10/01/20201
#Linear search - while loop implementation

#Search for an item in an unordered list
def linearSearch(items, searchItem):
    #Default index is -1 in case search item not in list
    index = -1
    #Flag that stores whether the item  has been found in the list
    found = False
    #Stores the current list position being considered
    currentIndex = 0
    
    #Iterate over list items until search item found or no more list items
    while currentIndex < len(items) and found == False:
        #If the item at this index is the one being searched for, update its index
        if items[currentIndex] == searchItem:
            index = currentIndex
            #Set flag to indicate item has been found and loop can be exited
            found = True

        #Increment the list index being considered
        currentIndex += 1

    #Return the item's index
    return index


print(linearSearch([2, 4, 7, 9, 13, 16], 16))
