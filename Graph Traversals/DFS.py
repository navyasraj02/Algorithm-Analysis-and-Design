time = -1

def DFSVisit(n):
    global time
    time += 1
    d[n] = time
    color[n] = "G"
    for u in adj[n]:
        if color[u] == "W":
            DFSVisit(u)
    time += 1
    color[n] = "B"
    f[n] = time


n = 6
e = [(0, 1), (1, 2), (2, 3), (0, 3), (3, 1), (4, 3), (4, 5)]
adj = [[] for _ in range(n+1)]

for u, v in e:
    # for directed graph,an edge from u to v means v adjacent to u
    adj[u].append(v)

for i in range(n):
    print("Adjacent vertices for vertex", i, "is", adj[i])

color = ["W"]*n
pi = [-1]*n
f = [-1]*n
d = [-1]*n


for i in range(0, 5):
    if color[i] == "W":
        DFSVisit(i)

print("Color array :", color)
print("Discovery array :", d)
print("Finish array :", f)
