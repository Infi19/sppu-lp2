class Node:
    def __init__(self, state, parent, g, h):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):  # Fix: use double underscore for __lt__
        return self.f < other.f


def manhattan_distance(state, goal_state):
    distance = 0
    for i in range(9):
        if state[i] == 0:
            continue
        xi, yi = divmod(i, 3)
        xg, yg = divmod(goal_state.index(state[i]), 3)
        distance += abs(xg - xi) + abs(yg - yi)
    return distance


def get_neighbors(state):
    neighbors = []
    idx = state.index(0)
    x, y = divmod(idx, 3)
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:  # Fix: use < 3 not <= 3
            n_idx = nx * 3 + ny
            new_state = list(state)
            new_state[idx], new_state[n_idx] = new_state[n_idx], new_state[idx]
            neighbors.append(tuple(new_state))  # Fix: append new_state not original state
    return neighbors


def astar(start_state, goal_state):
    open_list = [Node(start_state, None, 0, manhattan_distance(start_state, goal_state))]
    closed_set = set()

    while open_list:
        open_list.sort()
        current_node = open_list.pop(0)

        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.state)  # Fix: use add() not ()

        for neighbor in get_neighbors(current_node.state):
            if neighbor in closed_set:
                continue

            new_node = Node(neighbor, current_node, current_node.g + 1, manhattan_distance(neighbor, goal_state))
            if any(n.state == neighbor and n.f <= new_node.f for n in open_list):
                continue

            open_list.append(new_node)
    return None


def main():
    start_state = (1, 2, 3,
                   4, 0, 6,
                   7, 5, 8)

    goal_state = (1, 2, 3,
                  4, 5, 6,
                  7, 8, 0)

    result = astar(start_state, goal_state)
    if result:
        print("Solution steps:")
        for state in result:
            for i in range(0, 9, 3):
                print(state[i:i+3])
            print()
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
