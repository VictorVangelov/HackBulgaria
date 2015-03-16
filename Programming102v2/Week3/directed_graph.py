class DirectedGraph():

    def __init__(self):
        self.dict_of_all_nodes = {}

    def dfs(self, graph, start):
        visited, stack = set(), [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(graph[vertex] - visited)
        return visited

    def add_edge(self, node_a, node_b):
        if node_a in self.dict_of_all_nodes:
            if node_b in self.dict_of_all_nodes:
                self.dict_of_all_nodes[node_a].add(node_b)
            else:
                self.dict_of_all_nodes[node_b] = set()
        else:
            self.dict_of_all_nodes[node_a] = set()
            return self.add_edge(node_a, node_b)

    def get_neighbors_for(self, node):
        content = ""
        for neighbors in self.dict_of_all_nodes[node]:
            content += neighbors + "\n"
        if len(content) > 0:
            print (content)
        else:
            print("there is no neighbors")

    def path_between(self, node_a, node_b):
        if node_b in self.dfs(self.dict_of_all_nodes, node_a):
            return True
        else:
            return False

if __name__ == '__main__':
    graph = DirectedGraph()
