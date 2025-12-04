from dijkstra import dijkstra, reconstruct_path
from task_1 import G, cities

print("\n--- Найкоротші шляхи ---")

for city in cities:
    dists, prevs = dijkstra(G, city)
    
    print(f"\nВід міста {city}:")
    
    for target_city in cities:
        if city != target_city:
            distance = dists[target_city]
            path = reconstruct_path(prevs, city, target_city)
            print(f" -> до міста {target_city}: шлях {path}, довжина {distance}")
