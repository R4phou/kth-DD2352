V = int(input())
E = int(input())
m = int(input())

m = min(m, V)  # m cannot be greater than V

# Base cases
n = 3
s = 2 + E
k = 3 + m  # 2 divas, a dummy

scenes = []
seenRoles = {}

# Constraint 2 for the scene with divas and dummy
scenes.append((1, 3))
scenes.append((2, 3))

# Constraint 2 for the rest of the graph
for _ in range(E):
    u, v = map(int, input().split())
    if u not in seenRoles:
        n += 1
        seenRoles[u] = n
    if v not in seenRoles:
        n += 1
        seenRoles[v] = n
    scenes.append((seenRoles[u], seenRoles[v]))

print(n)
print(s)
print(k)

# Constraint 1 for the divas and dummy
print("1 1")
print("1 2")
print("1 3")

# Print constraint 1 for the rest of the roles
for i in range(4, n + 1):
    print(m, end=" ")
    for j in range(4, k + 1):
        print(j, end=" ")
    print()

# Print constraint 2 for the scenes
for scene in scenes:
    print("2", *scene)
