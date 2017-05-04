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

        def __init__(self, top_left_pt, size=SIZE, shape_attributes=SHAPE_ATTRIBUTES, color=None, updating=False):
            self.top_left_point = top_left_pt
            self.shape_attributes = dict(shape_attributes)
            self.size = size
            if color:
                self.set_color(color)
            self.updating = updating
        
        def set_color(self, color):
            self.shape_attributes["fill_color"] = color
            
        def update_location(self, new_pos, edges=[Constants.GRID_HEIGHT]):
            check_bottom_edge = new_pos[1] + 1

            if filter(lambda x: check_bottom_edge > x, edges):
                self.updating = False
                
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
            
            if self.updating:
                (x, y) = self.top_left_point
                self.update_location((x, y+.05))
class BlockMap:
    
    def __init__(self):
        self.block_map = self.init_block_map()
        for key in list(self.block_map):
            self.block_map[key] = self.init_block_map()
        print self.block_map

    def init_block_map(self):
        block_map = {}
        for x in range(Constants.GRID_WIDTH):
            block_map[x] = {}
        return block_map

    def update(self, new_block):
#        self.block_map[str(new_block.top_left_point[0]) + "_" + str(new_block.top_left_point[1])] = new_block
        self.block_map[str(new_block.top_left_point[0])][str(new_block.top_left_point[1])] = new_block
     
    def add_all(self, block_list):
        map(self.update, block_list)

    def block_list(self):
        return self.block_map.values()
# END OF API

bm = BlockMap()

sqr_default = Rect.Square((1,1))
sqr_blue = Rect.Square((2,2), color="Blue")


bm.add_all([sqr_default, sqr_blue])
bm.add_all([ Rect.Square((i,i), updating=True) for i in range(Constants.GRID_WIDTH)])

                               
def draw(canvas):
    for sqr in bm.block_list():
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
