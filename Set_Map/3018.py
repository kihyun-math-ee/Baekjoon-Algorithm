import sys

N = int(sys.stdin.readline())
songs = []
L = []

for _ in range(N + 1):
    songs.append(set())

E = int(sys.stdin.readline())
song_id = 0
for _ in range(E):
    data = list(map(int, sys.stdin.readline().split()))
    target = data[1:]

    if 1 in target:
        song_id += 1
        for num in target:
            songs[num].add(song_id)
    else:
        U = set()
        for num in target:
            U.update(songs[num])

        for num in target:
            songs[num].update(U)

for k in range(len(songs)):
    if len(songs[k]) == song_id:
        L.append(k)

for m in range(len(L)):
    print(L[m])