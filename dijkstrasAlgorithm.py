#ohamilton79
#Dijkstra's shortest path algorithm
#02/01/2021

import time

begin = time.time()

#Set up a sample (undirected) weighted graph as a 2D dictionary
graph = {}
graph["a"] = {}
graph["b"] = {}
graph["c"] = {}
graph["d"] = {}
graph["e"] = {}

#Add weights
graph["a"]["b"] = 5
graph["a"]["c"] = 4
graph["a"]["d"] = 2
graph["b"]["a"] = 5
graph["b"]["c"] = 3
graph["c"]["b"] = 3
graph["c"]["a"] = 4
graph["c"]["d"] = 3
graph["d"]["a"] = 2
graph["d"]["c"] = 3
graph["c"]["e"] = 4
graph["e"]["c"] = 4

#Get the node with the shortest distance from the start that hasn't been visited
def getLowestCostNode(graph, costs, visited):
    #Store the node with the lowest cost, and what this lowest cost is
    lowestCostNode = (None, float("inf"))
    #Iterate over each node in the graph
    for node in graph.keys():
        #If the node isn't visited and has a lower cost than the current lowest cost, update it
        if node not in visited and costs[node] <= lowestCostNode[1]:
            lowestCostNode = (node, costs[node])

    #Return the node with the lowest cost
    return lowestCostNode[0]


#Return the shortest path from a start node to a finishing node
def dijkstras(graph, startNode, endNode):
    #Create a dictionary containing the previously visited nodes for each node
    previousNodes = {}
    #Create a dictionary containing the costs for each node (its distance from the start node)
    costs = {}
    #For each node in the graph, initialise its starting cost as infinity...
    for node in graph.keys():
        costs[node] = float("inf")

    #...except the start node, which has a distance of 0 from the start
    costs[startNode] = 0

    #Create a list storing visited nodes
    visited = []

    #Get the node with the lowest cost (distance from start)
    currentNode = getLowestCostNode(graph, costs, visited)

    #While all nodes haven't been visited
    while not currentNode == None:
        #If the current node is the end node, we're done
        if currentNode == endNode:
            break

        #Get the cost for this node
        cost = costs[currentNode]

        #Loop over the adjacent nodes connected to this node
        adjacent = graph[currentNode]

        for node in adjacent.keys():
            #Get the cost of reaching this adjacent node by going through the current node...
            newCost = cost + adjacent[node]
            #If this new cost is less than the currently stored cost for this adjacent node, update it
            if not node in visited and newCost < costs[node]:
                costs[node] = newCost
                #Update the previous node travelled through to be the current node
                previousNodes[node] = currentNode

        #Once all adjacent nodes have been updated, mark this node as visited
        visited.append(currentNode)
            
        #Find the next lowest cost node to visit
        currentNode = getLowestCostNode(graph, costs, visited)

    #Get the shortest path from the start to the end node, and the distance of it
    currentNode = endNode
    pathString = ""
    pathDistance = 0
    while currentNode != startNode:
        #Update the path
        pathString = "-" + currentNode + pathString
        #Update the distance the path covers by adding the distance between the current node and previous node
        pathDistance += graph[currentNode][previousNodes[currentNode]]

        #Get the next node
        currentNode = previousNodes[currentNode]

    #Complete the path string
    pathString = startNode + pathString

    #Return the shortest path and its distance
    return (pathString, pathDistance)

print(dijkstras(graph, "a", "e"))

end = time.time()
print("Time taken: {}".format(end - begin))
