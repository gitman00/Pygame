import pygame as py
import random
py.init()

WIDTH, HEIGHT = 1100, 2100
SCREEN=py.display.set_mode((WIDTH, HEIGHT))

def game():
	WIDTH, HEIGHT = 1100, 2100
	SCREEN=py.display.set_mode((WIDTH, HEIGHT))
	running=True
	clock=py.time.Clock()
	 
	 # importing tree images
	Car=py.image.load("car.png")
	tree=py.image.load("tree.png")
	tree1=py.image.load("tree.png")
	tree2=py.image.load("tree.png")
	tree3=py.image.load("tree.png")
	tree4=py.image.load("tree.png")
	tree5=py.image.load("tree.png")
	tree6=py.image.load("tree.png")
	tree7=py.image.load("tree.png")
	
	# importing obstacles
	ob=py.image.load("construction.png")
	
	# variables
	x=400
	y=1300
	xx1=-180
	xx2=-180
	xx3=-180
	xx4=-180
	xx5=680
	xx6=680
	xx7=680
	yy1=-70
	yy2=500
	yy3=1100
	yy4=1700
	yy5=400
	yy6=1000
	yy7=1600
	x_change=0
	y_change=0
	size=100
	Left_btnx=350
	Left_btny=1980
	Right_btnx=750
	Right_btny=1980
	rx=545
	ry=0
	ry1=190
	ry2=380
	ry3=570
	ry4=760
	ry5=950
	ry6=1140
	ry7=1330
	ox=250
	oy=100
	
	while running:
		
		SCREEN.fill((70,70,70))
		
		# Displaying images 
		py.draw.rect(SCREEN,((234,213,189)),(rx,ry,50,100))
		py.draw.rect(SCREEN,((234,213,189)),(rx,ry1,50,100))
		py.draw.rect(SCREEN,((234,213,189)),(rx,ry2,50,100))
		py.draw.rect(SCREEN,((234,213,189)),(rx,ry3,50,100))
		py.draw.rect(SCREEN,((234,213,189)),(rx,ry4,50,100))
		py.draw.rect(SCREEN,((234,213,189)),(rx,ry5,50,100))
		py.draw.rect(SCREEN,((234,213,189)),(rx,ry6,50,100))
		py.draw.rect(SCREEN,((234,213,189)),(rx,ry7,50,100))
		SCREEN.blit(Car,(x, y))
		SCREEN.blit(tree1,(xx1, yy1))
		SCREEN.blit(tree2,(xx2, yy2))
		SCREEN.blit(tree3,(xx3, yy3))
		SCREEN.blit(tree4,(xx4, yy4))
		SCREEN.blit(tree5,(xx5, yy5))
		SCREEN.blit(tree6,(xx6, yy6))
		SCREEN.blit(tree7,(xx7, yy7))
		
		
		py.draw.circle(SCREEN,((100,100,100)),(550,2000),200)
		
		
		
		
		Left_btn=py.draw.circle(SCREEN,((255,255,255)),(Left_btnx,Left_btny),size)
		Right_btn=py.draw.circle(SCREEN,((255,255,255)),(Right_btnx,Right_btny),size,)
		
		 
		 # Controls of the car
		finger_touch=py.mouse.get_pos()
		print(finger_touch)
		 
		if 300 + size > finger_touch[0] > 300 and 1950 + size > finger_touch[1] > 1950:
			x_change=-10
			x += x_change
		else:
			Left_btn=py.draw.circle(SCREEN,((255,255,255)),(Left_btnx,Left_btny),size)
			
		if 700 + size > finger_touch[0] > 700 and 1950 + size > finger_touch[1] > 1950:
			x_change=10
			x += x_change	
		else:
			Right_btn=py.draw.circle(SCREEN,((255,255,255)),(Right_btnx,Right_btny),size,)
			
		yy1 += 15
		if yy1 > 2200:	
			xx1=-180
			yy1=0
			
		yy2 += 15
		if yy2 > 2200:	
			xx2=-180
			yy2=0
			
		yy3 += 15
		if yy3 > 2200:	
			xx3=-180
			yy3=0
			
		yy4 += 15
		if yy4 > 2200:	
			xx4=-180
			yy4=0
			
		yy5 += 15
		if yy5 > 2200:	
			xx5=650
			yy5=-600
			
		yy6 += 15
		if yy6 > 2200:	
			xx6=650
			yy6=-600
			
		yy7 += 15
		if yy7 > 2200:	
			xx7=650
			yy7=-600
			
			
		ry +=20
		if ry> 2200:
			rx=545
			ry=0
			
		ry1 +=20
		if ry1> 2200:
			rx=545
			ry1=0
			
		ry2 +=20
		if ry2> 2200:
			rx=545
			ry2=0
			
		ry3 +=20
		if ry3> 2200:
			rx=545
			ry3=0
			
		ry4 +=20
		if ry4> 2200:
			rx=545
			ry4=0
			
		ry5 +=20
		if ry5> 2200:
			rx=545
			ry5=0
		
		ry6 +=20
		if ry6> 2200:
			rx=545
			ry6=0
			
		ry7 +=20
		if ry7> 2200:
			rx=545
			ry7=0
			
		
				
		clock.tick(60)	
		py.display.update()
		
font_style=py.font.Font('Blazed.ttf', 200)
font_style1=py.font.Font('Blazed.ttf', 120)
font_style2=py.font.Font('Sectar.otf', 60)

while True:
	SCREEN.fill((255,255,0))
	font_text=font_style.render('Game',True,((0,120,50)))
	SCREEN.blit(font_text,(0,500))
	font_text2=font_style.render('Under',True,((120,0,50)))
	SCREEN.blit(font_text2,(0,700))
	font_text3=font_style1.render('Construction',True,((50,120,0)))
	SCREEN.blit(font_text3,(0,900))
	font_text4=font_style2.render('only authorized person can',True,((255,0,0)))
	SCREEN.blit(font_text4,(100,1800))
	font_text5=font_style2.render('acess the game',True,((255,0,0)))
	SCREEN.blit(font_text5,(100,1900))
	
	
	game()
	py.display.update()