n = 6
graph = [[1, 3], [0, 2, 3], [1, 3, 4], [0, 1, 2], [2, 5], [4]]

q = [-1]*n
f = -1
r = -1


# Function to add elements to the queue
def enqueue(q, s):
    global f, r

    if f == -1:
        f = 0
    r += 1
    q[r] = s

# Function to remove elements from queue
def dequeue(q):
    global f, r
    x = q[f]

    if f == r:
        f = -1
        r = -1
    else:
        f += 1
    return x

# Function to check if queue is empty or not
def qNotEmpty(count):
    if(count != n):
        return True
    else:
        return False

# BFS Algorithm
def bfs(graph, s):
    count = 0
    d[s] = 0
    color[s] = "G"
    enqueue(q, s)
    while(qNotEmpty(count)):
        v = dequeue(q)
        print("v:", v)
        for u in graph[v]:
            if color[u] == "W":
                enqueue(q, u)
                pi[u] = v
                color[u] = "G"
                d[u] = d[v]+1
        count += 1
        color[v] = "B"


# Initialize variables and arrays
d = [-1]*n
pi = ["None"]*n
color = ["W"]*n
for i in range(n):
    print("Adjacent vertices for vertex", i, "is", graph[i])

# Run BFS Algorithm
bfs(graph, 0)
print("Color array :", color)
print("Distance array :", d)
print("Pi array :", pi)
