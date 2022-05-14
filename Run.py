import pygame

from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from constants import *
from Render import Chair

def main():
    pygame.init()
    display = (600, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(60, (display[0]/display[1]), 0, -20)
    glTranslatef(0, 0, -20)
    glRotatef(-90, 2, 0, 0)
main()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False    
    glRotatef(6, 3, -10, -45)        
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    Chair()
    pygame.display.flip()
    pygame.display.set_caption("Graphics")
    pygame.time.wait(10)
pygame.quit()
quit()    