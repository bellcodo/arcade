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
            
        def draw_me(self, canvas):
            size = self.size
            (x,y) = self.top_left_point
            (x,y) = x*size, y*size
            canvas.draw_polygon(Rect.rect_coords(size, size, (x,y)),
                self.shape_attributes["line_width"],
                self.shape_attributes["line_color"],
                self.shape_attributes["fill_color"]
            )
#

sqrs = []

characters = {
    'a': [['0', '0', '1', '1', '0', '0', '0', '0'], ['0', '0', '0', '1', '0', '0', '0', '0'], ['0', '0', '0', '1', '0', '0', '0', '0'], ['0', '0', '1', '0', '1', '0', '0', '0'], ['0', '1', '1', '0', '1', '0', '0', '0'], ['0', '1', '0', '0', '0', '1', '0', '0'], ['0', '1', '1', '1', '1', '1', '0', '0'], ['0', '1', '0', '0', '0', '1', '0', '0'], ['1', '1', '1', '0', '1', '1', '1', '0'], ['0', '0', '0', '0', '0', '0', '0', '0']]
  , 'b': [['1', '1', '1', '1', '1', '1', '0', '0'], ['0', '1', '0', '0', '0', '0', '1', '0'], ['0', '1', '0', '0', '0', '0', '1', '0'], ['0', '1', '0', '0', '0', '0', '1', '0'], ['0', '1', '1', '1', '1', '1', '0', '0'], ['0', '1', '0', '0', '0', '0', '1', '0'], ['0', '1', '0', '0', '0', '0', '1', '0'], ['0', '1', '0', '0', '0', '0', '1', '0'], ['1', '1', '1', '1', '1', '1', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0']]
  , 'c': [['0', '0', '1', '1', '1', '1', '0', '0'], ['0', '1', '0', '0', '0', '0', '1', '0'], ['1', '0', '0', '0', '0', '0', '0', '0'], ['1', '0', '0', '0', '0', '0', '0', '0'], ['1', '0', '0', '0', '0', '0', '0', '0'], ['1', '0', '0', '0', '0', '0', '0', '0'], ['1', '0', '0', '0', '0', '0', '0', '0'], ['0', '1', '0', '0', '0', '0', '1', '0'], ['0', '0', '1', '1', '1', '1', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0']]
  , 't': [['1', '1', '1', '1', '1', '1', '1', '0'], ['1', '0', '0', '1', '0', '0', '1', '0'], ['0', '0', '0', '1', '0', '0', '0', '0'], ['0', '0', '0', '1', '0', '0', '0', '0'], ['0', '0', '0', '1', '0', '0', '0', '0'], ['0', '0', '0', '1', '0', '0', '0', '0'], ['0', '0', '0', '1', '0', '0', '0', '0'], ['0', '0', '0', '1', '0', '0', '0', '0'], ['0', '0', '1', '1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0']]
  , 'u': [['1', '1', '1', '0', '1', '1', '1', '0'], ['0', '1', '0', '0', '0', '1', '0', '0'], ['0', '1', '0', '0', '0', '1', '0', '0'], ['0', '1', '0', '0', '0', '1', '0', '0'], ['0', '1', '0', '0', '0', '1', '0', '0'], ['0', '1', '0', '0', '0', '1', '0', '0'], ['0', '1', '0', '0', '0', '1', '0', '0'], ['0', '1', '0', '0', '0', '1', '0', '0'], ['0', '0', '1', '1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0']]
}


def key_handler(key):
    global sqrs
    input_char = chr(key + 32)
    print input_char
    if input_char in characters:
        sqrs = []
        a_t = characters[input_char]    
        for row in range(len(a_t)):
            for char in range(len(a_t[row])):
                #print "At pos: (%i,%i) is the value: %s" % (row, char, a_t[row][char])
                if int(a_t[row][char]):
                    sqrs.append(
                        Rect.Square((char + 5,row + 5))
                    )
                    print sqrs
                               
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
        frame.set_keydown_handler(key_handler)
        frame.start()        
#              
Graphics()
