from typing import List, Dict


def dfs(graph: Dict[str, List[str]], start_point: str, visited: List[str]):
    if visited is None:
        visited = []
    if start_point not in visited:
        visited.append(start_point)
        for neighbor in graph[start_point]:
            dfs(graph, neighbor, visited)

def build_graph(cities: List[str], storages: List[str], gas_lines: List[List[str]]):
    graph = {}
    for city in cities + storages:
        graph[city] = []
    for source, destination in gas_lines:
        if source in graph and destination in graph:
            graph[source].append(destination)
            graph[destination].append(source)
    return graph

def find_unreachable_storage(cities: List[str], storages: List[str], gas_lines: List[List[str]]) -> List[str]:
    graph = build_graph(cities, storages, gas_lines)
    visited = []
    dfs(graph, storages[0], visited)
    reachable_storages = set()
    for city in visited:
        for storage in storages:
            if storage in graph[city]:
                reachable_storages.add(storage)
    unreachable_storage = [storage for storage in storages if storage not in reachable_storages]
    return unreachable_storage
