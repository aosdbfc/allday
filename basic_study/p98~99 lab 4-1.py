import turtle
t=turtle.Turtle()
t. shape("turtle")

t. penup()
t. goto(100, 100)
t. write(" 다문화학과 여러분~!!!")

t.goto(100,0)
t. write(" 중간고사 모두 파이팅 입니다! ")

t. goto(100,-100)
t. write(" 교수에게 자랑하고 싶은 거 있음 얼마든지 해 ~")

t.goto(0,0)
t.pendown()

s = turtle.textinput("" , "숫자를 입력하시오.")
n = int(s)

if n > 0 :
    t.goto(100,100)
if n == 0:
    t. goto(100,0)
if n < 0 :
    t. goto(100, -100)

turtle.done() 
