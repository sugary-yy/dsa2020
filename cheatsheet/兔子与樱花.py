import heapq

P=int(input())
places=[]
INF = float('inf')
dist = [[INF] * P for _ in range(P)]
next_place=[[None] * P for _ in range(P)]
for i in range(P):
    places.append(input())
    dist[i][i]=0
    next_place[i][i]=i
places_to_index={place:i for i,place in enumerate(places)}
R=int(input())
for _ in range(R):
    connections=input().split()
    a=places_to_index[connections[0]]
    b=places_to_index[connections[1]]
    dist[a][b]=int(connections[2])
    dist[b][a]=int(connections[2])
    next_place[a][b]=b
    next_place[b][a]=a
for k in range(P):
    for i in range(P):
        for j in range(P):
            if dist[i][k]+dist[k][j]<dist[i][j]:
                dist[i][j]=dist[i][k]+dist[k][j]
                next_place[i][j]=next_place[i][k]
R=int(input())
for _ in range(R):
    moves=input().split()
    a=places_to_index[moves[0]]
    b=places_to_index[moves[1]]
    path=[]
    cur_place=a
    while cur_place!=b:
        path.append(cur_place)
        cur_place=next_place[cur_place][b]
    path.append(b)
    for i in range(len(path)-1):
        a=path[i]
        b=path[i+1]
        print(f'{places[a]}->({dist[a][b]})->', end='')
    print(places[path[-1]])
