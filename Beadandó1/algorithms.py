class Algorithms:
    def __init__(self,graph):
        self.graph = graph
      
    def bfs(self,start,goal):
        expansion_count = 0
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            end_node = path[-1]
            if end_node == goal:
                print(f"{self.graph.name} expansions (bfs): {expansion_count}")
                return path
            for adjacent,weight in self.graph.edges[end_node]:
                if adjacent not in path:
                    new_path = list(path) + [adjacent]
                    queue.append(new_path)
                    expansion_count+=1
        return None
    
    def dfs(self,start, goal):
        expansion_count = 0
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            end_node = path[-1]
            if end_node == goal:
                print(f"{self.graph.name} expansions (dfs): {expansion_count}")
                return path
            for adjacent,weight in sorted(self.graph.edges[end_node],reverse=True):
                if adjacent not in path:
                    new_path = list(path) + [adjacent]
                    queue.insert(0, new_path)
                    expansion_count+=1
        return None
    
    def hc(self,start, goal):
        expansion_count = 0
        queue = []
        initial_cost = self.graph.heuristics[goal][start]
        queue.append((initial_cost,[start]))
        while queue:
            path_cost,path = queue.pop(0)
            end_node = path[-1]
            if end_node == goal:
                print(f"{self.graph.name} expansions (hc): {expansion_count}")
                return path
            min_costs = []
            for adjacent, weight in self.graph.edges[end_node]:
                if adjacent not in path:
                   temp_cost=path_cost+float(self.graph.heuristics[goal][adjacent])
                   min_costs.append((temp_cost, adjacent))
                   expansion_count+=1
            min_costs = sorted(min_costs, key=lambda x: x[0])
            min = min_costs[0]
            new_path = list(path) + [min[1]]
            queue.insert(0,(min[0],new_path))
        return None
    
    def beam(self,start,goal,beam_width):
        queue = []
        expansion_count = 0
        initial_cost = self.graph.heuristics[goal][start]
        queue.append((initial_cost,[start]))
        while queue:
            path_cost,path = queue.pop(0)
            end_node = path[-1]
            if end_node == goal:
                print(f"{self.graph.name} expansions (beam): {expansion_count}")
                return path
            for adjacent,weight in self.graph.edges[end_node]:
                if adjacent not in path:
                    temp_cost=path_cost+float(self.graph.heuristics[goal][adjacent])
                    new_path = list(path) + [adjacent]
                    queue.append((temp_cost,new_path))
                    expansion_count+=1
            queue = sorted(queue, key=lambda x: x[0])[:beam_width]
        return None
    
    def branch(self,start,goal):
        queue = []
        expansion_count = 0
        initial_cost = 0
        queue.append((initial_cost,[start]))
        while queue:
            path_cost,path = queue.pop(0)
            end_node = path[-1]
            if end_node == goal:
                print(f"{self.graph.name} expansions (b&b): {expansion_count}")
                return path
            for adjacent,weight in self.graph.edges[end_node]:
                if adjacent not in path:
                  temp_cost=path_cost+weight
                  new_path = list(path) + [adjacent]
                  queue.append((temp_cost,new_path))
                  expansion_count+=1
            queue = sorted(queue, key=lambda x: x[0])
        return None
    
    def branch_list(self,start,goal):
        visited = []
        queue = []
        expansion_count = 0
        initial_cost = 0
        queue.append((initial_cost,[start]))
        while queue:
            path_cost,path = queue.pop(0)
            end_node = path[-1]
            if end_node == goal:
                print(f"{self.graph.name} expansions (b&b w. list): {expansion_count}")
                return path
            for adjacent,weight in self.graph.edges[end_node]:
                if adjacent not in visited:
                    visited.append(adjacent)
                    temp_cost=path_cost+weight
                    new_path = list(path) + [adjacent]
                    queue.append((temp_cost,new_path))
                    expansion_count+=1
            queue = sorted(queue, key=lambda x: x[0])
        return None
    
    def branch_heur(self,start,goal):
        queue = []
        expansion_count = 0
        initial_cost = 0
        queue.append((initial_cost,initial_cost,[start]))
        while queue:
            _,path_cost,path = queue.pop(0)
            end_node = path[-1]
            if end_node == goal:
                print(f"{self.graph.name} expansions (b&b w. heursitic): {expansion_count}")
                return path
            for adjacent,weight in self.graph.edges[end_node]:
                if adjacent not in path:
                 actual_cost = path_cost+weight
                 temp_cost=self.graph.heuristics[goal][adjacent]+actual_cost
                 new_path = list(path) + [adjacent]
                 queue.append((temp_cost,actual_cost,new_path))
                 expansion_count+=1
            queue = sorted(queue, key=lambda x: x[0])
        return None
    
    def a(self,start,goal):
        visited = []
        queue = []
        expansion_count = 0
        initial_cost = 0
        queue.append((initial_cost,initial_cost,[start]))
        while queue:
            _,path_cost,path = queue.pop(0)
            end_node = path[-1]
            if end_node == goal:
                print(f"{self.graph.name} expansions (A*): {expansion_count}")
                return path
            for adjacent,weight in self.graph.edges[end_node]:
                if adjacent not in visited:
                   visited.append(adjacent)
                   actual_cost = path_cost+weight
                   temp_cost=self.graph.heuristics[goal][adjacent]+actual_cost
                   new_path = list(path) + [adjacent]
                   queue.append((temp_cost,actual_cost,new_path))
                   expansion_count+=1
            queue = sorted(queue, key=lambda x: x[0])
        return None