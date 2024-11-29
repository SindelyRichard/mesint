from collections import defaultdict

class Graph:
    def __init__(self,name):
        self.name = name
        self.nodes = []
        self.edges = defaultdict(list)
        self.heuristics = defaultdict(dict)
    
    def add_node(self,node):
        self.nodes.append(node)
        
    def add_edge(self,node1,node2,weight = 1):
        self.edges[node1].append((node2,weight))
        self.edges[node2].append((node1,weight))
        
    def add_heuristic(self,node,target,value):
        self.heuristics[node][target] = value
        
class ReadGraph:
    def __init__(self,text):
        self.text = text
        self.graphs = {}
        
    def build(self):
        graph = None
        heuristics = False
        
        for line in self.text.strip().splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("graph"):
                graph_name = line.split()[1]
                graph = Graph(graph_name)
                self.graphs[graph_name] = graph
            elif line.startswith("nodes"):
                nodes = line.split()[1:]
                for node in nodes:
                    graph.add_node(node)
            elif line.startswith("edges"):
                heuristics = False
            elif line.startswith("heuristic-start"):
                heuristics = True
            elif line.startswith("heuristic-end"):
                heuristics = False
            else:
                parts = line.split()
                if heuristics:
                    node = parts[0]
                    for item in parts[1:]:
                        target,value = item.split("-")
                        graph.add_heuristic(node,target,float(value))
                else:
                    node1,node2 = parts[:2]
                    if len(parts) == 3:
                        weight = int(parts[2])
                    else:
                        weight = 1
                    graph.add_edge(node1,node2,weight)
        
    