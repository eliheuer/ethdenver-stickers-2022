from drawBot import *

# Constants, these are the main "settings" for the image
WIDTH, HEIGHT, MARGIN, FRAMES = 2048, 1024, 128, 1
GRID_VIEW = True # Change this from "False" to "True" for a grid overlay

# Draws a grid
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
    fill(0.9)
    rect(-2, -2, WIDTH + 2, HEIGHT + 2)
    if GRID_VIEW:
        #grid()
        pass
    else:
        pass


# Draw main text
def draw_main_type():
    draw_background()
    fill(0)
    stroke(None)
    font("fonts/fraunces/Fraunces[SOFT,WONK,opsz,wght].ttf")
    for axis, data in listFontVariations().items():
        print((axis, data))
    fontSize(112.1)

    fontVariations(wght=900.0) # Range: 100.0 -> 900.0
    fontVariations(opsz=144.0) # Range: 9.0 -> 144.0
    fontVariations(SOFT=100.0) # Range: 0.0 -> 100.0 
    fontVariations(WONK=1.0)   # Range: 0,0 -> 1.0
    text("W", (MARGIN-5, MARGIN + (0*MARGIN)))
    text("e can build a more solarpunk world", (MARGIN+100, MARGIN + (0*MARGIN)))

    fontSize(3500)
    font("fonts/clipart/Clipart-Regular.ttf")
    text("A", (MARGIN, MARGIN + (1*MARGIN)))

# Build and save the image
if __name__ == "__main__":
    draw_main_type()
    # Save output, using the "--output" flag location
    saveImage("quote-003-solarpunk-world.png")
    # Print done in the terminal
    print("DrawBot: Done :-)")
