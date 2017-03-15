# Depends on src/geometric/square_example.py

sqr_default = Rect.Square((1,1))
sqr_blue = Rect.Square((2,2), color="Blue")

sqrs = []
for i in range(Constants.GRID_WIDTH):
    sqr = Rect.Square((i,i))
    if i % 2 == 0:
        sqr.set_color("Blue")
    sqrs.append(sqr)
                               
def draw(canvas):
    map(lambda x: x.draw_me(canvas), sqrs)
