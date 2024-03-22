# 거북이 그래픽 모듈 사용  - 한줄 주석

import turtle  # turtle 모듈을 내 프로그램에서 사용
#import turtle as t # 별명을 정해줌

turtle.shape("turtle") #circle    arrow   turtle  square


#삼각형 120 사각형 90  오각형 72 육각형 60 팔각형 45



#팔각형 그리기
turtle.color("purple")
turtle.begin_fill()
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.left(45)
turtle.end_fill()

#육각형 그리기

turtle.color("green")
turtle.begin_fill()
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.end_fill()

#오각형 그리기
turtle.color("yellow")
turtle.begin_fill()
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.end_fill()
#사각형 그리기
turtle.color("orange")
turtle.begin_fill()
turtle.forward(100)
turtle.left(360/4)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.end_fill()


#삼각형 그리기
turtle.color("red")
turtle.begin_fill()
turtle.forward(100)
turtle.left(360/3)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.end_fill()




