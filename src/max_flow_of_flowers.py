import csv
from collections import defaultdict
from typing import List, Dict


def dfs(graph: Dict[str, List[str]], start_point: str, visited: List[str]):
    if visited is None:
        visited = []
    if start_point not in visited:
        visited.append(start_point)
        for neighbor in graph[start_point]:
            dfs(graph, neighbor, visited)
def dfs(graph: Dict[str, List[str]], node: str, sink: str, visited: List[str], parent: str):
    """
    Deep Path Search (DFS) function.
    :param graph: The graph is presented in the form of a dictionary.
    :param node: The current node.
    :param sink: Drain node.
    :param visited: The number of nodes visited.
    :param parent: A dictionary containing the pair "son:father".
    :return: Returns True if the path to the drain is found, False otherwise.
    """
    if node == sink:
        return True

    visited.add(node)

    for neighbor, capacity in graph[node].items():
        if neighbor not in visited and capacity > 0:
            parent[neighbor] = node
            if dfs(graph, neighbor, sink, visited, parent):
                return True

    return False


def ford_fulkerson(graph, source, sink):
    """
    A function for finding the maximum flow in a graph according to the Ford-Falkerson algorithm.
    :param graph: The graph is presented in the form of a dictionary.
    :param source: Source node
    :param sink: Drain node
    :return: The maximum flow in the graph.
    """
    max_flow = 0
    while True:
        visited = set()
        parent = {}
        if not dfs(graph, source, sink, visited, parent):
            break

        path_flow = float('inf')
        current_node = sink    # почитаєм обхід з стоку
        while current_node != source:
            parent_node = parent[current_node]
            path_flow = min(path_flow, graph[parent_node][current_node])
            current_node = parent_node

        current_node = sink
        while current_node != source:
            parent_node = parent[current_node]
            graph[parent_node][current_node] -= path_flow
            if parent_node not in graph[current_node]:
                graph[current_node][parent_node] = 0
            graph[current_node][parent_node] += path_flow
            current_node = parent_node

        max_flow += path_flow

    return max_flow


def max_flow(filename):
    """
    A function for finding the maximum flow in a graph according to the Ford-Falkerson algorithm.
    :param filename: The path to the graph file.
    :return: The maximum flow in the graph.
    """
    graph, farms, shops = read_graph_from_inputfile(filename)

    source = 'Source'
    sink = 'Sink'

    for farm in farms:
        graph[source][farm] = float('inf')
    for shop in shops:
        if sink not in graph:
            graph[sink] = defaultdict(dict)
        graph[shop][sink] = float('inf')

    max_flow_value = ford_fulkerson(graph, source, sink)
    return max_flow_value

def read_graph_from_inputfile(filename):
    """
    Function for reading a graph from an input file.
    :param filename:The path to the graph file.
    :return: A tuple containing a graph as a dictionary, a list of farms, and a list of shops.
    """
    graph = defaultdict(dict)
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        farms = next(reader)
        shops = next(reader)
        for line in reader:
            node1, node2, capacity = line
            graph[node1][node2] = int(capacity)

    return graph, farms, shops
