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
    main()


def show_text_on_screen(text, font_size, y_position):
    font = pygame.font.Font(None, font_size)
    text_render = font.render(text, True, white)
    text_rect = text_render.get_rect(center = (width // 2, y_position))
    screen.blit(text_render, text_rect)


def game_over_screen():
    screen.fill(black)
    show_text_on_screen("Game Over! Press R to restart or Q to quit", 100, height // 2)
    pygame.display.flip()
    wait_for_key()


def wait_for_key():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == K_r:
                    waiting = False
                elif event.key == pygame.K_ESCAPE or event.key == K_q:
                    pygame.quit()
                    sys.exit()




# Define the Snake class
class Snake:
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


'''class food:
    def __init__(self, x, y):
        self.body = [(x, y)]
        self.body.insert(0, new_head)
        self.body.pop()




    def relocate(self):
        self.position = [random.randrange(0, screen.get_width() // 10) * 10, random.randrange(0, screen.get_height() // 10) * 10]'''




def main():
    # Game loop


    # Initialize the two Snakes and the food
    food_position = [random.randrange(0, screen.get_width() // 10) * 10, random.randrange(0, screen.get_height() // 10) * 10]
    Snake1 = Snake(400, 300)
    Snake2 = Snake(400, 600)


    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game_over = True
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
        Snake2.move()
        Snake1.grow()
        Snake2.grow()

        screen.fill((255, 255, 255))
        pygame.display.flip()


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
            game_over_screen()
            start_screen()
            Snake1.reset()
            Snake2.reset()
            game_over = False


        # # Render the game
        # else:
        #     screen.fill((255, 255, 255))  # Set background color to white




    # Draw Snake1
        for segment in Snake1.body:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(segment[0], segment[1], 10, 10))  # Green color for Snake1


    # Draw Snake2
        for segment in Snake2.body:
            pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(segment[0], segment[1], 10, 10))  # Blue color for Snake2


    #Draw the food
        # for segment in food.body:
        #     pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(segment[0], segment[1], 10, 10))
            


        pygame.display.flip()
        clock.tick(10)  # Adjust the speed of the game by changing the tick value


    # The game loop will exit when running is set to False


    pygame.quit()
    sys.exit()


start_screen()



