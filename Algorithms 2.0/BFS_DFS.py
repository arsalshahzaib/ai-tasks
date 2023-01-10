MyGraph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']
}

def DFS_Iterative_Algorithm(MyGraph,Start):
    Stack,Path=[Start],[]
    while Stack:
        Vertex=Stack.pop()
        if Vertex not in Path:
            Path.append(Vertex)
            for N in MyGraph[Vertex]:
                Stack.append(N)
    return Path
print(DFS_Iterative_Algorithm(MyGraph,'A'))