def perform_reduction(V, E, m, edges):
    noRoles = V + 2
    noActors = m + 2
    noScenes = E + V * 2

    print(noRoles)
    print(noScenes)
    print(noActors)

    constraint_1 = []
    for i in range(V):
        constraint_1.append([i for i in range(1, m + 1)])

    constraint_1.append([m + 1])
    constraint_1.append([m + 2])

    constraint_2 = []
    for u, v in edges:
        constraint_2.append([u, v])

    for i in range(1, m + 1):
        constraint_2.append([E + 1, i])
        constraint_2.append([E + 2, i])

    for actors in constraint_1:
        print(len(actors), *actors)
    for roles in constraint_2:
        print(len(roles), *roles)


# Example
# V = 3
# E = 3
# m = 3
# edges = [(1, 2), (2, 3), (3, 1)]

# # # Initialize variables
# V = int(input())
# E = int(input())
# m = int(input())
# edges = []

# # Read edges
# for line in range(E):
#     line = input()
#     line = line.split()
#     edges.append((int(line[0]), int(line[1])))
# print("Solution:")

perform_reduction(V, E, m, edges)
