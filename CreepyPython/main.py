from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')
screen.title('Creepy Python')


class Snake:
    def __init__(self):
        self.segment_count = 2
        self.segment_list = []
        self.create_head()
        self.head = self.segment_list[0]
        self.create_snake(2)
        self.draw_snake()
        screen.update()
        self.current_positions = [segment.position() for segment in self.segment_list]
        self.last_positions = []

    def create_head(self):
        python_head = Turtle()
        python_head.shape('triangle')
        python_head.pu()
        python_head.color('white')

        self.segment_list.append(python_head)

    def create_snake(self, segments):

        for segment in range(segments):
            python_segment = Turtle()
            python_segment.shape('square')
            python_segment.pu()
            python_segment.color('green')
            self.segment_list.append(python_segment)


    def draw_snake(self):
        starting_pos = self.head.position
        current_x = self.head.xcor()
        current_y = self.head.ycor()
        for segment in self.segment_list:
            segment.setx(current_x-20)

            current_x -= 20
    def update_snake(self):

        pass

    def go_down(self):
        self.head.setheading(270)
        self.head.fd(20)

        screen.update()

    def go_left(self):
        self.head.setheading(180)
        self.head.fd(20)
        screen.update()

    def go_up(self):
        self.head.setheading(90)
        self.head.fd(20)
        screen.update()

    def go_right(self):
        self.head.setheading(0)
        self.head.fd(20)
        screen.update()

snake = Snake()
screen.listen()
screen.onkeypress(key='w', fun=snake.go_up)
screen.onkeypress(key='s', fun=snake.go_down)
screen.onkeypress(key='a', fun=snake.go_left)
screen.onkeypress(key='d', fun=snake.go_right)

screen.exitonclick()
