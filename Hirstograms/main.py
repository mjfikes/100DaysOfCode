import turtle
import colorgram
import requests
from io import BytesIO
import random

IMAGE_URL = 'https://www.woodlandtrust.org.uk/media/48882/carrifran_rowan-19-aiden-maccormick.jpg'

CANVAS_W = 1000
CANVAS_H = 800
turtle.colormode(255)
damien = turtle.Turtle()
screen = turtle.Screen()
screen.canvheight = CANVAS_H
screen.canvwidth = CANVAS_W

def extract_colors(url,n_colors):
    rgb_list = []
    image = requests.get(url)

    if image.status_code == 200:
        dot_colors = colorgram.extract(BytesIO(image.content), n_colors)
        for c in dot_colors:
            c_r = c.rgb.r
            c_g = c.rgb.g
            c_b = c.rgb.b
            c_rgb = (c_r, c_g, c_b)
            rgb_list.append(c_rgb)
        return rgb_list
    else:
        return [(0, 0, 0)]


def dot_grid(turtle, grid_x, grid_y):
    turtle.speed(0)
    curr_y = -400
    turtle.pu()
    grid_height = CANVAS_H//grid_x
    grid_width = CANVAS_W//grid_y
    turtle.setx(-500)
    turtle.sety(curr_y)
    print(turtle.position)
    for y in range(grid_y):
        for x in range(grid_x):
            turtle.pd()
            turtle.dot(20, random.choice(palette))
            turtle.pu()
            turtle.fd(grid_width)
        turtle.setx(-500)
        curr_y += grid_height
        turtle.sety(curr_y)


palette = extract_colors(IMAGE_URL, 25)
print(palette)
dot_grid(damien, 25, 25)




screen.exitonclick()