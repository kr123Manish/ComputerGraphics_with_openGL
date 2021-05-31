## Aim: To make a pixel using openGL.
## Overview
<img src="https://github.com/kr123Manish/ComputerGraphics_with_openGL/blob/main/Programs/images/pixel1.PNG"></img>
- First import all necessary files.
``` 
import pygame 
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
```
- Now we are ready to make our pixel. To do this we create a function.
```python
def draw_pixel(x,y):
  //funtion_defination...
```
<img src="https://github.com/kr123Manish/ComputerGraphics_with_openGL/blob/main/Programs/images/pixel.PNG"></img>
- In OpenGL every drawing statement should be written between ```glBegin()``` and ```glEnd().```
```python
def draw_pixel(x,y):
	glColor3f(0,1,2) #gives sky blue colour for pixel
	glBegin(GL_POINTS)
	glVertex2i(x,y) #take x,y vertex.
	glEnd()
  ```
  - In the above program one should understand some functions used in the program.

- ```glColor3fv()``` function is used for coloring the pixel in sky blue colour in can varry when you change its value.

- gl stands for graphics library, Color stands for operation, 3fv means function will take three arguments that are floating point value.

- Similarly, ```glVertex3fv()``` has its own meaning. It is used to draw vertex. In the program we pass vertex x,y as an parameter

- It's time to step up the screen for this one can use and call the function.
``` python
def main():
	pygame.init()
	display=(800,600) #screen size
	pygame.display.set_mode(display, DOUBLEBUF | OPENGL) #For refresh rate(frame buffer)



	gluPerspective(45, (display[0] / display[1]), 0.1,  50.0)
    #Here 45 is angle view, then aspect ratio of screen (800/600),zoom in, zoom out
	glTranslatef(0.0, 0.0, -10)  #self movement of pixel.

	glRotatef(0, 0, 0, 0)  #for rotation.

	while True: ##user command input part.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		draw_pixel(0,0) #draw_pixel function call where x,y=0.
		#glRotatef(1,4,1,1) #auto rotation of pixel at point(x=1,y=4,z=1,speed=1).
		pygame.display.flip()  #update button.
		pygame.time.wait(10)  

main()  #function call.
```
- Final step is to make some user commands to move the pixel, close the window and auto movement of pixel.
- To do so one can use pygame game pygame.event that take input event from user like keyboard input, mouse input.
- Overall code looks likes this.
```python
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def draw_pixel(x,y):
	glColor3f(0,1,2)
	glBegin(GL_POINTS)
	glVertex2i(x,y)
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
		draw_pixel(0,0)
		#glRotatef(1,4,1,1)
		pygame.display.flip()
		pygame.time.wait(10)

main()
```
- You can also try for this by setting different x an y axis or make it custom by taking input from user.
<img src="https://github.com/kr123Manish/ComputerGraphics_with_openGL/blob/main/Programs/images/pixel3.PNG"></img>
## Completed.
