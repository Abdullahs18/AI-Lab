AI LAB MID - SIMPLE CODE VERSION

Files:
1. bfs.py
2. dfs.py
3. dls.py
4. ids.py
5. ucs.py
6. bestfirst.py
7. greedybfs.py
8. astar.py
9. beam_search.py
10. hill_climbing.py
11. genetic_algorithm.py

Main memory:
BFS = Queue
DFS = Stack
DLS = DFS + Limit
IDS = DLS + Increasing limits
UCS = lowest g(n)
GBFS = lowest h(n)
A* = lowest g(n)+h(n)
Beam = keep best K
Hill Climbing = move to better neighbor
Genetic = Population -> Fitness -> Selection -> Crossover -> Mutation

All priority-search examples use simple:
queue.sort()
queue.pop(0)

No lambda or heapq is used.
