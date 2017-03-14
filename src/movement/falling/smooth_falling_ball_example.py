import simplegui, time, random

WINDOW_WIDTH = 500
WINDOW_HEIGHT = WINDOW_WIDTH
GLOBAL_CIRCLE_DIAMETER = 25

GRID_WIDTH = WINDOW_WIDTH / 25
GRID_HEIGHT = GRID_WIDTH

class BowlingBall:
    
    MOMENT_LENGTH = 10
    
    def __init__(self):
        self.moment = self.MOMENT_LENGTH
        self.ball = self.GridCircle((1,1))
        
    def draw_me(self, canvas):
        if self.moment > 0:
            self.moment -= 1
        else:
            new_center = (
                self.ball.center[0],
                self.ball.center[1] + 1
            )
            self.ball = self.GridCircle(new_center)
            print self.ball
            self.moment = self.MOMENT_LENGTH
            
        self.ball.draw_me(canvas)
    
    class GridCircle:
        
        DEFAULT_CIRCLE_DRAW_ATTRIBUTES = {
            "line_width": 2,
            "line_color": 'Blue',
            "fill_color": 'Aqua'
        }
        
        DIAMETER = GLOBAL_CIRCLE_DIAMETER
        RADIUS = DIAMETER / 2
        SHAPE_ATTRIBUTES = DEFAULT_CIRCLE_DRAW_ATTRIBUTES

        def __init__(self, center, radius=RADIUS, shape_attributes=SHAPE_ATTRIBUTES):
            self.center_point = (center[0]*self.DIAMETER + self.RADIUS, center[1]*self.DIAMETER + self.RADIUS)
            self.circle = self.Circle(self.center_point, radius, shape_attributes)
            self.center = center
            

        def draw_me(self, canvas):
            self.circle.draw_me(canvas)

        def __repr__(self):
            return "(%s,%s)" % (self.center[0], self.center[1])
        
        class Circle:

            DEFAULT_CIRCLE_DRAW_ATTRIBUTES = {
                "line_width": 2,
                "line_color": 'Blue',
                "fill_color": 'Aqua'
            }
            
            DIAMETER = GLOBAL_CIRCLE_DIAMETER
            RADIUS = DIAMETER / 2
            SHAPE_ATTRIBUTES = DEFAULT_CIRCLE_DRAW_ATTRIBUTES
            
            def __init__(self, center_point, radius=RADIUS, shape_attributes=SHAPE_ATTRIBUTES):
                self.radius = radius
                self.center_point = center_point
                self.shape_attributes = shape_attributes

            def draw_me(self, canvas):
                canvas.draw_circle(
                    self.center_point,
                    self.radius,
                    self.shape_attributes["line_width"],
                    self.shape_attributes["fill_color"],
                    self.shape_attributes["fill_color"]   
                )            
            
            

bb = BowlingBall()
                               
def draw(canvas):
    bb.draw_me(canvas)
        
frame = simplegui.create_frame("Home", WINDOW_WIDTH, WINDOW_HEIGHT)
frame.set_canvas_background("Silver")
frame.set_draw_handler(draw)
frame.start()        
              
