import pygame
import sys
import random

w=480
h=640

miss = 0 

pad = pygame.display.set_mode((w,h)) #화면 생성
pygame.display.set_caption("Shooting Game") #제목 설정
#--------------------이미지로드 함수--------------------
def img_load(obj):
    img = pygame.image.load(str(obj)+'.png')
    img_size = img.get_rect().size
    return img, img_size[0], img_size[1]
#------------------------------------------------------

bg= img_load('background') [0]


p, pw,ph = img_load('eyes') #전투기이미지
px = w * 0.4 #전투기의 초기 x위치
py = h * 0.9 #전투기의 초기 y위치

ps=0 #전투기 스피드

#--------장애물그리기--------------------------------

rlist = ['rock01','rock02','rock03','rock04','rock05','rock06','rock07','rock08','rock09','rock10']
r, rw, rh=img_load(random.choice(rlist))
r, rw, rh=img_load(random.choice(rlist))
rx = random.randint(0,w-rw)
ry = 30
rs=2

#------------------바위그리기함수------------
def rock_init():
    global r, rw, rh, rx, ry
    r, rw, rh=img_load(random.choice(rlist))
    rx = random.randint(0,w-rw)
    ry = 30
    rs = 2

#-----------------------------------
    
    




#----------------미사일 그리기------------------------------------

m, mw, mh = img_load('missile')
mx = px+pw/2-mw/2
my = py - mh
mlist= []   #여래개의 미사일을 담을 list



pad.blit(bg,(0,0)) #배경화면 그리기
pad.blit(p,(px,py))
pygame.display.update()

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type in [pygame.KEYDOWN]:
            if event.key == pygame.K_LEFT:
                ps = -5
            elif event.key == pygame.K_RIGHT:
                ps = +5
            elif event.key == pygame.K_SPACE: #미사일 발사
               
                mx = px+pw/2-mw/2    #연발시 미사일 위치 초기화
                my = py -mh
                mlist.append([mx, my])  #발사할 미사일을 리스트에 추가

        if event.type in [pygame.KEYUP]:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ps = 0

    px += ps            #for문 밖에 있음
    if px <0:
        px =0
    elif px >w-pw:
        px = w-pw


    pad.blit(bg,(0,0))
    pad.blit(p, (px,py))

    ry += rs
    pad.blit(r,(rx,ry)) #바위 X 좌표 random

    if ry > h:  #바위를 파괴하지 못하고 놓쳤을 경우
        miss +=1
        rock_init()

        rs += 1
        if rs >= 10:
            rs = 10 



    pad.blit(m,(mx,my)) #미사일 그리기



    pygame.display.update()
    clock.tick(60)
