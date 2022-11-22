# DFS
graph = {
    "A": ["B", "C"],
    "B": ["A", "F", "D"],
    "F": ["B"],
    "D": ["B", "C"],
    "C": ["D", "E", "G"],
    "E": ["C"],
    "G": ["C"]
}

print(graph)

start = 'A'
goal = input("Enter the node to search: ")

open = []
open.append(('-', start))

close = []

terminate_loop = False

while not terminate_loop:
    node = open.pop()
    close.append(node)

    if node[1] == goal:
        terminate_loop = True
    else:
        parent = node[1]
        children = graph[parent]

        for x in reversed(children):
            t = (parent, x)

            if t not in close and (x, node[1]) not in close:
                open.append(t)

    print(close)
