from moviepy.editor import VideoFileClip
import pygame

def play_movie(path):
    pygame.display.set_caption('My video!')

    clip = VideoFileClip('videos/cut.mp4')
    clip.preview()
    pygame.event.wait()