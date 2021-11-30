# | drawbot.com | use drawbot-skia on GNU+Linux systems
from drawBot import *


# Constants, these are the main "settings" for the image
WIDTH = 2048
HEIGHT = 1024
MARGIN = 128
FRAMES = 1
GRID_VIEW = True # Change this from "False" to "True" for a grid overlay


# Draw a grid if the constant "GRID_VIEW" is set to "True"
def grid():
    stroke(1, 0, 0, 0.75)
    strokeWidth(2)
    STEP_X, STEP_Y = 0, 0
    INCREMENT_X, INCREMENT_Y = MARGIN / 2, MARGIN / 2
    rect(MARGIN, MARGIN, WIDTH - (MARGIN * 2), HEIGHT - (MARGIN * 2))
    for x in range(29):
        polygon((MARGIN + STEP_X, MARGIN), (MARGIN + STEP_X, HEIGHT - MARGIN))
        STEP_X += INCREMENT_X
    for y in range(12):
        polygon((MARGIN, MARGIN + STEP_Y), (WIDTH - MARGIN, MARGIN + STEP_Y))
        STEP_Y += INCREMENT_Y
    polygon((WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
    polygon((0, HEIGHT / 2), (WIDTH, HEIGHT / 2))


# Draw the page/frame and a grid if "GRID_VIEW" is set to "True"
def draw_background():
    newPage(WIDTH, HEIGHT)
    fill(0)
    rect(-2, -2, WIDTH + 2, HEIGHT + 2)
    if GRID_VIEW:
        grid()
        pass
    else:
        pass


def draw_image():
    draw_background()
    fill(0.95)
    stroke(None)
    #font("fonts/ferrite-core/FerriteCoreDX-Display.ttf")
    font("fonts/fraunces/Fraunces[SOFT,WONK,opsz,wght].ttf")
    for axis, data in listFontVariations().items():
        print((axis, data))
    fontSize(214)

    font("fonts/fraunces/Fraunces-Italic[SOFT,WONK,opsz,wght].ttf")
    fontVariations(wght=900.0) # Range: 100.0 -> 900.0
    fontVariations(opsz=144.0) # Range: 9.0 -> 144.0
    fontVariations(SOFT=100.0) # Range: 0.0 -> 100.0 
    fontVariations(WONK=1.0)   # Range: 0,0 -> 1.0
    text("W", (MARGIN-28, MARGIN + (3.5*MARGIN)))
    text("e", (MARGIN+165, MARGIN + (3.5*MARGIN)))
    text("can", (MARGIN+290, MARGIN + (3.5*MARGIN)))
    text("sla", (MARGIN+690, MARGIN + (3.5*MARGIN)))
    text("y", (MARGIN+990, MARGIN + (3.5*MARGIN)))
    fntVariations(WONK=1.0)   # Range: 0,0 -> 1.0
    text("y", (MARGIN+990, MARGIN + (3.5*MARGIN)))
    #text("slay Moloch", (MARGIN+690, MARGIN + (3.5*MARGIN)))
    #text("We can slay Moloch", (MARGIN-28, MARGIN + (3.5*MARGIN)))

    fontSize(1000)
    font("fonts/clipart/Clipart-Regular.ttf")
    #text("A", (MARGIN, MARGIN + (5*MARGIN)))

# Build and save the image
if __name__ == "__main__":
    draw_image()
    saveImage("quote-009-we-can-slay-moloch.png")
    print("DrawBot: Done :-)")
