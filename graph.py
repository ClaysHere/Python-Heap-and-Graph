def bfs(graph, node):
    visited = []
    queue = []
    visited.append(node)
    queue.append(node)

    while(queue):
        m = queue.pop(0)
        print(m, end=' ')
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

def dfs(visited, graph, node): 
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def menu():
    print('Graph Traversal')
    print('================================')
    print('1. BFS')
    print('2. DFS')
    print('3. Keluar')
    pil = int(input('Masukkan kode (1-3) = '))
    return pil

def insert():
    print('Input Data')
    print('=================================')
    n = int(input('Jumlah vertex = '))
    g = {}
    val = []

    for i in range(n):
        v = input('Vertex = ').upper()
        ad = int(input(f'Jumlah adjacency dari {v} = '))
        for i in range(ad):
            temp = input(f'Adjacency dari vertex {v} ke-{i+1} = ').upper()
            val.append(temp)
        val.sort()
        g[v] = val
        val = []
    g = dict(sorted(g.items()))
    return g


graph = insert()
ulang = 1

print('Graph =',graph)
print()

while (ulang != 3):
    ulang = menu()
    if(ulang == 1):
        start = input('Traversal BFS mulai dari vertex = ').upper()
        print('BFS Traversal = ',end='')
        bfs(graph, start)
        print()
    elif(ulang == 2):
        start = input('Traversal DFS mulai dari vertex = ').upper()
        print('DFS Traversal = ',end='')
        visited = set()
        dfs(visited,graph, start)
        print()
    elif(ulang > 3 or ulang < 1):
        print('Kode yang anda masukkan salah')
    print('')

print('Terima kasih telah menggunakan program ini.')
