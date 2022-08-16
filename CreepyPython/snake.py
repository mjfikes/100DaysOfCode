from turtle import Turtle, Screen
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_SEGMENTS = 2

class Snake:
    def __init__(self):
        self.segment_count = STARTING_SEGMENTS
        self.segment_list = []
        self.create_head()
        self.head = self.segment_list[0]
        self.create_snake(self.segment_count)
        Screen().update()
        self.current_positions = [segment.position() for segment in self.segment_list]
        self.last_positions = []
        self.is_alive = True

    def create_head(self):

        python_head = Turtle()
        python_head.goto(0,0)
        python_head.shape('square')
        python_head.pu()
        python_head.color('green')

        self.segment_list.append(python_head)

    def create_snake(self, segments):

        for segment in range(segments):
            python_segment = Turtle()
            python_segment.shape('square')
            python_segment.pu()
            python_segment.color('green')
            self.segment_list.append(python_segment)
            starting_pos = self.head.position
            current_x = self.head.xcor()
            current_y = self.head.ycor()
            for s in self.segment_list:
                s.setx(current_x - MOVE_DISTANCE)

                current_x -= MOVE_DISTANCE
        self.set_tail()

    def add_segment(self,score):
        python_segment = Turtle()
        python_segment.shape('square')

        python_segment.pu()
        python_segment.color('green')
        self.segment_list.append(python_segment)
        try:
            starting_pos = self.last_positions[-1]
        except ValueError:
            starting_pos = self.current_positions[-1]
        python_segment.setposition(starting_pos)
        self.set_tail()

    def update_snake(self):
        self.last_positions = self.current_positions
        for segment in self.segment_list[1:]:
            segment.setposition(self.last_positions.pop(0))

        self.current_positions = [segment.position() for segment in self.segment_list]  # refresh current positions


    def set_tail(self):
        for i in self.segment_list[:-1]:
            i.shape('square')
        tail_segment = self.segment_list[-1]
        tail_segment.shape('triangle')
        tail_segment.tiltangle(abs(self.head.heading()-180))


    def move(self):
        #self.last_positions = [segment.position() for segment in self.segment_list]
        self.head.fd(MOVE_DISTANCE)
        self.update_snake()
        self.ouroboros()


    def go_down(self):
        self.head.setheading(DOWN)
        self.segment_list[-1].tiltangle(UP)

    def go_left(self):
        self.head.setheading(LEFT)
        self.segment_list[-1].tiltangle(RIGHT)

    def go_up(self):
        self.head.setheading(UP)
        self.segment_list[-1].tiltangle(DOWN)

    def go_right(self):
        self.head.setheading(RIGHT)
        self.segment_list[-1].tiltangle(LEFT)

    def ouroboros(self):  # check if the snake is eating itself
        head_x = round(self.head.xcor())
        head_y = round(self.head.ycor())
        for pos in self.current_positions[1:]:
            pos_x = round(pos[0])
            pos_y = round(pos[1])

            if (head_x == pos_x and head_y==pos_y):
                self.is_alive = False

    def reset(self):
        [segment.hideturtle() for segment in self.segment_list]
        self.segment_list.clear()
        #self.current_positions.clear()
        #self.last_positions.clear()

        self.create_head()
        self.head = self.segment_list[0]
        self.create_snake(self.segment_count)
        self.current_positions = [segment.position() for segment in self.segment_list]
        self.is_alive = True



