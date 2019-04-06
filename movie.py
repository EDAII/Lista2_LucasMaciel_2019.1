from moviepy.editor import VideoFileClip
import pygame
import re


def play_movie(path, videos, title):
    # verifica se o usuario digitou um video.mp4 ou o indice
    try:
        parse = re.findall(r"[\w']+", title)
        print("parse = ", parse[-1])
        if parse[-1] != 'mp4':                  # se condicao for verdadeira, entao usuario passou um indice
            title = videos[int(parse[0])][0]    # videos[indice][0] - [0] representa o indice do titulo do video

        print("Reproduzindo: "+title)
        pygame.display.set_caption(title)
        clip = VideoFileClip(path+"/"+title)
        clipresized = clip.resize (width=500, height=400)
        clipresized.preview()
        pygame.quit()
    except:
        print("Video nao encontrado")
        input()
