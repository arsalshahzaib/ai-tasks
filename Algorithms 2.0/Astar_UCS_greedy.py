tree = {
        'A': [['B', 6], ['F', 3]],
        'B': [['A', 6], ['C', 3], ['D', 2]],
        'C': [['B', 3], ['D', 1], ['E', 5]],
        'D': [['B', 2], ['C', 1], ['E', 8]],
        'E': [['C', 5], ['D', 8], ['I', 5], ['J', 5]],
        'F': [['A', 3], ['G', 1], ['H', 7]],
        'G': [['F', 1], ['I', 3]],
        'H': [['F', 7], ['I', 2]],
        'I': [['G', 3], ['H', 2], ['E', 5], ['J', 3]],
        'J': [['E', 5], ['I', 3]]}

heuristic = {'A': 10, 'B': 8, 'C': 5, 'D': 7, 'E': 3, 'F': 6, 'G': 5, 'H': 3, 'I': 1, 'J': 0}

Start_State='A'
Goal_State='J'

vertex=Start_State #starting Node
array=list() # f(n) = g(n) + h(n)
nodelist=list() # Child Nodes from each current node
visited=list() # Visited Node list / Path

while vertex != Goal_State: #Ending while on Goal state
    for j in tree[vertex]: # Traversing childs to save them in nodelist array
        if vertex not in visited: # Checking if node has already been added in path
            visited.append(vertex) # adding vertex to path
        currnode = [j]
        nodelist.append(j)
        array.append(currnode[0][1]+heuristic[j[0]])  # adding heuristic + weight for f(n)
        # ^^^ only current node for UCS, and only heuristic for greedy. ^^^
    while nodelist[array.index(min(array))][0] in visited:
        array[array.index(min(array))] = 63219975
    vertex=nodelist[array.index(min(array))][0]
    if vertex == Goal_State: # Adding Goal state to visited list since loop will be terminated after this
        visited.append(Goal_State)
        
    nodelist.clear() # Clearing Child Nodes to enter child nodes of new current node
    array.clear() #  Clearing f(n) of child nodes to accomodate new f(n) of child nodes

print("Path from Start to Goal: ", visited)