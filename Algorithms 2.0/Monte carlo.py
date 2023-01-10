import random
# Monte carlo


class Node:
    def _init_(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0

    def add_child(self, child_state):
        child = Node(child_state, self)
        self.children.append(child)
        return child

    def update(self, result):
        self.visits += 1
        self.wins += result

    def get_uct_value(self, c=1.4):
        return self.wins / self.visits + c * sqrt(2 * log(self.parent.visits) / self.visits)

    def get_best_child(self, c=1.4):
        best_score = -float('inf')
        best_child = None
        for child in self.children:
            score = child.get_uct_value(c)
            if score > best_score:
                best_score = score
                best_child = child
        return best_child


def select_node(node):
    while len(node.children) > 0:
        node = node.get_best_child()
    return node


def expand_node(node, state_fn):
    possible_states = state_fn(node.state)
    if len(possible_states) == 0:
        return node
    return node.add_child(random.choice(possible_states))


def simulate_playout(node, playout_fn):
    result = playout_fn(node.state)
    return result


def backpropagate(node, result):
    while node is not None:
        node.update(result)
        node = node.parent


def monte_carlo_tree_search(root, state_fn, playout_fn):
    node = select_node(root)
    node = expand_node(node, state_fn)
    result = simulate_playout(node, playout_fn)
    backpropagate(node, result)


def get_best_move(root, c=1.4):
    best_score = -float('inf')
    best_move = None
    for child in root.children:
        score = child.wins / child.visits + c * \
            sqrt(2 * log(root.visits) / child.visits)
        if score > best_score:
            best_score = score
            best_move = child.state
    return best_move
