def selection_sort(videos = [], field = 0, ord = 0):
    '''
        Funcao para ordenar com o metodo selection sort
        o argumento field se refere a qual campo do vetor sera feito a comparacao:
            0 - titulo do video
            1 - duracao do video
            2 - data de criacao
    '''
    index_min = 0
    aux = 0
    if ord == 0:
        compare = compare_videos_min
    elif ord == 1:
        compare = compare_videos_max

    for i in range(len(videos) - 1):
        index_min = i
        for j in range(i, len(videos)):
            if videos[j][field] < videos[index_min][field]:
                index_min = j
        if index_min != i:
            aux = videos[index_min]
            videos[index_min] = videos[i]
            videos[i] = aux
    return videos

def insertion_sort(videos = [], field = 0, ord = 1):
    '''
        Funcao para ordenar com o metodo insertion sort
        o argumento field se refere a qual campo do vetor sera feito a comparacao:
            0 - titulo do video
            1 - duracao do video
            2 - data de criacao
    '''
    aux = 0
    if ord == 0:
        compare = compare_videos_min
    elif ord == 1:
        compare = compare_videos_max
    
    for i in range(1, len(videos)):
        j = i
        while(compare(videos[j][field], videos[j - 1][field]) and j > 0):
            aux = videos[j]
            videos[j] = videos[j - 1]
            videos[j - 1] = aux
            j-=1
    return videos

def bubble_sort(vector = [], field = 0, ord = 0):
    '''
        Funcao para ordenar com o metodo bubble sort
        o argumento field se refere a qual campo do vetor sera feito a comparacao:
            0 - titulo do video
            1 - duracao do video
            2 - data de criacao
    '''
    aux = 0
    if ord == 0:
        compare = compare_videos_min
    elif ord == 1:
        compare = compare_videos_max

    while True:
        count = 0
        for i in range(1, len(vector)):
            if vector[i][field] < vector[i-1][field]:
                aux = vector[i]
                vector[i] = vector[i-1]
                vector[i-1] = aux
                count = 1
        if count == 0:
            return vector

def compare_videos_min(video1, video2):
    if video1 < video2:
        return True
    return False

def compare_videos_max(video1, video2):
    if video1 > video2:
        return True
    return False