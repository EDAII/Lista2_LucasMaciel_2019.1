import os, fnmatch

listOfFiles = os.listdir('videos')
pattern = "*.mp4"  
for entry in listOfFiles:  
    if fnmatch.fnmatch(entry, pattern):
            print (entry)