import turtle
import keyboard

muslim= turtle.Turtle()

while True:
    if keyboard.is_pressed("w"):
        muslim.forward(10)
    if keyboard.is_pressed("s"):
        muslim.back(10)
    if keyboard.is_pressed("a"):
        muslim.left(5)
    if keyboard.is_pressed("d"):
        muslim.right(5)
    if keyboard.is_pressed("esc"):
        break