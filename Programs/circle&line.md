## Aim: To make a line and a circle using pixels.
## Overview
<img src="https://github.com/kr123Manish/ComputerGraphics_with_openGL/blob/main/Programs/images/circleline.PNG"></img>
- First import all necessary files.
``` 
import pygame 
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
```
- Now we are ready to make our line and circle using pixels. To do this we create a function.
```python
def draw_lines():
  //funtion_defination...
```
- In OpenGL every drawing statement should be written between ```glBegin()``` and ```glEnd().```
```python
def draw_lines():
	glColor3f(0,1,2)  #for colours
	glBegin(GL_POINTS)
	for i in range(0,1000): #get 1000 pixels for line or circle
		glVertex3f(math.cos(2*3.14159*i/1000.0),math.sin(2*3.14159*i/1000.0),r) #for circle in form of (x-axis,y-axis,radius)
		glVertex2f(math.cos(2*3.14159*i/1000.0),math.cos(2*3.14159*i/1000.0)) #for line in form of (x-axis,y-axis)
	glEnd()
 ```
 - In the above program one should understand some functions used in the program.

- ```glColor3fv()``` function is used for coloring the pixel in sky blue colour in can varry when you change its value.

- gl stands for graphics library, Color stands for operation, 3fv,2fv means function will take three and two arguments that are floating point value.

- Similarly, ```glVertex3fv()``` has its own meaning. It is used to draw vertex. In the program we pass vertex x,y as an parameter

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
		draw_lines()  #function call.
		# glRotatef(1,4,1,1)
		pygame.display.flip()
		pygame.time.wait(10)

r=float(input("Enter value of radius "))  #taking radius as an input.
main()
```
- Final step is to make some user commands to move the pixel, close the window and auto movement of pixel.
- To do so one can use pygame game pygame.event that take input event from user like keyboard input, mouse input.
- Overall code looks likes this.
```python
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

	glTranslatef(0.0, 0.0, -10) #self movement of pixel.

	glRotatef(0, 0, 0, 0)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #For refresh rate(frame buffer)
		draw_lines()
		# glRotatef(1,4,1,1)  #for rotation.
		pygame.display.flip()
		pygame.time.wait(10)

r=float(input("Enter value of radius "))
main()
```
## Completed.
