from collections import deque

def have_cycle_in_graph(graph):
    visited_vertexes = set()
    for vertex in graph:
        if vertex not in visited_vertexes:
            if bfs(graph, vertex, visited_vertexes, parent=None):
                return True

    return False

def bfs(graph, vertex, visited_vertexes, parent):
    queue = deque([(vertex, None)])
    while queue:
        vertex, parent = queue.popleft()
        if vertex in visited_vertexes:
            return True
        visisted_vertexes.add(vertex)
        for neighbor in graph[vertex]:
            if parent != neighbor:
                queue.append((neighbor, vertex

    return False

def read_graph_from_inputfile(file_name):
    graph = {}
    with open(file_name, 'r') as file:
        for line in file:
            vertexes = line.strip().split()
            vertex = int(vertexes[0])
            neighbors = [int(vert) for vert in vertexes[1:]]
            graph[vertex] = neighbors
        file.close()
    return graph

def write_result_to_outputfile(file_name, have_cycle):
    with open(file_name, "w") as file:
        file.write(str(have_cycle))

if __name__ == "__main":
    graph = read_graph_from_inputfile_("input.txt")
    is_cycle = have_cycle(graph)
    write_result_to_outputfile("output.txt", is_cycle)
