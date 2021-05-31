import pygame
import math
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def draw_lines():
	glColor3f(0,1,2)
	glBegin(GL_POINTS)
	for i in range(0,1000):
		glVertex3f(math.cos(2*3.14159*i/1000.0),math.sin(2*3.14159*i/1000.0),r)
		glVertex2f(math.cos(2*3.14159*i/1000.0),math.cos(2*3.14159*i/1000.0))
	glEnd()


def main():
	pygame.init()
	display=(800,600)
	pygame.display.set_mode(display, DOUBLEBUF | OPENGL)


	gluPerspective(45, (display[0] / display[1]), 0.1,  50.0)

	glTranslatef(0.0, 0.0, -10)

	glRotatef(0, 0, 0, 0)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		draw_lines()
		# glRotatef(1,4,1,1)
		pygame.display.flip()
		pygame.time.wait(10)

r=float(input("Enter value of radius "))
main()