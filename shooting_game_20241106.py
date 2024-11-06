import pygame
import sys
import random
pygame.init()

w=480
h=640

white = (255,255,255)
red = (255,0,0) 

hit = 0
miss = 0

pad = pygame.display.set_mode((w,h)) #화면 생성
pygame.display.set_caption("Shooting Game") #제목 설정

##--------------게임오버---------------
def gameover():
    global pad, run
    write('Game Over', 70,200,red,60)
    gameover_sound.play()
    pygame.display.update()
    run = False



#-------사운드 로드------------#################

pygame.mixer.music.load('bgm.wav') #배경음악 로드
pygame.mixer.music.play(-1) #배경음악 재생, -1이면 무한재생
mis_sound = pygame.mixer.Sound('missile.wav')
exp_sound = pygame.mixer.Sound('explosion.wav')
gameover_sound = pygame.mixer.Sound('gameover.wav')

################################


#--------------------이미지로드 함수--------------------
def img_load(obj):
    img = pygame.image.load(str(obj)+'.png')
    img_size = img.get_rect().size
    return img, img_size[0], img_size[1]
#------------------------------------------------------


#------------------쓰기 함수--------
def write(string, a,b,color,size = 20):
    global pad
    font = pygame.font.Font('NanumGothic.ttf',size)
    text = font.render(string,False,color)
    pad.blit(text,(a,b))
#----------------------------------

bg= img_load('background')[0]

p, pw,ph = img_load('ironman') #전투기이미지
px = w * 0.4 #전투기의 초기 x위치
py = h * 0.9 #전투기의 초기 y위치

ps=0 #전투기 스피드



#10.8 4교시_1.-------------운석 그리기-------

rlist = ['rock01','rock02','rock03','rock04','rock05',
         'rock06','rock07','rock08','rock09','rock10']
r,rw,rh=img_load(random.choice(rlist))

rx = random.randint(0,w-rw)
ry=30
rs=2

#------------바위그리기 함수 --------
def rock_init():
    global r, rw, rh, rx, ry
    r,rw,rh=img_load(random.choice(rlist))
    rx = random.randint(0,w-rw)
    ry =30
    rs = 2
#---------------------------- 
    



#--------미사일 그리기--------------
m, mw, mh = img_load('missile')
mx = px+pw/2-mw/2
my = py - mh
mlist = []

exp = img_load('explosion')[0]

clock = pygame.time.Clock()

run = True

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type in [pygame.KEYDOWN]:
            if event.key == pygame.K_LEFT:
                    ps = -5
            elif event.key == pygame.K_RIGHT:
                ps = +5
            elif event.key == pygame.K_SPACE:
                mis_sound.play() ##################
                mx = px+pw/2-mw/2
                my = py - mh
                mlist.append([mx,my])
                
            
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
    pad.blit(r,(rx, ry)) #바위 x 좌표 random

    if ry > h: #바위를 파괴하지 못하고 놓쳤을 경우
        miss += 1
        rock_init()

        rs += 0.02
        if rs >= 10:
            rs =10
    #전투기와 운석 충돌상황
    if (py<ry+rh) and (px <rx +rw) and(px+pw > rx):
        miss += 1 
        pad.blit(exp,(rx,ry))
        exp_sound.play()##################
        rock_init()
        
        rs += 0.02   #전투기와 운석이 부딪히면 운석 떨어지는 속도 빨라지게
        if rs >= 10:
            rs = 10
            


            

    #미사일 발사하기
    if len(mlist) != 0:
        for mis in mlist:
            mis[1] -= 10
            #운석과 미사일 충돌상황
            if (mis[1] < ry+rh) and (mis[0] < rx+rw) and (mis[0] +mw > rx):
                pad.blit(exp,(rx,ry))
                exp_sound.play()##################
                mlist.remove(mis)
                hit +=1
                pad.blit(exp,(rx,ry))
                rock_init()
            elif mis[1] <-50:  #-미사일 꼬리가 화면밖으로 나가면 미사일 삭제
                mlist.remove(mis) #미사일 삭제

            pad.blit(m,(mis[0],mis[1]))


    #----글씨 쓰기------------
    hit_text ='Scores : '+str(hit)
    write(hit_text, 10, 10,white)
    
    miss_text = 'Miss : '+str(miss)
    write(miss_text,400,10,red)

    if miss == 3:
        gameover()
   

            
    pygame.display.update()
    clock.tick(60)
