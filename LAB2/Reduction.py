def perform_reduction(V, E, m, edges):
    """
    Function that perform  the reduction of the graph coloring problem to the casting problem
    :param V: number of vertices
    :param E: number of edges
    :param m: number of colors
    :param edges: list of edges
    :return: None
    """
    # Isolated vertices

    scenes = []
    nonAlone = set()
    for u, v in edges:  # E
        nonAlone.add(u)
        nonAlone.add(v)
        scenes.append((u + 3, v + 3))
    alone = list(set(range(1, V + 1)) - nonAlone)  # E

    # alone = []
    # for i in range(1, V + 1):
    #     if i not in [u for u, v in edges] and i not in [v for u, v in edges]:
    #         alone.append(i)

    m = min(m, V)  # m cannot be greater than V

    noRoles = V + 3
    noScenes = E + 2 + len(alone)
    noActors = m + 2

    # Printing the number of roles, scenes, and actors
    print(noRoles)
    print(noScenes)
    print(noActors)

    # T1 Divas and dummys role constraints
    print(1, 1)
    print(1, 2)
    print(1, 3)

    # T1 Other role constraints
    for _ in range(V):  # V * m
        temp = []
        for j in range(1, m + 1):
            temp.append(j + 2)
        print(len(temp), *temp)

    # T2 standard constraints
    for u, v in scenes:  # E
        print(2, u, v)
    # T2 isolated constraints
    for i in range(len(alone)):  # E
        print(2, 1, alone[i] + 3)

    # T2 constraints for divas and dummies
    print(2, 1, 3)
    print(2, 2, 3)


# Variables
V = int(input())
E = int(input())
m = int(input())
edges = []

# Read edges
for line in range(E):
    line = input()
    line = line.split()
    edges.append((int(line[0]), int(line[1])))

# Example usage
# V = 5
# E = 4
# m = 3
# edges = [(1, 2), (2, 3), (3, 1), (3, 5)]

perform_reduction(V, E, m, edges)
