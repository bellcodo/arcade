sqrs = []
for i in range(8):
    for j in range(8):
        sqr = Rect.Square((i,j))
        if j % 2 == 0 and i % 2 == 0:
            sqr.set_color("Red")
        elif j % 2 != 0 and i % 2 != 0:
            sqr.set_color("Red")
        else:
            sqr.set_color("Black")

        sqrs.append(sqr)
                               
def draw(canvas):
    map(lambda x: x.draw_me(canvas), sqrs)
