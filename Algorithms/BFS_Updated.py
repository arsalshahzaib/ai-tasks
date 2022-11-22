graph = {
    "A": ["B", "D"],
    "B": ["A", "C", "D"],
    "C": ["B", "D"],
    "D": ["A", "B", "C", "G"],
    "G": ["D"]
}

open = []
closed = []

available_nodes = graph.keys()
print("Available nodes:", end=" ")
for node in available_nodes:
    print(node, end=" ")
print("")

starting_node = input("Enter starting node: ")
while not available_nodes.__contains__(starting_node):
    print("Invalid node selected!")
    starting_node = input("Enter starting node: ")

final_node = input("Enter final node: ")
while not available_nodes.__contains__(final_node):
    print("Invalid node selected!")
    final_node = input("Enter final node: ")

starting_pair = ("/", starting_node)
open.append(starting_pair)

terminate_loop = False
while not terminate_loop:
    if len(open) == 0:
        terminate_loop = True
    else:
        current_pair = open.pop()
        closed.append(current_pair)

        current_node = current_pair[1]

        if current_node == final_node:
            terminate_loop = True
        else:
            adjacent_to_current_node = graph[current_node]

            for index in range(0, len(adjacent_to_current_node)).__reversed__():
                adjacent_node = adjacent_to_current_node[index]

                visited_nodes = []
                for item in closed:
                    visited_nodes.append(item[1])

                if not visited_nodes.__contains__(adjacent_node):
                    next_pair = (current_node, adjacent_node)
                    open.append(next_pair)

print(closed)


def find_pair(node):
    for item in closed:
        if item[1] == node:
            return item


current_pair = find_pair(final_node)
print(current_pair[1], end=" <- ")

terminate_loop = False
while not terminate_loop:
    if current_pair[0] == '/':
        terminate_loop = True
    else:
        current_pair = find_pair(current_pair[0])
        print(current_pair[1], end=" <- ")

print('/')
