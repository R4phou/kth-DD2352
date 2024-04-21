def perform_reduction(V, E, m, edges):
    noRoles = V + 2
    noActors = m + 2
    noScenes = E + V*2
    
    print(noRoles)
    print(noScenes)
    print(noActors)
    
    # # Adding divas and dummy role constraints
    # print("1 1")  
    # print("1 2")
    # print(f"1 {noActors}") 

    # Type 1 Constraints
    for i in range(V):
        print(m, " ".join(str(i) for i in range(1, m + 1)))
        # print("For role", i, "actors: ", " ".join(str(i) for i in range(1, m+1)))

    print(f"1 {m+1}")
    print(f"1 {m+2}")

    # Type 2 Constraints
    for u, v in edges:
        print(f"2 {u} {v}")
    
    for i in range(1, m + 1):
        print(f"2 {E+1} {i}")
        print(f"2 {E+2} {i}")
# Example 
# V = 3
# E = 3
# m = 3
# edges = [(1, 2), (2, 3), (3, 1)]

# # Initialize variables
V = int(input())
E = int(input())
m = int(input())
edges = []

# Read edges
for line in range(E):
    line = input()
    line = line.split()
    edges.append((int(line[0]), int(line[1])))
# print("Solution:")

perform_reduction(V, E, m, edges)
