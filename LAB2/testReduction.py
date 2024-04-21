def perform_reduction(V, E, m, edges):
    noRoles = V + 3
    noActors = m + 2
    noScenes = E + 2
    
    print(noRoles)
    print(noScenes)
    print(noActors)
    
    # Adding divas and dummy role constraints
    print("1 1")  
    print("1 2")
    print(f"1 {noActors}") 

    # Type 1 Constraints
    for i in range(V):
        print(m, " ".join(str(i) for i in range(3, m+3)))
        # print("For role", i, "actors: ", " ".join(str(i) for i in range(1, m+1)))

    print("2 1 3")
    print("2 2 3")

    # Type 2 Constraints
    for u, v in edges:
        print(f"2 {u+3} {v+3}")
    

# Example 
V = 4
E = 4
m = 3
edges = [(1, 2), (2, 3), (3, 1), (3, 4)]

# Initialize variables
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
