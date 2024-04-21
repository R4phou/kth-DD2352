def perform_reduction(V, E, m, edges):
    noRoles = V + 2
    noActors = m + 2
    noScenes = E + V*2
    
    # Printing the number of roles, scenes, and actors
    print(noRoles)
    print(noScenes)
    print(noActors)
    
    # Type 1 Constraints
    for i in range(V):
        print(m, end=' ')
        for j in range(1, m + 1):
            if j == m:
                print(j) 
            else:
                print(j, end=' ')
    
    # Divas role constraints
    print(1, m + 1)
    print(1, m + 2)
    
    # Type 2 Constraints
    # For each edge in the input list
    for u, v in edges:
        print(2, u, v)
    
    # Additional constraints for divas and dummies
    for i in range(1, m + 1):
        print(2, E + 1, i)
        print(2, E + 2, i)

# # Variables
# V = int(input())
# E = int(input())
# m = int(input())
# edges = []

# # Read edges
# for line in range(E):
#     line = input()
#     line = line.split()
#     edges.append((int(line[0]), int(line[1])))
# # Example usage
V = 3
E = 3
m = 3
edges = [(1, 2), (2, 3), (3, 1), (3, 4)]
perform_reduction(V, E, m, edges)
