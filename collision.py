import sys
import pygame
from pygame.locals import *
import winsound
width = 600
height = 400
colors={
    "white":[255,255,255],
    "black":[0,0,0],
    "red":[255,0,0],
    "green":[0,255,0],
    "blue":[0,0,255]
}
fps = 6000

pygame.init()

pygame.display.set_caption("왜 충돌실험이 파이를 출력할까?")
displaysurf = pygame.display.set_mode((width, height),0, 32)
clock = pygame.time.Clock()

rectA = {
    "mess" :1, #kg
    "speed":0,
    "x":100
}
num = 3
rectB = {
    "mess" :100**(num), #kg
    "speed":-0.03,
    "x":230
}
collisions = 0
font = pygame.font.SysFont('굴림', 40)
collisions_text = font.render("Collisions : ", 1, colors["white"])


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    rectA["x"] = rectA["x"] + rectA["speed"]
    rectB["x"] = rectB["x"] + rectB["speed"]
    m1 = rectA["mess"]
    m2 = rectB["mess"]
    v1 = rectA["speed"]
    v2 = rectB["speed"]
    if(rectA["x"] + 30 > rectB["x"]):
        #print((rectA["speed"]**(2))*rectA["mess"]*(1/2) + (rectB["speed"]**(2))*rectB["mess"]*(1/2))
        rectA["speed"] = ((v1*(m1-m2)+2*m2*v2)/(m1+m2))
        rectB["speed"] = ((v2*(m2-m1)+2*m1*v1)/(m1+m2))
        collisions = collisions + 1
        #winsound.PlaySound("clack_sound.wav", winsound.SND_ASYNC)
    if(rectA["x"] <= 20):
        rectA["speed"] = rectA["speed"] * -1
        collisions = collisions + 1
        #winsound.PlaySound("clack_sound.wav", winsound.SND_ASYNC)
    displaysurf.fill(colors["black"])
    collisions_text = font.render(str(collisions), 1, colors["white"])
    displaysurf.blit(collisions_text, [300,0])
    pygame.draw.line(displaysurf, colors["white"], (20,10), (20,380), 3)
    pygame.draw.line(displaysurf, colors["white"], (10,370), (580,370), 3)

    if(rectA["x"] < 20):
        pygame.draw.rect(displaysurf, colors["red"],[20,365-30,30,30],100)
    else:
        pygame.draw.rect(displaysurf, colors["red"],[rectA["x"],365-30,30,30],100)
    if(rectB["x"] < 50):
        pygame.draw.rect(displaysurf, colors["blue"],[50,365-60,60,60],100)
    else:
        pygame.draw.rect(displaysurf, colors["blue"],[rectB["x"],365-60,60,60],100)

    pygame.display.update()
    clock.tick(fps)