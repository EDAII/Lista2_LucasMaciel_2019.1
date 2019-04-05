from moviepy.editor import VideoFileClip
import pygame
from pygame.locals import *

def play_movie(path, title):
    try:
        pygame.display.set_caption(title)
        clip = VideoFileClip(path+"/"+title)
        clip.preview()
        print("Reproduzindo...")
        pygame.quit()
    except:
        print("Video nao encontrado")
        input()