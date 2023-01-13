import turtle
#6번째 코드 : 규칙없어서 안됨
#7번째 코드
def set_orange(n):
    t = turtle.Turtle()
    t.color('orange')
    t.begins_fill()
    for i in range(n):
        t.forward(100)
        t.left(90)
    t.end_fill()

    t.penup()
    t.goto(10, 30)
    t.pendown()
    t.color("white")
    t.begin_fill()

    for i in range(n):
        t.forward(80)
        t.left(90)
    t.end_fill()

#8번쨰코드
def set_grey(n):
    t = turtle.Turtle()
    t.color('grey')
    t.begin_fill()
    t.forward(100)
    t.left(90)
    for i in range(3):
        t.forward(100)
        t.right(90)
        t.forward(100)
        t.left(90)
        t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.end_fill()
#9번째 코드
def set_grey_2(n):
    t = turtle.Turtle()

    t.color("grey")
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.right(90)
    t.forward(100)
    t.end_fill()
#10번쨰 코드 : 그대로 치면 됨 요약할 게 없음

n = input("vertex num : ")
set_orange(n)
set_grey(n)
set_grey_2(n)
set_10(n)




