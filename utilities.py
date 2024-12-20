import pygame, sys, os
from os.path import join

from pygame.math import Vector2 as vector

screen_width = 800
screen_height = 600

rect_size = 30
rect_y = screen_height - rect_size * 2
rect_x = screen_width // 2 - rect_size // 2

e_pos_x = rect_size
e_pos_y = rect_size

player_bolt_speed = 750
enemy_bolt_speed = 500
bullet_width = 5


