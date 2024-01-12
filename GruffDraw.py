# Gruficlath (Trenton Burnes) 2024
# Released to public domain

import turtle as t

def draw_triangle(
        turtle: t.Turtle, 
        x_pos: float = 0, 
        y_pos: float = 0, 
        size: float = 50, 
        color: str = 'black', 
        fill: bool = True
        ):
    turtle.teleport(x_pos, y_pos)
    turtle.fillcolor(color)
    turtle.color(color)
    if fill:
        turtle.begin_fill()
    turtle.rt(60)
    turtle.fd(size)
    for i in range(2):
        turtle.rt(120)
        turtle.fd(size)
    if fill:
        turtle.end_fill()
    turtle.setheading(0)

def draw_rectangle(
        turtle: t.Turtle,
        x_pos: float = 0,
        y_pos: float = 0,
        x_size: float = 50,
        y_size: float = 50,
        color: str = 'black',
        fill: bool = True
        ):
    turtle.teleport(x_pos, y_pos)
    turtle.fillcolor(color)
    turtle.color(color)
    if fill:
        turtle.begin_fill()
    for i in range(4):
        if i % 2 == 1:
            turtle.fd(y_size)
        else:
            turtle.fd(x_size)
        turtle.rt(90)
    if fill:
        turtle.end_fill()
    turtle.setheading(0)

def draw_circle(
        turtle: t.Turtle,
        x_pos: float = 0,
        y_pos: float = 0,
        size: float = 50,
        color: str = 'black',
        fill: bool = True,
        resolution: int = 25
        ):
    resolution = min(resolution, 360)
    resolution = max(resolution, 3)
    turtle.teleport(x_pos, y_pos)
    turtle.fillcolor(color)
    turtle.color(color)
    if fill:
        turtle.begin_fill()
    for i in range(resolution):
        turtle.fd(size / 500 * (360 / resolution))
        turtle.right(360 / resolution)
    if fill:
        turtle.end_fill()
    turtle.setheading(0)

def draw_star(
        turtle: t.Turtle,
        x_pos: float = 0,
        y_pos: float = 0,
        size: float = 50,
        color: str = 'black',
        fill: bool = True
        ):
    turtle.teleport(x_pos, y_pos)
    turtle.fillcolor(color)
    turtle.color(color)
    if fill:
        turtle.begin_fill()
    for i in range(5):
        turtle.rt(144)
        turtle.fd(size)
        turtle.lt(72)
        turtle.fd(size)
    if fill:
        turtle.end_fill()
    turtle.setheading(0)

def write(
        turtle: t.Turtle,
        x_pos: float = 0,
        y_pos: float = 0,
        size: int = 50,
        color: str = 'black',
        text: str = 'Hello!'
        ):
    turtle.teleport(x_pos, y_pos)
    turtle.fillcolor(color)
    turtle.color(color)
    turtle.write(text, False, 'center', ("FiraCode Nerd Font", size, "normal"))
