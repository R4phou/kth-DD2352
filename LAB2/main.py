def transform_graph_to_casting(V, E, m, edges):
    # Initialize casting problem input
    casting_input = {"n": V, "s": E, "k": m, "roles": [], "scenes": []}

    # Initialize roles list
    for i in range(1, V + 1):
        casting_input["roles"].append([])

    # Populate roles
    for i in range(1, V + 1):
        casting_input["roles"][i - 1] = [i]  # Role i can be played by actor i

    # Populate scenes
    for edge in edges:
        v1, v2 = edge
        casting_input["scenes"].append([v1, v2])

    return casting_input


V = int(input())
E = int(input())
m = int(input())
edges = []
for i in range(E):
    line = input().split()
    edges.append((int(line[0]), int(line[1])))

casting_input = transform_graph_to_casting(V, E, m, edges)


# Output:
# Casting Problem Input:
print(casting_input["n"])
print(casting_input["s"])
print(casting_input["k"])
for role_actors in casting_input["roles"]:
    print(len(role_actors), *role_actors)
for scene_roles in casting_input["scenes"]:
    print(len(scene_roles), *scene_roles)
