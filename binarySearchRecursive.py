#ohamilton79
#10/01/2021
#Binary search - recursive approach

#Search for an item in an ordered list of items
def binarySearch(items, searchItem, start=0, end=None):
    #Detect sentinel value and define end of list
    if end == None:
        end = len(items) - 1
    #Calculate the midpoint of the section of the list being examined
    midpoint = (start + end) // 2

    #If the item at this location is the item being searched for
    if items[midpoint] == searchItem:
        #Return the index of the item
        return midpoint

    #Otherwise, if the item at this location is less than the search item
    elif items[midpoint] < searchItem:
        #Discard the left half of the list, and perform a binary search on the right
        return binarySearch(items, searchItem, midpoint + 1, end)

    #Else, if the item at this location is more than the search item
    else:
        #Discard the right half of the list, and perform a binary search on the left
        return binarySearch(items, searchItem, start, midpoint - 1)

print(binarySearch([2, 3, 7, 9, 13, 17], 17))
