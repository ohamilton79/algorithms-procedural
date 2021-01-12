#ohamilton79
#10/01/20201
#Linear search - for loop implementation

#Search for an item in an unordered list
def linearSearch(items, searchItem):
    #Default index is -1 in case search item not in list
    index = -1
    #Iterate over each list index in order
    for i in range(len(items)):
        #If the item at this index is the one being searched for, return its index
        if items[i] == searchItem:
            #Update index of search item
            index = i

    #Return the index of the item or -1 if not found
    return index

print(linearSearch([2, 4, 7, 9, 13, 16], 7))
