import turtle
xc, yc, r, x, y = map(int, input().split())
turtle.penup()
turtle.goto(xc, yc - r)
turtle.pendown()
turtle.circle(r)
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.dot(10, 'red')
turtle.penup()
turtle.goto(xc - r, yc - r - 20)
turtle.pendown()
if x ** 2 + y ** 2 < r ** 2:
    turtle.write('Точка внутри окружности')
elif x ** 2 + y ** 2 > r ** 2:
    turtle.write('Точка вне окружности')
elif x ** 2 + y ** 2 == r ** 2:
    turtle.write('Точка лежит на окружности')
turtle.done()