## Aim: To make a 2D and 3D Model using lines.
## Overview
<p float="left">
  <img src="https://github.com/kr123Manish/ComputerGraphics_with_openGL/blob/main/Programs/images/triangle.PNG" width=49%></img>
  <img src="https://github.com/kr123Manish/ComputerGraphics_with_openGL/blob/main/Programs/images/3Dcube.PNG" width=49%></img>
</p>

- First import all necessary files.
``` python
import pygame 
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
```
- Now we are ready to make our triangel and cube using lines. To do this we create a function.
```python
def draw_lines(A):
  //funtion_defination...
```
```python
def cube():
  //funtion_defination...
```
- In OpenGL every drawing statement should be written between ```glBegin()``` and ```glEnd().```
## Part 1 for triangle.
```python
def draw_lines(A):
	glColor3f(0,1,2)
	glBegin(GL_LINES)
	for i in A:
		glVertex2f(i[0],i[1])
	glEnd()
```
 - In the above program one should understand some functions used in the program.

- ```glColor3fv()``` function is used for coloring the pixel in sky blue colour in can varry when you change its value.

- gl stands for graphics library, Color stands for operation, 3fv,2fv means function will take three and two arguments that are floating point value.

- Similarly, ```glVertex2fv()``` has its own meaning. It is used to draw vertex. In the program we pass vertex x,y as an parameter

- It's time to step up the screen for this one can use and call the function.
```python
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
		draw_lines(A)  #function call.
		# glRotatef(1,4,1,1)
		pygame.display.flip()
		pygame.time.wait(10)
#Here we create a touple for vertices of triangle.
a=[(-1,-1),(2,-1), #coordinates of line AC
   (-1,-1),(0.5,2), #coordinates of line AB
   (2,-1),(0.5,2)]  #coordinates of line CB	
A=tuple(a)
main(A)
```
- Final step is to make some user commands to move the pixel, close the window and auto movement of pixel.
- To do so one can use pygame game pygame.event that take input event from user like keyboard input, mouse input.
- Overall code looks likes this.
```python
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def draw_lines(A):
	glColor3f(0,1,2)
	glBegin(GL_LINES)
	#glBegin(GL_QUADS)

	for i in A:
		glVertex2f(i[0],i[1])
	glEnd()


def main(A):
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
		draw_lines(A)
		# glRotatef(1,4,1,1)
		pygame.display.flip()
		pygame.time.wait(10)
# below code is used for make polygon where coordinates are taken from user.
# n=int(input("Enter value of n"))
# a=[]
# for i in range(0,n):
# 	x=float(input("Enter x"))
# 	y=float(input("Enter y"))
# 	a.append((x,y))
a=[(-1,-1),(2,-1),
   (-1,-1),(0.5,2),
   (2,-1),(0.5,2)]	
A=tuple(a)
main(A)
```
### code for triangle is finished.
## Part2 for cube.
- Here using out art skills to draw a rough diagram on paper with proper coordinates of points as shown below.
<img src="https://github.com/kr123Manish/ComputerGraphics_with_openGL/blob/main/Programs/images/cube.jpg"></img>
- In program your vertices will be in touple which looks like
```python
vertices = (
	(0, 0, 0),	#Point 0
	(2, 0, 0),	#Point 1
	(2, 2, 0), 	#Point 2
	(0, 2, 0),	#Point 3
	(0, 2, 2),	#Point 4
	(0, 0, 2),	#Point 5
	(2, 0, 2), 	#Point 6
	(2, 2, 2)	#Point 7
	)
```
- Next we connect vertices, for this we create a edges touple.
```python
edges = (
	(0, 1),	#This means connect Point 0 to Point 1.
	(0, 3), #Similarly, other connections are to be made
	(0, 5),	#according to the diagram of cube.
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
```
- Now we are ready to make our cube. To do this we create a function.
```python
def cube():
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex])
	glEnd()
```
- From now all steps is almost same like triange.
```python
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
		cube()
		glRotatef(1,4,1,1)
		pygame.display.flip()
		pygame.time.wait(10)
main()
```
- Overall code is 
```python
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
		cube()
		glRotatef(1,4,1,1)
		pygame.display.flip()
		pygame.time.wait(10)
main()
```
### Completed :)
### now we can try for quard color filling and make 3D model from user input.



