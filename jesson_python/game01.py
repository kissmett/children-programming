import pygame
import sys,random

def draw_circles(screen):
    for i in range(100):
        x = random.randint(0,640)
        y = random.randint(0,480)
        r = random.randint(20,50)
        color = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
        print(x,y,r)
        pygame.draw.circle(screen,color,[x,y],r,2)
        
pygame.init()
screen = pygame.display.set_mode([640,480])
timer = pygame.time.Clock()
screen.fill([100,100,100])
draw_circles(screen)
pygame.display.flip()
running = True
while running:
    screen.fill([100,100,100])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('close window')
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            print('mouse up')
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('mouse down')
    draw_circles(screen)
    pygame.display.flip()
    timer.tick(60)
pygame.quit()