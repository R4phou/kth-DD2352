def transform_graph_to_casting(V, E, m, edges):
    # Initialize casting problem input
    casting_input = {"n": V, "s": E, "k": m, "roles": [], "scenes": []}

    # Initialize roles list
    for i in range(1, V + 1):
        casting_input["roles"].append([])

    # Initialize scenes list
    for i in range(E):
        casting_input["scenes"].append([])

    # Populate roles and scenes
    for edge in edges:
        v1, v2 = edge
        # Assign actors to roles
        casting_input["roles"][v1 - 1] = list(range(1, m + 1))
        casting_input["roles"][v2 - 1] = list(range(1, m + 1))
        # Assign roles to scenes
        casting_input["scenes"][edges.index(edge)].extend([v1, v2])

    return casting_input


# Example graph coloring problem input
V = 5
E = 4
m = 3
edges = [(1, 2), (1, 3), (2, 4), (3, 5)]

# Transform graph input to casting input
casting_input = transform_graph_to_casting(V, E, m, edges)

# Print casting problem input
print("Casting Problem Input:")
print("n =", casting_input["n"])
print("s =", casting_input["s"])
print("k =", casting_input["k"])
print("Roles:")
for i, role_actors in enumerate(casting_input["roles"], 1):
    print(f"{i}: {' '.join(map(str, role_actors))}")
print("Scenes:")
for i, scene_roles in enumerate(casting_input["scenes"], 1):
    print(f"{i}: {' '.join(map(str, scene_roles))}")
