import pygame as p

p.init()

SCREEN_WIDTH,SCREEN_HEIGHT=1100,2250

SCREEN=p.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

rect1=p.Rect(500,500,200,200)
x_speed,y_speed=5,-4

rect2=p.Rect(400,1000,200,400)
rect2_speed=2

def moving_rect():
	global x_speed,y_speed

	rect1.x += x_speed
	rect1.y += y_speed
	
	if rect1.right >= SCREEN_WIDTH or rect1.left<= 0:
		x_speed *= -1
		
	if rect1.bottom >= SCREEN_HEIGHT or rect1.top<= 0:
		y_speed *= -1
		
	collision_tolerance=10
	if rect1.colliderect(rect2):
		if abs(rect2.top-rect1.bottom)< collision_tolerance:
			y_speed *= -1
		if abs(rect2.bottom-rect1.top)< collision_tolerance:
			y_speed *= -1	
		if abs(rect2.right-rect1.left)< collision_tolerance:
			x_speed *= -1
		if abs(rect2.left-rect1.right)< collision_tolerance:
			x_speed *= -1
				
	p.draw.rect(SCREEN,((255,0,0)),rect1)
	p.draw.rect(SCREEN,((0,0,255)),rect2)
	
On=True
while On:
	SCREEN.fill((0,0,0))
	moving_rect()
	p.display.update()