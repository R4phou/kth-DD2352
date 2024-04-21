"""
Transform a graph coloring problem input to a casting problem input
Graph coloring problem input:
V # number of vertices
E # number of edges
m # maximum number of colors needed to color the graph
# list of edges (u, v) where u and v are vertices in the graph
e1
e2
...
e_E

Cast problem input:
n # number of roles
s # number of scenes
k # number of actors
n lines with: length of the line = number of actors that can play that role, and the values are the actors that can play that role
s lines with: length of the line = number of roles that need to be played in that scene, and the values are the roles that need to be played in that scene

Rules of the casting problem:
- Each role can be played by at most one actor
- Actor 1 and 2 cannot play in the same scene and are guaranteed to play in at least one scene
- Each scene must have at least two actors
"""

V = int(input())
E = int(input())
m = int(input())
edges = []
for i in range(E):
    line = input().split()
    edges.append((int(line[0]), int(line[1])))


def col_to_graph(V, E, m, edges):
    n = V - m
    s = E
    k = m
    all_actors = [i for i in range(1, k + 1)]
    roles = [all_actors for _ in range(n)]  # list of actors that can play that role
    scenes = [
        [] for _ in range(s)
    ]  # list of roles that need to be played in that scene

    # Create scenes with edges, a cycle is a scene and all the vertices in the cycle are the roles of that scene
    for i, edge in enumerate(edges):
        scenes[i].extend(edge)

    return n, s, k, roles, scenes


n, s, k, roles, scenes = col_to_graph(V, E, m, edges)

print(n)
print(s)
print(k)
for role in roles:
    print(len(role), *role)
for scene in scenes:
    print(len(scene), *scene)
