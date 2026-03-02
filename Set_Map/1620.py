import sys

N, M = map(int, sys.stdin.readline().split())
pokemon_dict = {}

for i in range(1, N + 1):
    pokemon_name = sys.stdin.readline().strip()
    pokemon_dict[pokemon_name] = str(i)
    pokemon_dict[str(i)] = pokemon_name 

for _ in range(M):
    problem = sys.stdin.readline().strip()
    print(pokemon_dict[problem])