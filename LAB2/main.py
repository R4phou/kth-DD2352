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

scenes.append((1, 3))
scenes.append((2, 3))

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

print("1 1")
print("1 2")
print("1 3")

for i in range(4, n + 1):
    print(m, end=" ")
    for j in range(4, k + 1):
        print(j, end=" ")
    print()

for scene in scenes:
    print("2", *scene)
