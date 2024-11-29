from graph import ReadGraph
from algorithms import Algorithms
import time

def main():
    with open("graphs.txt","r") as file:
        text = file.read()
            
        reader = ReadGraph(text)
        reader.build()

        g0 = reader.graphs.get("GRAPH_0")
        
        g1 = reader.graphs.get("GRAPH_1")
        
        g2 = reader.graphs.get("GRAPH_2")
        
        g3 = reader.graphs.get("GRAPH_3")
        
        graph0 = Algorithms(g0)
        graph1 = Algorithms(g1)
        graph2 = Algorithms(g2)
        graph3 = Algorithms(g3)

        print("BFS:")
        
        begin = time.perf_counter()
        print(f"GRAPH_1 (bfs) path:{graph1.bfs('a','d')}")
        end = time.perf_counter()
        runtime = end - begin
        print(f"Runtime GRAPH_1 (bfs):{runtime:.6f} sec")
        
        begin = time.perf_counter()
        print(f"GRAPH_2 (bfs) path:{graph2.bfs('S', 'G')}")
        end = time.perf_counter()
        runtime = end - begin
        print(f"Runtime GRAPH_2 (bfs):{runtime:.6f} sec")

        begin = time.perf_counter()
        print(f"GRAPH_3 (bfs) path:{graph3.bfs('s','g')}")
        end = time.perf_counter()
        runtime = end - begin
        print(f"Runtime GRAPH_3 (bfs):{runtime:.6f} sec")
        
        print("DFS:")
        
        begin = time.perf_counter()
        print(f"GRAPH_1 (dfs) path:{graph1.dfs('a','d')}")
        end = time.perf_counter()
        runtime = end - begin
        print(f"Runtime GRAPH_1 (dfs):{runtime:.6f} sec")
        
        begin = time.perf_counter()
        print(f"GRAPH_2 (dfs) path:{graph2.dfs('S','G')}")
        end = time.perf_counter()
        runtime = end - begin
        print(f"Runtime GRAPH_2 (dfs):{runtime:.6f} sec")

        begin = time.perf_counter()
        print(f"GRAPH_3 (dfs) path:{graph3.dfs('s','g')}")
        end = time.perf_counter()
        runtime = end - begin
        print(f"Runtime GRAPH_3 (dfs):{runtime:.6f} sec")
        
        print("HC:")

        begin = time.perf_counter()
        print(f"GRAPH_1 (hc) path:{graph1.hc('a','d')}")
        end = time.perf_counter()
        runtime = end - begin
        print(f"Runtime GRAPH_1 (hc):{runtime:.6f} sec")

        begin = time.perf_counter()
        print(f"GRAPH_2 (hc) path:{graph2.hc('S','G')}")
        end = time.perf_counter()
        runtime = end - begin
        print(f"Runtime GRAPH_2 (hc):{runtime:.6f} sec")

        begin = time.perf_counter()
        print(f"GRAPH_3 (hc) path:{graph3.hc('s','g')}")
        end = time.perf_counter()
        runtime = end - begin
        print(f"Runtime GRAPH_3 (hc):{runtime:.6f} sec")

        print("Beam:")

        begin = time.perf_counter()
        print(f"GRAPH_1 (beam) path:{graph1.beam('a','d',2)}")
        end = time.perf_counter()
        runtime = end - begin
        print(f"Runtime GRAPH_1 (beam):{runtime:.6f} sec")

        begin = time.perf_counter()
        print(f"GRAPH_2 (beam) path:{graph2.beam('S','G',2)}")
        end = time.perf_counter()
        runtime = end - begin
        print(f"Runtime GRAPH_2 (beam):{runtime:.6f} sec")

        begin = time.perf_counter()
        print(f"GRAPH_3 (beam) path:{graph3.beam('s','g',2)}")
        end = time.perf_counter()
        runtime = end - begin
        print(f"Runtime GRAPH_3 (beam):{runtime:.6f} sec")
        
        print("Branch and Bound")
        
        begin = time.perf_counter()
        print(f"GRAPH_1 (b&b) path:{graph1.branch('a','d')}")
        end = time.perf_counter()
        runtime = end - begin
        print(f"Runtime GRAPH_1 (b&b):{runtime:.6f} sec")
        
        begin = time.perf_counter()
        print(f"GRAPH_2 (b&b) path:{graph2.branch('S','G')}")
        end = time.perf_counter()
        runtime = end - begin
        print(f"Runtime GRAPH_2 (b&b):{runtime:.6f} sec")

        begin = time.perf_counter()
        print(f"GRAPH_3 (b&b) path:{graph3.branch('s','g')}")
        end = time.perf_counter()
        runtime = end - begin
        print(f"Runtime GRAPH_3 (b&b):{runtime:.6f} sec")

        print("Branch and Bound w. List")
        
        begin = time.perf_counter()
        print(f"GRAPH_1 (b&b w. list) path:{graph1.branch_list('a','d')}")
        end = time.perf_counter()
        runtime = end - begin
        print(f"Runtime GRAPH_1 (b&b w. list):{runtime:.6f} sec")
        
        begin = time.perf_counter()
        print(f"GRAPH_2 (b&b w. list) path:{graph2.branch_list('S','G')}")
        end = time.perf_counter()
        runtime = end - begin
        print(f"Runtime GRAPH_2 (b&b w. list):{runtime:.6f} sec")

        begin = time.perf_counter()
        print(f"GRAPH_3 (b&b w. list) path:{graph3.branch_list('s','g')}")
        end = time.perf_counter()
        runtime = end - begin
        print(f"Runtime GRAPH_3 (b&b w. list):{runtime:.6f} sec")

        print("Branch and Bound w. Heuristic")
        
        begin = time.perf_counter()
        print(f"GRAPH_1 (b&b w. heuristic) path:{graph1.branch_heur('a','d')}")
        end = time.perf_counter()
        runtime = end - begin
        print(f"Runtime GRAPH_1 (b&b w. heuristic):{runtime:.6f} sec")
        
        begin = time.perf_counter()
        print(f"GRAPH_2 (b&b w. heuristic) path:{graph2.branch_heur('S','G')}")
        end = time.perf_counter()
        runtime = end - begin
        print(f"Runtime GRAPH_2 (b&b w. heuristic):{runtime:.6f} sec")

        begin = time.perf_counter()
        print(f"GRAPH_3 (b&b w. heuristic) path:{graph3.branch_heur('s','g')}")
        end = time.perf_counter()
        runtime = end - begin
        print(f"Runtime GRAPH_3 (b&b w. heuristic):{runtime:.6f} sec")

        print("A*")
        
        begin = time.perf_counter()
        print(f"GRAPH_1 (A*) path:{graph1.a('a','d')}")
        end = time.perf_counter()
        runtime = end - begin
        print(f"Runtime GRAPH_1 (A*):{runtime:.6f} sec")
        
        begin = time.perf_counter()
        print(f"GRAPH_2 (A*) path:{graph2.a('S','G')}")
        end = time.perf_counter()
        runtime = end - begin
        print(f"Runtime GRAPH_2 (A*):{runtime:.6f} sec")

        begin = time.perf_counter()
        print(f"GRAPH_3 (A*) path:{graph3.a('s','g')}")
        end = time.perf_counter()
        runtime = end - begin
        print(f"Runtime GRAPH_3 (A*):{runtime:.6f} sec")

main()
    