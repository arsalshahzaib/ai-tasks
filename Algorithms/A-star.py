#A* ALGORITHM

G = {
    'S': [('A', 1), ('G', 10)],
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 5)],
    'C': [('D', 3), ('G', 4)],
    'D': [('G', 2)],

}

H = {
    'S': 5,
    'A': 3,
    'B': 4,
    'C': 2,
    'D': 6,
    'G': 0,
}

open = []
close = []
goal = input("Enter the goal node: ")
root = 'S'
g = 0

r = ('-', root, H[root])

open.append(r)

terminatedLoop = True

while terminatedLoop:
    v = open.pop(0)
    close.append(v)
    if v[1] == goal:
        print("Goal Node Found: ", v[1])
        terminatedLoop = False
    else:
        for i in G[v[1]]:
            if i[0] not in [x[1] for x in close]:
                g = v[2] - H[v[1]] + i[1]
                r = (v[1], i[0], g + H[i[0]])

                open.append(r)
                open.sort(key=lambda x: x[2])
        if len(open) == 0:
            print("not found")
            terminatedLoop = False
print("open: ", open)
print("close: ", close)

# CALCULATING THE PATH FROM CLOSED
path = [goal]

while path[-1] != root:
    for i in close:
        if i[1] == path[-1]:
            path.append(i[0])
path.reverse()
print("path: ", path)
