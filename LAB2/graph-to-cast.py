"""
- The divas are the first 2 actors
- The dummy is the last actor
- The divas cannot play in the same scene    
The idea is to transform a graph coloring problem input to a casting problem input
To do this, we split the graph in 2 subgraphs
    - The first subgraph has 3 nodes: the dummy and the 2 divas
    - The rest of the graph is a regular coloring problem
        - Each vertex is a role
        - Each edge is a scene
        - Each color is an actor

We have 3 colors reserved to color the first subgraph
And the rest of the colors are used to color the rest of the graph

That way, if we can solve the casting problem, we can solve the coloring problem as the transformation just added this dummy graph off to the side


Graph coloring problem input:
V
E
m
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
"""

# Initialize variables
V = int(input())
E = int(input())
m = int(input())
edges = []

# Read edges
for line in range(E):
    line = line.split()
    edges.append((int(line[0]), int(line[1])))


# Adding the dummy graph in order to solve the casting problem
n = V + 3  # Number of roles
s = E + 3  # Number of scenes
k = m + 1  # Number of actors


constraint_1 = []  # index = role, value = actors that can play that role
constraint_2 = []  # index = scene, value = roles that need to be played in that scene


all_actors = [i for i in range(k)]

for i in range(3):
    constraint_1.append([i])  # The divas and the dummy can only play their own role

constraint_2.append([0, 1])  # The first scene needs the divas
constraint_2.append([0, 2])  # The second scene needs the divas and the dummy
constraint_2.append([1, 2])  # The third scene needs the divas and the dummy

for i in range(3, n):
    constraint_1.append(all_actors)  # The rest of the roles can be played by any actor


# fill the constraint_2 with the scenes-roles (edges)
for edge in edges:
    role1, role2 = edge
    constraint_2.append([role1, role2])  # Each scene needs the roles in the edge


# Print the casting problem
print(n)
print(s)
print(k)
for actors in constraint_1:
    print(len(actors), *actors)
for roles in constraint_2:
    print(len(roles), *roles)
