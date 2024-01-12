# Gruficlath (Trenton Burnes) 2024
# Released to public domain

import turtle as t
import random as r

class SnowConfig:
    def __init__(
            self,
            x_range: list = [-300, 300],
            height: float = 300,
            fall_speed: list = [1, 10],
            wind_speed: list = [-10, 10],
            ground_height: float = -300,
            stamp: bool = True
            ):
        self.x_range = x_range
        self.height = height
        self.fall_speed = fall_speed
        self.wind_speed = wind_speed
        self.ground_height = ground_height
        self.stamp = stamp

def snow_setup(
        config: SnowConfig,
        count: int = 10,
        color: str = 'white',
        shape: str = 'circle',
        size: float = 1
        ):
    snowflakes = []
    for i in range(count):
        flake = t.Turtle(shape)
        flake.color(color)
        flake.speed(0)
        flake.penup()
        flake.shapesize(size)
        flake.teleport(r.randint(config.x_range[0], config.x_range[1]), config.height)
        snowflakes.append(flake)
    return snowflakes

def snow_step(snowflakes: list, config: SnowConfig, step_amount: int = 1):
    for step in range(step_amount):
        for flake in snowflakes:
            speed_x = r.randint(config.wind_speed[0], config.wind_speed[1])
            speed_y = r.randint(config.fall_speed[0], config.fall_speed[1])
            new_x = flake.xcor() - speed_x
            new_y = flake.ycor() - speed_y
            flake.teleport(new_x, new_y)
            if flake.ycor() < config.ground_height:
                if config.stamp:
                    flake.stamp()
                flake.teleport(r.randint(config.x_range[0], config.x_range[1]), config.height)

def snow_end(snowflakes: list):
    for flake in snowflakes:
        flake.stamp()
    snowflakes.clear()
