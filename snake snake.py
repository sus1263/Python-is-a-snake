# Import necessary libraries
import sys
import pygame
import random
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
    K_d,
    K_r,
    K_q,
)

# Initialize Pygame
pygame.init()
display_info = pygame.display.Info()
width, height = display_info.current_w, display_info.current_h
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
pygame.display.set_caption("Snake")

def start_screen():
    screen.fill(black)
    show_text_on_screen("Snake Game", 200, height // 3)
    show_text_on_screen("Press Space Bar To Start", 100, height // 2)
    pygame.display.flip()
    wait_for_key()

def show_text_on_screen(text, font_size, y_position):
    font = pygame.font.Font(None, font_size)
    text_render = font.render(text, True, white)
    text_rect = text_render.get_rect(center = (width // 2, y_position))
    screen.blit(text_render, text_rect)

def wait_for_key():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
                    waiting = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# Define the Snake class
class Snake1:
    def __init__(self, x, y):
        self.body = [(x, y)]
        self.length = 1
        self.direction = 'RIGHT'
    
    def move(self):
        #head = self.body[0].copy()
        if self.direction == 'UP':
            head[1] -= 10
        elif self.direction == 'DOWN':
            head[1] += 10
        elif self.direction == 'LEFT':
            head[0] -= 10
        elif self.direction == 'RIGHT':
            head[0] += 10

        self.body.insert(0, head)

        if len(self.body) > self.length:
            self.body.pop()

    def grow(self):
        self.length += 1
    
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
        self.direction = 'RIGHT'
    
    def move2(self):
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
Snake1 = Snake1(400, 300)
Snake2 = Snake2(400, 600)

def main():
    # Game loop
    running = True
    game_over = False 
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_w:
                    Snake1.change_direction('UP')
                elif event.key == K_s:
                    Snake1.change_direction('DOWN')
                elif event.key == K_a:
                    Snake1.change_direction('LEFT')
                elif event.key == K_d:
                    Snake1.change_direction('RIGHT')
                elif event.key == K_UP:
                    Snake2.change_direction('UP')
                elif event.key == K_DOWN:
                    Snake2.change_direction('DOWN')
                elif event.key == K_LEFT:
                    Snake2.change_direction('LEFT')
                elif event.key == K_RIGHT:
                    Snake2.change_direction('RIGHT')

        
        # Move the snake
        Snake1.move()
        Snake2.move2()

        # Check for collisions with food for Snake1 and Snake2
        for snake in [Snake1, Snake2]:
            if snake.body[0] == food_position:
                snake.grow()
                food_position = [random.randrange(0, screen.get_width() // 10) * 10, random.randrange(0, screen.get_height() // 10) * 10]

            # Check for collisions with game window boundaries
        if Snake1.body[0][0] < 0 or Snake1.body[0][1] < 0 or Snake1.body[0][0] >= screen.get_width() or Snake1.body[0][1] >= screen.get_height():
            game_over = True
        if Snake2.body[0][0] < 0 or Snake2.body[0][1] < 0 or Snake2.body[0][0] >= screen.get_width() or Snake2.body[0][1] >= screen.get_height():
            game_over = True    # Check for collisions with game window boundaries
        if Snake1.body[0][0] < 0 or Snake1.body[0][1] < 0 or Snake1.body[0][0] >= screen.get_width() or Snake1.body[0][1] >= screen.get_height():
            game_over = True
        if Snake2.body[0][0] < 0 or Snake2.body[0][1] < 0 or Snake2.body[0][0] >= screen.get_width() or Snake2.body[0][1] >= screen.get_height():
            game_over = True

        if game_over:
            screen.fill((0, 0, 0)) 
            font = pygame.font.Font(None, 100)
            text = font.render("Game Over! Press R to restart or Q to quit", True, (255, 255, 255))
            text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
            screen.blit(text, text_rect)

            pygame.display.flip()

            # Reset the game if the player chooses to restart
            keys = pygame.key.get_pressed()
            if keys[K_r]:
                Snake1.reset()
                Snake2.reset()
                game_over = False
                running = True
            elif keys[K_q]:
                running = False

        # Render the game
        else:
            screen.fill((255, 255, 255))  # Set background color to white


    # Draw Snake1
        for segment in Snake1.body:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(segment[0], segment[1], 10, 10))  # Green color for Snake1

    # Draw Snake2
        for segment in Snake2.body:
            pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(segment[0], segment[1], 10, 10))  # Blue color for Snake2


        pygame.display.flip()
        clock.tick(10)  # Adjust the speed of the game by changing the tick value

    # The game loop will exit when running is set to False

    pygame.quit()
    sys.exit()

start_screen()
