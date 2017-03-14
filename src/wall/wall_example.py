import simplegui, time, random

WINDOW_WIDTH = 500
WINDOW_HEIGHT = WINDOW_WIDTH
GLOBAL_DEFAULT_SQUARE_SIZE = 25

GRID_WIDTH = WINDOW_WIDTH / GLOBAL_DEFAULT_SQUARE_SIZE
GRID_HEIGHT = GRID_WIDTH

DEFAULT_FLOOR_HEIGHT = 10

class Wall:
    
    def __init__(self, active_blocks, width=DEFAULT_FLOOR_HEIGHT):
        self.floor = self.Floor(range(3)).as_wall()
        
    def draw_me(self, canvas):
        self.floor.draw_me(canvas)
    

    class Floor:

        def __init__(self, active_blocks, height=DEFAULT_FLOOR_HEIGHT):
            self.height = height
            self.blocks = self.init_blocks(active_blocks)

        def init_blocks(self, active_blocks):
            blocks = []
            for i in active_blocks:
                blocks.append(
                    self.Rect.Square((i,GRID_HEIGHT - self.height))
                )
            return blocks
        
        def as_wall(self):
            for block in self.blocks:
                block.transpose()
            return self

        def draw_me(self, canvas):
            for block in self.blocks:
                block.draw_me(canvas)

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
                    "line_width": 1,
                    "line_color": 'Green',
                    "fill_color": 'Orange'
                }

                SHAPE_ATTRIBUTES = DEFAULT_SQUARE_DRAW_ATTRIBUTES
                SIZE = GLOBAL_DEFAULT_SQUARE_SIZE

                def __init__(self, top_left_pt, size=SIZE, shape_attributes=SHAPE_ATTRIBUTES):
                    self.top_left_point = top_left_pt
                    self.shape_attributes = shape_attributes
                    self.size = size
                    
                def transpose(self):
                    pt = self.top_left_point
                    self.top_left_point = (pt[1], pt[0])

                def draw_me(self, canvas):
                    size = self.size
                    (x,y) = self.top_left_point
                    (x,y) = x*size, y*size
                    canvas.draw_polygon(Wall.Floor.Rect.rect_coords(size, size, (x,y)),
                        self.shape_attributes["line_width"],
                        self.shape_attributes["line_color"],
                        self.shape_attributes["fill_color"]
                    )

floor = Wall(range(20) + range(6,9))










def draw(canvas):
    floor.draw_me(canvas)

class Graphics:
    
    def __init__(self):
        frame = simplegui.create_frame("Home", WINDOW_WIDTH, WINDOW_HEIGHT)
        frame.set_canvas_background("Silver")
        frame.set_draw_handler(draw)
        frame.start()
Graphics()
              
