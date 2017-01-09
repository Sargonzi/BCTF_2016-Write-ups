#!/usr/bin/env python
from turtle import *

def fill_rect(width, height, fill_color):
	color(fill_color)
	begin_fill()
	for distance in (width, height) * 2:
		forward(distance)
		right(90)
		end_fill()

def draw_flag():
	back(150)
fill_rect(300, 50, '#52D6FF')
fill_rect(300, -50, '#52D6FF')
left(-90); up(); forward(100); down();
fill_rect(50, -300, '#FFF700')
fill_rect(-50, -300, '#FFF700')