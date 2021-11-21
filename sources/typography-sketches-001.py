from drawBot import *

# Constants, these are the main "settings" for the image
WIDTH, HEIGHT, MARGIN, FRAMES = 2048, 2048, 128, 1
GRID_VIEW = False # Change this from "False" to "True" for a grid overlay

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
    for y in range(29):
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
    else:
        pass


# Draw main text
def draw_main_type():
    draw_background()
    fill(1)
    stroke(None)
    font("fonts/fraunces/Fraunces-Italic[SOFT,WONK,opsz,wght].ttf")
    for axis, data in listFontVariations().items():
        print((axis, data))
    fontSize(96)

    fontVariations(wght=900.0) # Range: 100.0 -> 900.0
    fontVariations(opsz=144.0) # Range: 9.0 -> 144.0
    fontVariations(SOFT=100.0) # Range: 0.0 -> 100.0 
    fontVariations(WONK=1.0)   # Range: 0,0 -> 1.0
    text("Ethereum is Solarpunk", (MARGIN, MARGIN + (13*MARGIN)))

    fontVariations(wght=100.0) # Range: 100.0 -> 900.0
    fontVariations(opsz=9.0)   # Range: 9.0 -> 144.0
    fontVariations(SOFT=100.0) # Range: 0.0 -> 100.0 
    fontVariations(WONK=1.0)   # Range: 0,0 -> 1.0
    text("Ethereum is Solarpunk", (MARGIN, MARGIN + (12*MARGIN)))

    fontVariations(wght=900.0) # Range: 100.0 -> 900.0
    fontVariations(opsz=144.0) # Range: 9.0 -> 144.0
    fontVariations(SOFT=100.0) # Range: 0.0 -> 100.0 
    fontVariations(WONK=1.0)   # Range: 0,0 -> 1.0
    text("Ethereum is Solarpunk", (MARGIN, MARGIN + (11*MARGIN)))

    font("fonts/ferrite-core/FerriteCoreDX-Black.ttf")
    text("Take the Green Pill", (MARGIN, MARGIN + (10*MARGIN)))

    font("fonts/ferrite-core/FerriteCoreDX-Black.ttf")
    text("Regen > Degen", (MARGIN, MARGIN + (9*MARGIN)))

    font("fonts/bobo/Bobo.ttf")
    text("TAKE THE GREEN PILL", (MARGIN, MARGIN + (8*MARGIN)))

    font("fonts/rompacta/Rompacta.ttf")
    text("TAKE THE GREEN PILL", (MARGIN, MARGIN + (7*MARGIN)))

    font("fonts/fraunces/Fraunces[SOFT,WONK,opsz,wght].ttf")
    fontVariations(wght=900.0) # Range: 100.0 -> 900.0
    fontVariations(opsz=144.0) # Range: 9.0 -> 144.0
    fontVariations(SOFT=70.0) # Range: 0.0 -> 100.0 
    fontVariations(WONK=1.0)   # Range: 0,0 -> 1.0
    text("Ethereum was not made to make you rich.", (MARGIN, MARGIN + (6*MARGIN)))
    text("Ethereum was made to make you free.", (MARGIN, MARGIN + (5.2*MARGIN)))

    font("fonts/print-shope/PrintShope.ttf")
    text("TAKE THE GREEN PILL", (MARGIN, MARGIN + (4*MARGIN)))

    font("fonts/fraunces/Fraunces-Italic[SOFT,WONK,opsz,wght].ttf")
    text("Take me to the Quadratic Lands", (MARGIN, MARGIN + (3*MARGIN)))

    font("fonts/bach/Bach.ttf")
    text("TAKE me to the Quadratic Lands", (MARGIN, MARGIN + (2*MARGIN)))

    font("fonts/bachlin/Bachlin.ttf")
    text("TAKE me to the Quadratic Lands", (MARGIN, MARGIN + (1*MARGIN)))

# Build and save the image
if __name__ == "__main__":
    draw_main_type()
    # Save output, using the "--output" flag location
    saveImage("typography-sketches-001.png")
    # Print done in the terminal
    print("DrawBot: Done :-)")
