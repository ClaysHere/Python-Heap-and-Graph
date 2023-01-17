def max_heapify(A, k):
    l = 2 * k + 1
    r = 2 * k + 2

    if l < len(A) and A[l] > A[k]:
        largest = l
    else:
        largest = k
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != k:
        A[k], A[largest] = A[largest], A[k]
        max_heapify(A, largest)

def max_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        max_heapify(A, k)

def min_heapify(A, k):
    l = 2 * k + 1
    r = 2 * k + 2

    if l < len(A) and A[l] < A[k]:
        smallest = l
    else:
        smallest = k
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    if smallest != k:
        A[k], A[smallest] = A[smallest], A[k]
        min_heapify(A, smallest)

def min_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        min_heapify(A, k)

def deleteMax(arr,data):
    size = len(arr)
    i = 0
    
    for i in range(0, size):
        if data == arr[i]:
            break
    arr[i], arr[size-1] = arr[size-1], arr[i]
    arr.remove(data)

    for i in range((len(arr)//2)-1,-1,-1):
        max_heapify(arr,i)

def deleteMin(arr,data):
    size = len(arr)
    i = 0
    
    for i in range(0, size):
        if data == arr[i]:
            break
    arr[i], arr[size-1] = arr[size-1], arr[i]
    arr.remove(data)

    for i in range((len(arr)//2)-1,-1,-1):
        min_heapify(arr,i)

def insert_max(arr):
    print('Masukkan data ke dalam heap')
    print('='*40)
    n = int(input('Jumlah data = '))
    for i in range(n):
        temp = int(input(f'Input data ke-{i+1} = '))
        arr.append(temp)
        arr.sort()
    max_heap(arr)
    print(f'Heap = {arr}')
    print()
    fiturMax(arr)

def fiturMax(arr):
    print('Fitur Max Heap')
    print('='*40)
    print('1. Insert Data')
    print('2. Delete Data')
    print('3. Keluar')
    choose = int(input('Masukkan pilihan fitur Max Heap (1-3) = '))
    print()
    if choose == 1:
        insert_max(arr)
    elif choose == 2:
        hapus = int(input('Data yang akan dihapus = '))
        if hapus in arr:
            print(f'Data {hapus} telah dihapus')
            deleteMax(arr,hapus)
            print(f'Heap = {arr}')
            print()
        else:
            print('Data tidak ditemukan')
            print()
        fiturMax(arr)
    elif choose == 3:
        fitur(arr)
        print()
    else:
        print('Kode yang anda masukkan salah')
        print()
        fiturMax(arr)

def insert_min(arr):
    print('Masukkan data ke dalam heap')
    print('='*40)
    n = int(input('Jumlah data = '))
    for i in range(n):
        temp = int(input(f'Input data ke-{i+1} = '))
        arr.append(temp)
        arr.sort()
    min_heap(arr)
    print(f'Heap = {arr}')
    print()
    fiturMin(arr)

def fiturMin(arr):
    print('Fitur Min Heap')
    print('='*40)
    print('1. Insert Data')
    print('2. Delete Data')
    print('3. Keluar')
    choose = int(input('Masukkan pilihan fitur Min Heap (1-3) = '))
    print()
    if choose == 1:
        insert_min(arr)
    elif choose == 2:
        hapus = int(input('Data yang akan dihapus = '))
        if hapus in arr:
            print(f'Data {hapus} telah dihapus')
            deleteMin(arr,hapus)
            print(f'Heap = {arr}')
            print()
        else:
            print('Data tidak ditemukan')
            print()
        fiturMin(arr)
    elif choose == 3:
        fitur(arr)
        print()
    else:
        print('Kode yang anda masukkan salah')
        print()
        min(arr)

def fitur(arr):
    print('Welcome to Program Heap')
    print('='*40)
    print('1. Create Max Heap')
    print('2. Creata Min Heap')
    print('3. Keluar')
    choose = int(input('Masukkan pilihan fitur (1-3) = '))
    print()
    if choose == 1:
        if len(arr) == 0:
            insert_max(arr)
        else:
            fiturMax(arr)
    elif choose == 2:
        if len(arr) == 0:
            insert_min(arr)
        else:
            fiturMin(arr)
    elif choose == 3:
        print('Terima kasih telah menggunakan program Heap')
    else:
        print('Kode yang anda masukkan salah')
        print()
        fitur(arr)

listnya = []

fitur(listnya)
