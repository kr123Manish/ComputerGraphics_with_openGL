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

r=float(input("Enter value of radius "))  #taking radius as an input.
main()
```


