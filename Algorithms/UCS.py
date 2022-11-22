# MUHAMMAD ASIF KHAN
# SP20-BCS-130

from queue import PriorityQueue

graph = {
    'A': [('B', 8), ('C', 2)],
    'B': [('A', 8), ('D', 2)],
    'C': [('A', 2), ('E', 5), ('G', 20)],
    'D': [('B', 2), ('E', 5), ('F', 8)],
    'E': [('D', 5), ('C', 5), ('G', 14)],
    'G': [('C', 20), ('E', 14)],
    'F': [('D', 8)],
}
print(graph)

S = 'A'

open = PriorityQueue()
close = []

open.put((0, '-', S))

terminate = False
target = input("Enter a Node to Search: ")

while not terminate:

    v = open.get()
    close.append(v)

    if v[2] == target:
        print("Target Found ===", v[2])
        terminate = True
    else:
        for i in graph[v[2]]:
            if i[0] not in [j[1] for j in close]:
                open.put((v[0] + i[1], v[2], i[0]))

    if open.empty():
        terminate = True

print("Cost: ", close[-1][0])