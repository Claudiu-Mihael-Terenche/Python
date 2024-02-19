# Python3 implementation to build a graph using dictionaries
from collections import defaultdict


def build_graph():  # function to build the graph
    edges = [['A', 'B'], ['A', 'E'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['C', 'G'], ['D', 'E']]
    graph01 = defaultdict(list)

    for edge in edges:  # loop to iterate over every edge of the graph
        a, b = edge[0], edge[1]
        graph01[a].append(b)  # creating the graph as an adjacency list
        graph01[b].append(a)
    return graph01


if __name__ == '__main__':
    graph1 = build_graph()
    print(graph1)


# Python implementation to find the shortest path in the graph using dictionaries

# Function to find the shortest path between two nodes of a graph

def bfs_sp(graph02, start, goal):
    explored = []
    queue = [[start]]  # queue for traversing the graph in the BFS

    if start == goal:  # if the desired node is reached
        print('Same node')
        return

    while queue:  # loop to traverse the graph with the help of the queue
        path = queue.pop(0)
        node = path[-1]

        if node not in explored:  # condition to check if the current node is not visited
            neighbours = graph02[node]

            for neighbour in neighbours:  # loop to iterate over the neighbors of the node
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == goal:  # condition to check if the neighbor node is the goal
                    print('Shortest path = ', *new_path)
                    return
            explored.append(node)

    print('So sorry, but a connecting'
          'path does not exist :(')  # condition when the nodes are not connected
    return


if __name__ == '__main__':
    graph2 = {'A': ['B', 'E', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F', 'G'], 'D': ['B', 'E'],
              'E': ['A', 'B', 'D'], 'F': ['C'], 'G': ['C']}  # graph using dictionaries

    bfs_sp(graph2, 'A', 'D')  # function call
