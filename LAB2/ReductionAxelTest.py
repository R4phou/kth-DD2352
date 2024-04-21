def perform_reduction(V, E, m, edges):

    #Isolated vertices

    nonAlone = set()
    for u, v in edges:
        nonAlone.add(u)
        nonAlone.add(v)
    alone = list(set(range(1, V + 1)) - nonAlone)

    # alone = []
    # for i in range(1, V + 1):
    #     if i not in [u for u, v in edges] and i not in [v for u, v in edges]:
    #         alone.append(i)

    noRoles = V + 4
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
    print(1, 3)

    # T1 Other role constraints
    for _ in range(V):
        temp = []
        for j in range(1, m + 1):
            temp.append(j + 2)
        print(len(temp), *temp)

    # T2 standard constraints
    for u, v in edges:
        print(2, u + 4, v + 4)

    # T2 isolated constraints
    for i in range(len(alone)):
        print(2, 1, alone[i]+4)

    # T2 constraints for divas and dummies
    print(2, 1, 3)
    print(2, 2, 4)

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
