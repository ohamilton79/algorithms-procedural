#ohamilton79
#28/12/2020
#Depth-first traversal (for directed graph)
from collections import deque

#Create a sample graph (in adjacency list format)
graph = {}
graph["A"] = ["B", "C"] #A is directly connected to B and C
graph["B"] = ["D"]  #B is directly connected to D
graph["C"] = ["E"]   #C is directly connected to E
graph["D"] = ["E"]  #D is directly  connected to E
graph["E"] = ["B"]  #E is directly connected to B

#Store nodes that have already been visited
visited = []

#Create a stack of nodes that need to be traversed
searchStack = deque()
#Push the root node of the graph onto the stack
searchStack.append("A")
#Mark the root node as visited
visited.append("A")

#Whilst there are still items to be traversed
while len(searchStack) > 0:
    #Pop the next node to be traversed from the stack
    currentNode = searchStack.pop()

    #Output the node
    print(currentNode)

    #Get all nodes adjacent to the current node in the graph
    for adjacentNode in graph[currentNode]:
        #Mark unvisited nodes as visited and push them onto the search stack
        if not adjacentNode in visited:
            visited.append(adjacentNode)
            searchStack.append(adjacentNode)
