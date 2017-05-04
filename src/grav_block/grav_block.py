# Place holder
import simplegui, time, random

class Constants:

    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = WINDOW_WIDTH
    GLOBAL_DEFAULT_SQUARE_SIZE = 25

    GRID_WIDTH = WINDOW_WIDTH / GLOBAL_DEFAULT_SQUARE_SIZE
    GRID_HEIGHT = GRID_WIDTH
class Rect:
    
    def rect_coords (length, height, startpos = (0, 0)) :
        x = startpos[0]
        y = startpos[1]
        return [
            (x, y),
            (x, y + height),
            (x + length, y + height),
            (x + length, y)  
        ] 

    class Square:
        
        DEFAULT_SQUARE_DRAW_ATTRIBUTES = {
            "line_width": 2,
            "line_color": 'White',
            "fill_color": 'Orange'
        }        

        SHAPE_ATTRIBUTES = DEFAULT_SQUARE_DRAW_ATTRIBUTES
        SIZE = Constants.GLOBAL_DEFAULT_SQUARE_SIZE

        def __init__(self, top_left_pt, size=SIZE, shape_attributes=SHAPE_ATTRIBUTES, color=None):
            self.top_left_point = top_left_pt
            self.shape_attributes = dict(shape_attributes)
            self.size = size
            if color:
                self.set_color(color)
        
        def set_color(self, color):
            self.shape_attributes["fill_color"] = color
            
        def update_location(self, new_pos):
            self.top_left_point = new_pos
            
        def draw_me(self, canvas):
            size = self.size
            (x,y) = self.top_left_point
            (x,y) = x*size, y*size
            canvas.draw_polygon(Rect.rect_coords(size, size, (x,y)),
                self.shape_attributes["line_width"],
                self.shape_attributes["line_color"],
                self.shape_attributes["fill_color"]
            )
            (x, y) = self.top_left_point
            self.update_location((x, y+.05))
#

sqrs = []

sqr_default = Rect.Square((1,1))
sqr_blue = Rect.Square((2,2), color="Blue")

sqrs.extend([sqr_default, sqr_blue])

                               
def draw(canvas):
    for sqr in sqrs:
        sqr.draw_me(canvas)

class Graphics:   
    WINDOW_WIDTH = Constants.WINDOW_WIDTH
    WINDOW_HEIGHT = Constants.WINDOW_HEIGHT
    
    def __init__(self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT):
        frame = simplegui.create_frame("Home", width, height)
        frame.set_canvas_background("Silver")
        frame.set_draw_handler(draw)
        frame.start()        
#              
Graphics()
