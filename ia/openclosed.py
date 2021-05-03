from queue import PriorityQueue

h = {
    'a': 0,
    'b': 8,
    'c': 3,
    'd': 5,
    'e': 9,
    'f': 0,
    'g': 5,
}

graph = {}
with open("input", "r") as f:
    for line in f:
        a, b, cost = line.split()
        if a not in graph: graph[a] = []
        graph[a].append((int(cost), b))


prev = {'a': None}
dist = {'a': 0, 'b': 1000, 'c': 1000, 'd': 1000, \
        'e': 1000, 'f': 1000, 'g': 1000}

openL = PriorityQueue()
openL.put((0, 'a'))

closedL = set()
target = 'f'

it = 0

while not openL.empty():

    it += 1
    print(it)
    print('open')
    for cost, n in openL.queue:
        print(n, dist[n], cost, prev[n])
    print('closed')
    for n in closedL:
        print(n, dist[n], dist[n] + h[n], prev[n])
    print()

    d, node = openL.get()

    if target == node:
        li = []
        while node:
            li.append(node)
            node = prev.get(node)
        print(li[::-1])
        break

    closedL.add(node)

    for l, child in graph[node]:
        if child in closedL:
            continue

        g = dist[node] + l
        f = g + h[child]

        openQ = {n for _, n in openL.queue}
        if child in openQ and g >= dist[child]:
            continue

        dist[child] = g
        prev[child] = node
        openL.put((f, child))


print(prev)
