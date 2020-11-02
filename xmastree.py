#!/usr/bin/python3
from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
brown = (150,75,0)



def tree():
  G = green
  O = nothing
  B = brown
  logo = [
    O, O, O, G, G, O, O, O,
    O, O, O, G, G, O, O, O,
    O, O, G, G, G, G, O, O,
    O, O, G, G, G, G, O, O,
    O, G, G, G, G, G, G, O,
    G, G, G, G, G, G, G, G,
    O, O, O, B, B, O, O, O,
    O, O, O, B, B, O, O, O,
  ]
  return logo

def animated_trees():
  G = green
  O = nothing
  B = brown
  L = blue
  W = white
  R = red
  trees = [
    [
    O, O, O, G, G, O, O, O,
    O, O, O, G, G, O, O, O,
    O, O, G, L, G, G, O, O,
    O, O, G, G, G, G, O, O,
    O, G, G, G, W, G, R, O,
    W, G, R, G, G, G, G, G,
    O, O, O, B, B, O, O, O,
    O, O, O, B, B, O, O, O,
    ],
    [
    O, O, O, W, G, O, O, O,
    O, O, O, G, G, O, O, O,
    O, O, L, G, R, G, O, O,
    O, O, G, G, G, G, O, O,
    O, G, R, G, G, G, G, O,
    G, G, G, G, L, G, G, W,
    O, O, O, B, B, O, O, O,
    O, O, O, B, B, O, O, O,
    ],
    [
    O, O, O, G, R, O, O, O,
    O, O, O, G, G, O, O, O,
    O, O, G, G, G, G, O, O,
    O, O, G, G, G, L, O, O,
    O, G, R, G, G, G, R, O,
    G, G, G, G, L, G, G, G,
    O, O, O, B, B, O, O, O,
    O, O, O, B, B, O, O, O,
    ],
    [
    O, O, O, W, L, O, O, O,
    O, O, O, G, G, O, O, O,
    O, O, G, G, G, G, O, O,
    O, O, G, R, G, W, O, O,
    O, L, G, G, G, G, R, O,
    G, G, G, G, G, G, G, G,
    O, O, O, B, B, O, O, O,
    O, O, O, B, B, O, O, O,
    ],
    [
    O, O, O, G, L, O, O, O,
    O, O, O, G, G, O, O, O,
    O, O, G, R, G, G, O, O,
    O, O, G, G, L, G, O, O,
    O, G, R, G, G, G, G, O,
    W, G, G, G, G, G, G, W,
    O, O, O, B, B, O, O, O,
    O, O, O, B, B, O, O, O,
    ],
    [
    O, O, O, R, G, O, O, O,
    O, O, O, G, G, O, O, O,
    O, O, R, G, G, W, O, O,
    O, O, G, G, G, G, O, O,
    O, G, G, G, L, G, R, O,
    R, G, W, G, G, G, G, G,
    O, O, O, B, B, O, O, O,
    O, O, O, B, B, O, O, O,
    ],
    [
    O, O, O, G, G, O, O, O,
    O, O, O, G, W, O, O, O,
    O, O, G, G, G, L, O, O,
    O, O, G, R, G, G, O, O,
    O, G, G, G, G, R, G, O,
    G, L, W, G, G, G, W, G,
    O, O, O, B, B, O, O, O,
    O, O, O, B, B, O, O, O,
    ],
    [
    O, O, O, L, G, O, O, O,
    O, O, O, G, G, O, O, O,
    O, O, L, G, R, G, O, O,
    O, O, G, G, G, G, O, O,
    O, G, R, G, W, G, G, O,
    W, G, G, L, G, G, R, G,
    O, O, O, B, B, O, O, O,
    O, O, O, B, B, O, O, O,
    ],
    [
    O, O, O, G, R, O, O, O,
    O, O, O, G, G, O, O, O,
    O, O, L, G, R, G, O, O,
    O, O, G, G, G, W, O, O,
    O, G, R, G, L, G, R, O,
    G, G, G, W, G, G, G, G,
    O, O, O, B, B, O, O, O,
    O, O, O, B, B, O, O, O,
    ],
    [
    O, O, O, W, G, O, O, O,
    O, O, O, G, G, O, O, O,
    O, O, G, G, G, W, O, O,
    O, O, R, G, L, G, O, O,
    O, G, G, W, G, R, G, O,
    L, G, G, G, G, G, R, G,
    O, O, O, B, B, O, O, O,
    O, O, O, B, B, O, O, O,
    ]
  ]
  return trees


images = animated_trees()
count = 0

while True: 
    curimage=images[count% len(images)]
    s.set_pixels(curimage)
    time.sleep(.75)
    count += 1
