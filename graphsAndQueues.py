def kFrequent(nums, k):
    # Frequency dictionary
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    # Sort them by frequency, then number
    sorted_things = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    # Grab the top k in dicitionary
    top_k = [num for num, _ in sorted_things[:k]]
    return top_k

def allPaths(edges, source, destination):
    # Creating a graph map
    graph = {}
    for s, e in edges:
        graph.setdefault(s, []).append(e)
    
    # Creating a dfs function to find paths
    def dfs(node, path):
        if node == destination:
            paths.append(path.copy())
            return
        for next in graph.get(node, []):
            dfs(next, path + [next])
    
    paths = []  # Stores paths
    dfs(source, [source])  # Dfs is created
    return paths