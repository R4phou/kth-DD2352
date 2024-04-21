def perform_reduction(V, E, m, edges):
    noRoles = V + 4
    noActors = m + 2
    noScenes = E + 2
    
    # Printing the number of roles, scenes, and actors
    print(noRoles)
    print(noScenes)
    print(noActors)
    
    # Divas role constraints
    print(1, 1)
    print(1, 2)

    # Dummy role constraints
    print(1, noActors - 1)
    print(1, noActors)

    # Type 1 Constraints
    for i in range(2, m + 2):
        print(m, end=' ')
        for j in range(1, m + 1):
            if j == m:
                print(j+2) 
            else:
                print(j+2, end=' ')
        
    # Type 2 Constraints
    # For each edge in the input list
    for u, v in edges:
        print(2, u+2, v+2)
    
    # Additional constraints for divas and dummies
    print(2, 1, 3)
    print(2, 2, 4)
    # for i in range(1, m + 1):
    #     print(2, E + 1, i)
    #     print(2, E + 2, i)

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
edges = [(1, 2), (2, 3), (3, 1)]
perform_reduction(V, E, m, edges)
