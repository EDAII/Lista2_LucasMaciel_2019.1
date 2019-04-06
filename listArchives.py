import os
import fnmatch
from sortMethods import *
import subprocess
import re


def get_metadata_movie(path, title):
    ''' Retorna os dados de cada video, como duracao e data de criacao'''
    output = subprocess.check_output(["hachoir-metadata", path+"/"+title]).splitlines() # extrai os metadados do video e separa cada categoria
    
    duration = re.findall(r"[\w']+", str(output[1]))    # metadado referente a duracao do video, 1 - elemento referente a duracao do video
    duration_formatted =  ' '.join(str(duration[i]) for i in range(2, len(duration) - 2)) # corta partes nao necessarias do dado
    
    date = re.findall(r"[\w']+", str(output[4]))    # mesmo processo do duration
    date_formatted = '-'.join(str(date[i]) for i in range(3, len(date)-3))+' '+':'.join(str(date[i]) for i in range(len(date)-3, len(date)-1))
    
    output_formatted = [duration_formatted, date_formatted]
    return output_formatted


def get_movies(path):
    try:
        listOfFiles = os.listdir(path)
        pattern = "*.mp4"
        videos = []
        index = 0
        for title in listOfFiles:
            if fnmatch.fnmatch(title, pattern):
                video = []
                metadata = get_metadata_movie(path, title) # duration and date
                video = [title, metadata[0], metadata[1]]
                videos.append(video)
        return videos
    except FileNotFoundError:
        print("Pasta nao encontrada")


def list_movies(videos=[], field = 0, ord = 0):
    field_sort = 'titulo'
    ord_sort = 'ascendente'
    if field == 1:
        field_sort = 'duracao do video'
    elif field == 2:
        field_sort = 'data'
    
    if ord == 1:
        ord_sort = 'descendente'

    print("---------------------------------------------------------------------------------------------")
    print("Videos Encontrados na Pasta (ordenacao = "+field_sort+", "+ord_sort+"):\n")
    videos = insertion_sort(videos, field, ord)
    for i in range(len(videos)):
        print(i, "-", end="\t")
        print(videos[i][0]+"\t"+videos[i][1]+"\t"+videos[i][2])
    return videos


def list_dir():
    print("---------------------------------------------------------------------------------------------")
    print("Diretorios Encontrados:\n")
    for dirs in next(os.walk('.'))[1]:
        print(dirs)
