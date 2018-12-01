import pygame
import sys
import random


def randomize():
    sett = random.randint(200, 400)
    randoming = random.randint(0, 200)
    speed = random.randint(1, 5)
    return sett, randoming, speed