import turtle, random


class Game:
    '''
Purpose: Represents the general setup of the game in turtle
Instance variables: canvas which is the game board, self.player: the sname that the player controls
self.food: the food pellet that the snake should eat
Methods: initial method, gameloop
'''

    def __init__(self):
        #Setup 700x700 pixel window
        turtle.setup(700, 700)

        #Bottom left of screen is (-40, -40), top right is (640, 640)
        turtle.setworldcoordinates(-40, -40, 640, 640)
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        #Ensure turtle is running as fast as possible
        turtle.hideturtle()
        turtle.delay(0)
        turtle.tracer(0, 0)
        turtle.speed(0)

        #Draw the board as a square from (0,0) to (600,600)
        for i in range(4):
            turtle.forward(600)
            turtle.left(90)

        self.player = Snake(315, 315, 'green')
        self.food = Food()
        
        turtle.onkeypress(self.player.go_down, 'Down')
        turtle.onkeypress(self.player.go_up, 'Up')
        turtle.onkeypress(self.player.go_right, 'Right') #movement based on user key press
        turtle.onkeypress(self.player.go_left, 'Left')

        self.gameloop()
        #These two lines must always be at the BOTTOM of __init__
        turtle.listen()
        turtle.mainloop()

    def gameloop(self):
        if self.player.game_over(): #creating game over 
            turtle.write('Game Over', True, align ='Left', font =('Arial', 20, 'normal')) 
            return
        self.player.move(self.food)
        turtle.ontimer(self.gameloop, 200)
        turtle.update()

class Snake:
    '''
Purpose: x and y represent positions on the game board, segments represent the amount of segments on the snake which will grow as it eats
Instance variables: x and y coordinates, color, the snakes body (segments)
Methods: initial, grow which appends sections to the head as it eats, movements, game over which creates conditions where the user loses, and up down left right
'''

    def __init__(self, x, y, color):
        self.x = x
        self.y = y #initial stuff
        self.color = color
        self.segments = [] 
        self.vx = 30
        self.vy = 0
        self.grow() #calls grow to append segments during game
    
    def grow(self):
        head = turtle.Turtle()
        head.speed(0)
        head.fillcolor(self.color)
        head.shape('turtle') 
        head.shapesize(1.5, 1.5)
        head.penup()
        head.goto(self.x, self.y)
        self.segments.append(head)
        
   
    def move(self, food):
        head_x = self.x + self.vx
        head_y = self.y + self.vy
        if head_x == food.x and head_y == food.y: #if the head collides with a food piece
            self.grow() #calls grow to grow the snake
            food.delete_food()
            food.food_position()    #positions food after collision
        else:
            for i in range(len(self.segments) -1, 0, -1): #loops through every segment except the head
                self.segments[i].goto(self.segments[i - 1].xcor(), self.segments[i -1].ycor())  
        self.segments[0].goto(head_x, head_y) #moves first segment to head_x and head_y
        
        self.x = head_x
        self.y = head_y
        self.segments[0].goto(self.x, self.y) #split at the head and moves to new coordinates

    def game_over(self):
        if self.x < 0 or self.x > 600 or self.y < 0 or self.y > 600:
            return True #returns true if snake leaves box
        for segment in self.segments[1:]: #loop through every non-head segment
            if segment.xcor() == self.x and segment.ycor() == self.y: #if a segment collides into itself
                return True #returns true if snake runs into itself
        return False

    def go_down(self):
        self.vx = 0
        self.vy = -30

    def go_up(self):
        self.vx = 0
        self.vy = 30

    def go_right(self):
        self.vx = 30
        self.vy = 0

    def go_left(self):
        self.vx = -30
        self.vy = 0

class Food:
    '''
Purpose: creates the food piece
Instance variables: x and y which are the position on the board assigned to the food
Methods: initial method which just calls the food position method, and the food position method which creates the food piece and assigns its
'''

    def __init__(self):
        self.food_position() #calls food position

    def food_position(self):
        self.x = 15 + 30 * random.randint(0, 19) #chooses random position for food piece
        self.y = 15 + 30 * random.randint(0, 19)
        self.food = turtle.Turtle()
        self.food.shape('circle')  #
        self.food.fillcolor('red') # creating food piece
        self.food.penup()          #
        self.food.goto(self.x, self.y) #positions the food piece
    def delete_food(self):
        self.food.hideturtle()
        self.food.clear()
if __name__ == '__main__':
    Game()     
