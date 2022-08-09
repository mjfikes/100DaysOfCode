from turtle import Turtle, Screen
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segment_count = 4
        self.segment_list = []
        self.create_head()
        self.head = self.segment_list[0]
        self.create_snake(self.segment_count)
        Screen().update()
        self.current_positions = [segment.position() for segment in self.segment_list]
        self.last_positions = []

    def create_head(self):
        python_head = Turtle()
        python_head.shape('triangle')
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

    def update_snake(self):
        for segment in self.segment_list[1:]:
            segment.setposition(self.last_positions.pop(0))

        self.current_positions = [segment.position() for segment in self.segment_list]  # refresh current positions
        Screen().update()


    def go_down(self):
        self.last_positions = [segment.position() for segment in self.segment_list]
        self.head.setheading(DOWN)
        self.head.fd(MOVE_DISTANCE)
        self.update_snake()
        self.ouroboros()

    def go_left(self):
        self.last_positions = [segment.position() for segment in self.segment_list]
        self.head.setheading(LEFT)
        self.head.fd(MOVE_DISTANCE)
        self.update_snake()
        self.ouroboros()

    def go_up(self):
        self.last_positions = [segment.position() for segment in self.segment_list]
        self.head.setheading(UP)
        self.head.fd(MOVE_DISTANCE)
        self.update_snake()
        self.ouroboros()

    def go_right(self):
        self.last_positions = [segment.position() for segment in self.segment_list]
        self.head.setheading(RIGHT)
        self.head.fd(MOVE_DISTANCE)
        self.update_snake()
        self.ouroboros()

    def ouroboros(self):
        head_x = round(self.head.xcor())
        head_y = round(self.head.ycor())
        for pos in self.current_positions[1:]:
            pos_x = round(pos[0])
            pos_y = round(pos[1])

            if (head_x == pos_x and head_y==pos_y):
                print("CHOMP CHOMP!")
                exit()

