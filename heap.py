ef max_heapify(A, k):
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
    n = (len(A)//2)-1
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
    n = (len(A)//2)-1
    for k in range(n, -1, -1):
        min_heapify(A, k)

def insert(list,data):
    list.append(data)
    return list

def delete(list,data):
    indeks = 0
    if data in list:
        for i in list:
            if data == i:
                break
            else:
                indeks += 1
                continue

        list[indeks] = list[-1]
        list.pop(-1)
        return list
    else:
        print('Data tidak ditemukan')


def insert_max(list):
    print('Masukkan data ke dalam heap')
    print('='*40)
    n = int(input('Jumlah data = '))
    for i in range(n):
        temp = int(input(f'Input data ke-{i+1} = '))
        insert(list,temp)
        max_heap(list)
    print(f'Heap = {list}')
    print()
    max(list)

def max(list):
    print('Fitur Max Heap')
    print('='*40)
    print('1. Insert Data')
    print('2. Delete Data')
    print('3. Keluar')
    choose = int(input('Masukkan pilihan fitur Max Heap (1-3) = '))
    print()
    if choose == 1:
        insert_max(list)
    elif choose == 2:
        hapus = int(input('Data yang akan dihapus = '))
        if hapus in list:
            print(f'Data {hapus} telah dihapus')
            delete(list,hapus)
            max_heap(list)
            print(f'Heap = {list}')
            print()
        else:
            print('Data tidak ditemukan')
            print()
        max(list)
    elif choose == 3:
        fitur(list)
        print()
    else:
        print('Kode yang anda masukkan salah')
        print()
        max(list)

def insert_min(list):
    print('Masukkan data ke dalam heap')
    print('='*40)
    n = int(input('Jumlah data = '))
    for i in range(n):
        temp = int(input(f'Input data ke-{i+1} = '))
        insert(list,temp)
        min_heap(list)
    print(f'Heap = {list}')
    print()
    min(list)

def min(list):
    print('Fitur Min Heap')
    print('='*40)
    print('1. Insert Data')
    print('2. Delete Data')
    print('3. Keluar')
    choose = int(input('Masukkan pilihan fitur Min Heap (1-3) = '))
    print()
    if choose == 1:
        insert_min(list)
    elif choose == 2:
        hapus = int(input('Data yang akan dihapus = '))
        if hapus in list:
            print(f'Data {hapus} telah dihapus')
            delete(list,hapus)
            min_heap(list)
            print(f'Heap = {list}')
            print()
        else:
            print('Data tidak ditemukan')
            print()
        min(list)
    elif choose == 3:
        fitur(list)
        print()
    else:
        print('Kode yang anda masukkan salah')
        print()
        min(list)

def fitur(list):
    print('Welcome to Program Heap')
    print('='*40)
    print('1. Create Max Heap')
    print('2. Creata Min Heap')
    print('3. Keluar')
    choose = int(input('Masukkan pilihan fitur (1-3) = '))
    print()
    if choose == 1:
        if len(list) == 0:
            insert_max(list)
        else:
            max(list)
    elif choose == 2:
        if len(list) == 0:
            insert_min(list)
        else:
            min(list)
    elif choose == 3:
        print('Terima kasih telah menggunakan program Heap')
    else:
        print('Kode yang anda masukkan salah')
        print()
        fitur(list)

listnya = []

fitur(listnya)
