from queue import PriorityQueue

v = 14
graph = [[] for i in range(v)]


# Function For Implementing Best First Search
# Gives output path having lowest cost


def best_first_search(actual_src, goal, n):
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, actual_src))
    visited[actual_src] = True

    while not pq.empty():
        u = pq.get()[1]
        # Displaying the path having lowest cost
        print(u, end=" ")
        if u == goal:
            break

        for v, c in graph[u]:
            if not visited[v]:
                visited[v] = True
                pq.put((c, v))
    print()


# Function for adding edges to graph


def add_edge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))


# The nodes shown in above example(by alphabets) are
# implemented using integers addedge(x,y,cost);
add_edge(0, 1, 3)
add_edge(0, 2, 6)
add_edge(0, 3, 5)
add_edge(1, 4, 9)
add_edge(1, 5, 8)
add_edge(2, 6, 12)
add_edge(2, 7, 14)
add_edge(3, 8, 7)
add_edge(8, 9, 5)
add_edge(8, 10, 6)
add_edge(9, 11, 1)
add_edge(9, 12, 10)
add_edge(9, 13, 2)

source = 0
target = 9
best_first_search(source, target, v)
