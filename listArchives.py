import os
import fnmatch


def list_movies(path):
    # os.system('clear')
    print("---------------------------------------------------------------------------------------------")
    print("VIDEOS ENCONTRADOS NA PASTA:")
    listOfFiles = os.listdir(path)
    pattern = "*.mp4"
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            print(entry)
