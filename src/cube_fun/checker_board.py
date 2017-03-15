# Need to set a global constant
Constants.GLOBAL_DEFAULT_SQUARE_SIZE = 50
##

sqrs = []
for i in range(8):
    for j in range(8):
        sqr = Rect.Square((i + 1, j + 1), color="Black")
        
        if i % 2 == j % 2:
            sqr.set_color("Red")

        sqrs.append(sqr)
                               
def draw(canvas):
    map(lambda x: x.draw_me(canvas), sqrs)
