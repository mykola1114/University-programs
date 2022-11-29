import random
import turtle
import time

def pointer(t, value_max, x_step, y_step,x_start=0, y_start=0):
    t.setpos(x_start+x_step, y_start+20 + value_max*y_step)

def sec_pointer(t, x_step, x_start=0, y_start=0):
    t.setpos(x_start+x_step, y_start-10)

def go_home(t, x_step, x_start=0, y_stop=0):
    t.clear()
    t.penup()
    t.setpos(x_start+x_step, y_stop)
    t.setheading(90)
    t.pendown()

def draw_one(color, t, value, x_step, y_step):
    t.fillcolor(color)
    t.begin_fill()
    t.fd(y_step * value)
    t.right(90)
    t.fd(x_step)
    t.right(90)
    t.fd(y_step * value)
    t.end_fill()


def bubble_sort(a, speed):
    turtle.title("Сортування Бульбашкою")
    turtle.delay(speed)
    n = len(a)
    dx = 20
    dy = 500
    x_start = -dx*n/2
    y_start = -dy/2
    max_value = max(a)
    border_t = turtle.Turtle()
    border_t.ht()
    border_t.penup()
    border_t.goto(x_start, y_start)
    border_t.pendown()
    border_t.fd(n*dx)
    point_t = turtle.Turtle()
    point_t.ht()
    point_t.penup()
    point_t.right(90)
    point_t.setpos(x_start+0.5*dx, y_start + 20 + dy)
    point_t.st()

    SECpoint_t = turtle.Turtle()
    SECpoint_t.ht()
    SECpoint_t.penup()
    SECpoint_t.left(90)
    SECpoint_t.setpos(x_start + 0.5*dx, y_start - 10)
    SECpoint_t.st()
    turtle_list = [turtle.Turtle() for _ in range(n)]
    for f, t in enumerate(turtle_list):
        t.ht()
        t.penup()
        t.speed(0)
        pointer(point_t, 1, (f + 1 / 2) * dx, dy, x_start, y_start)
        sec_pointer(SECpoint_t, (f + 1 / 2) * dx, x_start, y_start)
        go_home(t, f*dx, x_start, y_start)
        draw_one('grey', t, a[f]/max_value, dx, dy)


    for i in range(n-1):
        for j in range(n-i-1):
            pointer(point_t, 1, (j + 1 / 2) * dx, dy, x_start, y_start)
            sec_pointer(SECpoint_t, (j + 1 / 2) * dx, x_start, y_start)
            color = ['red', 'green']
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                sec_pointer(SECpoint_t, (j + 1 / 2) * dx, x_start, y_start)
                go_home(turtle_list[j], j*dx, x_start, y_start)
                draw_one(color[0], turtle_list[j], a[j] / max_value, dx, dy)

                if j+1 != n-i-1:
                    sec_pointer(SECpoint_t, (j + 1 + 1/2) * dx, x_start, y_start)
                    go_home(turtle_list[j + 1], (j + 1) * dx, x_start, y_start)
                    draw_one(color[1], turtle_list[(j + 1)], a[(j + 1)] / max_value, dx, dy)

        sec_pointer(SECpoint_t, (n - i - 1 + 1/2) * dx, x_start, y_start)
        go_home(turtle_list[n - i - 1], (n - i - 1) * dx, x_start, y_start)
        draw_one('blue', turtle_list[n - i - 1], a[(n - i - 1)] / max_value, dx, dy)

    pointer(point_t, 1, (0 + 1 / 2) * dx, dy, x_start, y_start)
    sec_pointer(SECpoint_t, (0 + 1/2) * dx, x_start, y_start)
    go_home(turtle_list[0], 0, x_start, y_start)
    draw_one('blue', turtle_list[0], a[0] / max_value, dx, dy)




def selection_sort(a, speed):
    turtle.title("Сортування Вибором")
    turtle.delay(speed)
    n = len(a)
    dx = 20
    dy = 500
    x_start = -dx * n/2
    y_start = -dy / 2
    max_value = max(a)
    border_t = turtle.Turtle()
    border_t.ht()
    border_t.penup()
    border_t.goto(x_start, y_start)
    border_t.pendown()
    border_t.fd(n * dx)
    point_t = turtle.Turtle()
    point_t.ht()
    point_t.penup()
    point_t.right(90)
    point_t.goto(x_start + 0.5*dx, y_start + 20 + dy)
    point_t.st()

    SECpoint_t = turtle.Turtle()
    SECpoint_t.ht()
    SECpoint_t.penup()
    SECpoint_t.left(90)
    SECpoint_t.setpos(x_start + 0.5*dx, y_start - 10)
    SECpoint_t.st()
    turtle_list = [turtle.Turtle() for _ in range(n)]
    for f, t in enumerate(turtle_list):
        t.ht()
        t.penup()
        t.speed(0)
        pointer(point_t, 1, (f + 1/2) * dx, dy, x_start, y_start)
        sec_pointer(SECpoint_t, (f + 1/2) * dx, x_start, y_start)
        go_home(t, f * dx, x_start, y_start)
        draw_one('grey', t, a[f] / max_value, dx, dy)

    for i in range(n):
        m, p = a[0], 0
        for j in range(n - i):
            sec_pointer(SECpoint_t, (j + 1 / 2) * dx, x_start, y_start)
            if a[j] > m:
                m, p = a[j], j

        a[p], a[n - i - 1] = a[n - i - 1], a[p]
        color = ['red', 'blue']
        pointer(point_t, 1, (p + 1/2) * dx, dy, x_start, y_start)
        go_home(turtle_list[p], p * dx, x_start, y_start)
        draw_one(color[0], turtle_list[p], a[p] / max_value, dx, dy)

        pointer(point_t, 1, (n - i - 1 + 1/2) * dx, dy, x_start, y_start)
        go_home(turtle_list[n - i - 1], (n - i - 1) * dx, x_start, y_start)
        draw_one(color[1], turtle_list[n - i - 1], a[n - i - 1] / max_value, dx, dy)




if __name__ == "__main__":
    random.seed(222)
    # Початковий список для сортування
    start_array = [random.randint(10, 60) for _ in range(15)]

    # Швидкість (0 - швидко, 50 - повільно)
    speed = 20

    # Сортування Бульбашкою
    bubble_sort(start_array.copy(), speed)

    time.sleep(2)
    turtle.clearscreen()
    turtle.resetscreen()

    # Сортування Вибором
    selection_sort(start_array.copy(), speed)

    turtle.done()






