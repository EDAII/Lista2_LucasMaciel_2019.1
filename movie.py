from moviepy.editor import VideoFileClip
import pygame

pygame.display.set_caption('My video!')

clip = VideoFileClip('videos/CLEAN CODE 1 Introdução.mp4')
clip.preview()
pygame.event.wait()