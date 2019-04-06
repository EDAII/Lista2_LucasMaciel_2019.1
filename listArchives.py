import os
import fnmatch
from searchMethods import *


def get_movies(path):
    try:
        listOfFiles = os.listdir(path)
        pattern = "*.mp4"
        videos = []
        index = 0
        for entry in listOfFiles:
            if fnmatch.fnmatch(entry, pattern):
                videos.append(entry)
        return videos
    except FileNotFoundError:
        print("Pasta nao encontrada")


def list_movies(videos=[]):
    print("---------------------------------------------------------------------------------------------")
    print("VIDEOS ENCONTRADOS NA PASTA:\n")
    videos = insertion_sort(videos)
    for i in range(len(videos) - 1):
        print(i, "-", end="")
        print("\t"+videos[i])


def list_dir():
    for dirs in next(os.walk('.'))[1]:
        print(dirs)
