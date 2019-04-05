from moviepy.editor import VideoFileClip
import pygame
from pygame.locals import *

def play_movie(path, title):
    try:
        print("Reproduzindo: "+title)
        pygame.display.set_caption(title)
        clip = VideoFileClip(path+"/"+title)
        clip.preview()
        pygame.quit()
    except:
        print("Video nao encontrado")
        input()