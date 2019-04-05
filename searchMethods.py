def selection_sort(vector = []):
    index_min = 0
    aux = 0
    for i in range(len(vector) - 1):
        index_min = i
        for j in range(i, len(vector) - 1):
            if vector[j] < vector[index_min]:
                index_min = j
        if index_min != i:
            aux = vector[index_min]
            vector[index_min] = vector[i]
            vector[i] = aux
    return vector

def insertion_sort(vector = []):
    aux = 0
    for i in range(1, len(vector) - 1):
        j = i
        while(vector[j] < vector[j - 1] and j > 0):
            aux = vector[j]
            vector[j] = vector[j - 1]
            vector[j - 1] = aux
            j-=1
    return vector

def bubble_sort(vector = []):
    aux = 0
    while True:
        count = 0
        for i in range(1, len(vector) - 1):
            if vector[i] < vector[i-1]:
                aux = vector[i]
                vector[i] = vector[i-1]
                vector[i-1] = aux
                count = 1
        if count == 0:
            return vector