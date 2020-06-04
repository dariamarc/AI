def findEdge(x, y, edges):
    for edge in edges:
        if edge.source == x and edge.dest == y or edge.source == y and edge.dest == x:
            return edge
    return None