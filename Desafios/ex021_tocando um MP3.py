# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3. (arquivo não incluso)(atualizado 2021)

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
parar = input('')
