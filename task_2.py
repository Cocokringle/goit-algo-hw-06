import networkx as nx

from bfs_path import  bfs_paths
from dfs_path import  dfs_paths
from task_1 import G

start_city = "Івано-Франківськ"
end_city = "Харків"

dfs_result = list(dfs_paths(G, start_city, end_city))
bfs_result = list(bfs_paths(G, start_city, end_city))

# print(f"Шляхи від {start_city} до {end_city}:")
# print("\nDFS (Глибина):", dfs_result[0])
# print("BFS (Ширина):", bfs_result[0])