import os
import time
import pyautogui
import pygame

files = os.listdir(path=".")
files.pop(-3)
files = len(files)

pyautogui.FAILSAFE = False

display = pygame.display.set_mode((683, 383))

i = 0

display.blit(pygame.image.load("menu.png"), (0, 0))
pygame.display.update()

is_render = False

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        if x >= 266 and y >= 36:
            if x <= 426 and y <= 102:
                is_render = True
    if is_render == True:
        for x in range(0, files):
            os.system(f"scene{i}.blend")
            pyautogui.click()
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'F12')
            while not os.path.isfile(f'./scene{i}0001.png'):
                pass
            os.system("taskkill /f /IM blender.exe")
            i += 1
            if i > files:
                exit()
