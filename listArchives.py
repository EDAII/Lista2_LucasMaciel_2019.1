import os
import fnmatch


def list_movies(path):
    print("---------------------------------------------------------------------------------------------")
    print("VIDEOS ENCONTRADOS NA PASTA:\n")
    listOfFiles = os.listdir(path)
    pattern = "*.mp4"
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            print("\t"+entry)
