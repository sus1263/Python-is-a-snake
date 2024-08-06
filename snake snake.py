# Import necessary libraries
import sys
import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    FULLSCREEN,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_w,
    K_a,
    K_s,
    K_d
)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((0, 0), FULLSCREEN)
clock = pygame.time.Clock()

# Define the Snake class
class Snake1:
    def __init__(self, x, y):
        self.body = [(x, y)]
        self.direction = 'RIGHT'
    
    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x, head_y)  # Default: no movement
        
        if self.direction == 'UP':
            new_head = (head_x, head_y - 10)
        elif self.direction == 'DOWN':
            new_head = (head_x, head_y + 10)
        elif self.direction == 'LEFT':
            new_head = (head_x - 10, head_y)
        elif self.direction == 'RIGHT':
            new_head = (head_x + 10, head_y)
        
        self.body.insert(0, new_head)
        self.body.pop()  # Remove the tail to keep the same length
    
    def change_direction(self, new_direction):
        if new_direction in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
            if (new_direction == 'UP' and self.direction != 'DOWN') or \
               (new_direction == 'DOWN' and self.direction != 'UP') or \
               (new_direction == 'LEFT' and self.direction != 'RIGHT') or \
               (new_direction == 'RIGHT' and self.direction != 'LEFT'):
                self.direction = new_direction
    
    def grow(self):
        tail_x, tail_y = self.body[-1]
        self.body.append((tail_x, tail_y))


class Snake2:
    def __init__(self, x, y):
        self.body = [(x, y)]
        self.direction = 'LEFT'
    
    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x, head_y)  # Default: no movement
        
        if self.direction == 'UP':
            new_head = (head_x, head_y - 10)
        elif self.direction == 'DOWN':
            new_head = (head_x, head_y + 10)
        elif self.direction == 'LEFT':
            new_head = (head_x - 10, head_y)
        elif self.direction == 'RIGHT':
            new_head = (head_x + 10, head_y)
        
        self.body.insert(0, new_head)
        self.body.pop()  # Remove the tail to keep the same length
    
    def change_direction(self, new_direction):
        if new_direction in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
            if (new_direction == 'UP' and self.direction != 'DOWN') or \
               (new_direction == 'DOWN' and self.direction != 'UP') or \
               (new_direction == 'LEFT' and self.direction != 'RIGHT') or \
               (new_direction == 'RIGHT' and self.direction != 'LEFT'):
                self.direction = new_direction
    
    def grow(self):
        tail_x, tail_y = self.body[-1]
        self.body.append((tail_x, tail_y))

# Initialize the two Snakes
snake = Snake(400, 300)
snake2 = Snake(width-400, height-300)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_UP:
                snake.change_direction('UP')
            elif event.key == K_DOWN:
                snake.change_direction('DOWN')
            elif event.key == K_LEFT:
                snake.change_direction('LEFT')
            elif event.key == K_RIGHT:
                snake.change_direction('RIGHT')
            elif event.key == K_w:
                snake.change_direction('UP')
            elif event.key == K_s:
                snake.change_direction('DOWN')
            elif event.key == K_a:
                snake.channge_direction('LEFT')
            elif event.key == K_d:
                snake.change_direction('RIGHT')


    # Move the snake
    snake.move()

    # Render the game
    screen.fill((255, 255, 255))  # Set background color to white
    # Add code to draw the snake on the screen

    pygame.display.flip()
    clock.tick(10)  # Adjust the speed of the game by changing the tick value

# The game loop will exit when running is set to False
pygame.quit()
sys.exit()
