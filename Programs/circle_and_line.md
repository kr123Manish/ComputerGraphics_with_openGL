## Aim: To make a line and a circle using pixels.
## Overview
<img src="https://github.com/kr123Manish/ComputerGraphics_with_openGL/blob/main/Programs/images/circleline.PNG"></img>
- First import all necessary files.
``` python
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
## Completed :)
<h3>For better understanding follow this sequence to study the programs</h3>
<li>
	<a href="https://github.com/kr123Manish/ComputerGraphics_with_openGL/blob/main/Programs/draw_a_pixel.md">How To Make Pixel. </a>
</li>

<li>
	<a href="https://github.com/kr123Manish/ComputerGraphics_with_openGL/blob/main/Programs/circle_and_line.md">Create line and circle using pixel.</a>
</li>

<li>
	<a href="https://github.com/kr123Manish/ComputerGraphics_with_openGL/blob/main/Programs/2D_and_3D_Model.md">Create 2D and 3D model using lines.</a>
</li>

<li>
	<a href="https://github.com/kr123Manish/ComputerGraphics_with_openGL/blob/main/Programs/3D_model_and_colour_filling.md">Create 2D and 3D model using Quard and colour filling.</a>
</li>
<h4><a href="https://kr123manish.github.io/CG_video.github.io/">Click here to see the videos of all practicals</a></h4>

