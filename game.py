import pygame, time, random, os
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('game')
screen.fill((233, 232, 90))
success = [False]*100
clock = pygame.time.Clock()
crashed = False
pygame.draw.rect(screen, (255, 255, 255), (100, 100, 360, 360))

def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()
 
def show(tup):
	x, y = tup
	first, second = tup
	x -= 100
	y -= 100
	if x >= 0 and x < 360 and y >= 0 and y < 360:
		x //= 60
		y //= 60
		first = first-((first-100)%60)
		second = second-((second-100)%60)
		temp = ls.index(y*6+x)
		temp //= 2
		car(first, second, os.path.join('img', 'img ('+str(temp)+').png'))
	return (x, y)

def car(x, y, name):
	img = pygame.image.load(name)
	img = pygame.transform.scale(img, (60, 60))
	rect = img.get_rect()
	rect = rect.move(x, y)
	#pygame.display.update()
	screen.blit(img, rect)

def layout(x, y):
	if x >= 0 and x < 360 and y >= 0 and y < 360:
		if success[y*6+x] == False:
			pygame.draw.rect(screen, ((x^y)%255, ((x|y)*60)%255, ((x&y)*62)%255), (60*x+100, 60*y+100, 60, 60))

ls = random.sample(range(0, 36), 36)

for m in range(6):
	i = 100
	j = 100
	for n in range(6):
		loc = 6*m+n
		temp = ls.index(loc)
		temp //= 2
		layout(m, n)
		i += 60
	j += 60	

	
check = 0
last = -2
pre_x, pre_y = 0, 0
pre_dol = False
fail = 0
count = 0
clicks = 0
finish = False
largeText = pygame.font.SysFont("comicsansms",50)
TextSurf, TextRect = text_objects("Clicks: " , largeText)
TextRect.center = ((100),(500))
screen.blit(TextSurf, TextRect)
TextSurf, TextRect = text_objects("Success: " , largeText)
TextRect.center = ((110),(70))
screen.blit(TextSurf, TextRect)
TextSurf, TextRect = text_objects("Fail: " , largeText)
TextRect.center = ((480),(70))
screen.blit(TextSurf, TextRect)


while not crashed:
	TextSurf, TextRect = text_objects(str(clicks), largeText)
	TextRect.center = (200, 500)
	screen.blit(TextSurf, TextRect)
	TextSurf, TextRect = text_objects(str(count) , largeText)
	TextRect.center = ((240),(70))
	screen.blit(TextSurf, TextRect)
	TextSurf, TextRect = text_objects(str(fail) , largeText)
	TextRect.center = ((550),(70))
	screen.blit(TextSurf, TextRect)
	check += 1
	if finish == True:
		lrgtxt = pygame.font.SysFont("comicsansms",100)
		TextSurf = lrgtxt.render("You Won", True, (255, 0, 255))
		TextRect = TextSurf.get_rect()
		TextRect.center = ((270),(250))
		screen.blit(TextSurf, TextRect)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			pygame.draw.rect(screen, (233, 232, 90), (170, 480, 80, 50))
			pygame.mixer.music.load('tone (2).wav')
			pygame.mixer.music.play(0)
			now = pygame.time.get_ticks()
			if now-last <= 400:
				single_click = False
			else: 
				single_click = True
			last = pygame.time.get_ticks()
			first, second = event.pos
			x, y = first, second
			x -= 100
			y -= 100
			if single_click == True:
				if first >= 100 and first <= 460 and second >= 100 and second <= 460:
					clicks += 1
				if pre_dol == False:
					layout(pre_x, pre_y)
				else:
					temp1 = ((y//60)*6)+(x//60)
					temp2 = (pre_y*6)+pre_x
					if temp1 == temp2:
						continue
					if x >= 0 and x < 360 and y >= 0 and y < 360:
						temp1 = ls.index(temp1)
					if pre_x >= 0 and pre_x < 360 and pre_y >= 0 and pre_y < 360:
						temp2 = ls.index(temp2)
					temp1 //= 2
					temp2 //= 2
					show((event.pos))
					print(temp1, temp2)
					if temp1 != temp2:
						time.sleep(0.3)
						pygame.mixer.music.load('tone (3).wav')
						pygame.mixer.music.play(0)
						fail += 1
						pygame.draw.rect(screen, (233, 232, 90), (530, 50, 60, 50))

					else:
						clicks -= 1	
						pygame.draw.rect(screen, (233, 232, 100), (200, 50, 80, 50))
						success[pre_y*6+pre_x] = True
						success[(y//60)*6+(x//60)] = True
						pygame.mixer.music.load('tone (1).wav')
						pygame.mixer.music.play(0)
						count += 1
						if count == 18:
							finish = True
							pygame.mixer.music.load('jazz.wav')
							pygame.mixer.music.play(0)
					layout(x//60, y//60)
					layout(pre_x, pre_y)
			else:
				layout(pre_x, pre_y)
			retrn = show(event.pos)
			pre_x = retrn[0]
			pre_y = retrn[1]
			if single_click == False:
				pre_dol = True
			else:
				pre_dol = False
			
	l = 1
	pygame.display.update()
	clock.tick(60)
	
pygame.quit()
quit()
