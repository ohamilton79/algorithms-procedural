#ohamilton79
#28/12/2020
#Breadth-first traversal (for directed graph)
from collections import deque

#Create a sample graph (in adjacency list format)
graph = {}
graph["A"] = ["B", "C"] #A is directly connected to B and C
graph["B"] = ["D"]  #B is directly connected to D
graph["C"] = ["E"]   #C is directly connected to E
graph["D"] = ["E"]  #D is directly  connected to E
graph["E"] = ["B"]  #E is directly connected to B

#Stores nodes that have already been visited
visited = []

#Create a queue of nodes that need to be traversed
searchQueue = deque()
#Enqueue the root node of the graph
searchQueue.appendleft("A")
#Mark the root node as visited
visited.append("A")

#Whilst there are still items to be traversed
while len(searchQueue) > 0:
    #Dequeue the next node to be traversed from the queue
    currentNode = searchQueue.pop()

    #Output the node
    print(currentNode)

    #Get all nodes adjacent to this node in the graph
    for adjacentNode in graph[currentNode]:
        #Mark unvisited nodes as visited and enqueue them
        if not adjacentNode in visited:
            visited.append(adjacentNode)
            searchQueue.appendleft(adjacentNode)
    
