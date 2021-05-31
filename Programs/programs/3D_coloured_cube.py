import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
	(0, 0, 0),
	(2, 0, 0),
	(2, 2, 0), 
	(0, 2, 0),
	(0, 2, 2),
	(0, 0, 2),
	(2, 0, 2), 
	(2, 2, 2)
	)

edges = (
	(0, 1),
	(0, 3), 
	(0, 5),
	(1, 2),
	(1, 6),
	(2, 3),
	(2, 7),
	(3, 4),
	(4, 5),
	(5, 6), 
	(6, 7), 
	(7, 4)
	)

surfaces = (
	(0, 1, 2, 3),
	(0, 3, 4, 5),
	(0, 1, 6, 5),
	(1, 2, 7, 6),
	(2, 3, 4, 7),
	(4, 5, 6, 7)
	)

colors = (
	(1, 0, 0),
	(0, 1, 0),
	(0, 0, 1),
	(1, 1, 0),
	(0, 1, 1),
	(1, 0, 1),
	)

colors = (
	(1, 0, 0),
	(0, 1, 0),
	(0, 0, 1),
	(1, 1, 0),
	(0, 1, 1),
	(1, 0, 1),
	)




def cube():
	glBegin(GL_QUADS)
	for surface in surfaces:
		x = 0
		for vertex in surface:
			x += 1
			glColor3fv(colors[x])
			glVertex3fv(vertices[vertex])

	glEnd()




	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex])
	glEnd()
def main():
	pygame.init()
	display=(800,600)
	pygame.display.set_mode(display, DOUBLEBUF | OPENGL)


	gluPerspective(45, (display[0] / display[1]), 0.1,  50.0)

	glTranslatef(-1, 0.0, -10) #rotate among (x,y,z)

	glRotatef(0, 0, 0, 0)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					glTranslatef(-1, 0, 0)

				if event.key == pygame.K_RIGHT:
					glTranslatef(1, 0, 0)

				if event.key == pygame.K_UP:
					glTranslatef(0, 1, 0)

				if event.key == pygame.K_DOWN:
					glTranslatef(0, -1, 0)

		glRotatef(1, 3, 1, 1)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		cube()
		pygame.display.flip()
		pygame.time.wait(10)
main()