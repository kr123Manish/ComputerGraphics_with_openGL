import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def draw_pixel(A):
	glColor3f(0,1,2)
	glBegin(GL_POINTS)
	for i in A:
		glVertex2f(i[0],i[1])
	glEnd()


def main(A):
	pygame.init()
	display=(1000,800)
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
		draw_pixel(A)
		#glRotatef(1,4,1,1)
		pygame.display.flip()
		pygame.time.wait(10)


# n=int(input("Enter value of n"))
# a=[]
# for i in range(0,n):
# 	x=float(input("Enter x"))
# 	y=float(input("Enter y"))
# 	a.append((x,y))
a=[(-1,-1),(2,-1),(0.5,2)]	
A=tuple(a)
main(A)
	
