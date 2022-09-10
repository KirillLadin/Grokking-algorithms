def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


if __name__ == '__main__':
    g = {}
    g['start'] = {}
    g['start']['a'] = 6
    g['start']['b'] = 2
    g['a'] = {}
    g['a']['end'] = 1
    g['b'] = {}
    g['b']['a'] = 3
    g['b']['end'] = 5
    g['end'] = {}
    infinity = float('inf')
    costs = {'a': 6, 'b': 2, 'end': infinity}
    parents = {'a': 'start', 'b': 'start', 'end': None}
    processed = []
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = g[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)

    v = 'end'
    path = [v]
    path_length = costs['end']
    while v != 'start':
        v = parents[v]
        path.append(v)
    path.reverse()
    print(path_length)
    print(path)







