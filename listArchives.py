import os
import fnmatch


def list_movies(path):
    try:
        listOfFiles = os.listdir(path)
        print("---------------------------------------------------------------------------------------------")
        print("VIDEOS ENCONTRADOS NA PASTA:\n")
        pattern = "*.mp4"
        videos = []
        for entry in listOfFiles:
            if fnmatch.fnmatch(entry, pattern):
                print("\t"+entry)
                videos.append(entry)
        return videos
    except FileNotFoundError:
        print("Pasta nao encontrada")


def list_dir():
    for dirs in next(os.walk('.'))[1]:  
        print(dirs)
