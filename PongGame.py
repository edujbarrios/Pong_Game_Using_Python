import pygame

# Initialize pygame
pygame.init()

# Set the window size
window_size = (400, 400)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Pong")

# Set the dimensions of the game elements
paddle_width = 15
paddle_height = 60
ball_size = 20

# Set the speed of the ball
ball_speed_x = 5
ball_speed_y = 5

# Set the initial position of the ball
ball_x = 200
ball_y = 200

# Set the initial position of the paddles
left_paddle_y = 150
right_paddle_y = 150

# Set the score to 0
score = 0

# Set the font for rendering the score
font = pygame.font.Font(None, 36)

# Set the game loop to run indefinitely
while True:
    # Handle events
    for event in pygame.event.get():
        # Quit the game if the user closes the window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the ball
    pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), ball_size)

    # Draw the left paddle
    pygame.draw.rect(screen, (255, 255, 255), (0, left_paddle_y, paddle_width, paddle_height))

    # Draw the right paddle
    pygame.draw.rect(screen, (255, 255, 255), (400 - paddle_width, right_paddle_y, paddle_width, paddle_height))

    # Update the position of the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Check for ball collision with top and bottom of screen
    if ball_y > 400 - ball_size or ball_y < 0:
        ball_speed_y *= -1

    # Check for ball collision with paddles
    if ball_x < paddle_width and left_paddle_y < ball_y < left_paddle_y + paddle_height:
        ball_speed_x *= -1
        score += 1
    elif ball_x > 400 - paddle_width and right_paddle_y < ball_y < right_paddle_y + paddle_height:
        ball_speed_x *= -1
        score += 1

    # Render the score
    text = font.render(str(score), True, (255, 255, 255))
    screen.blit(text, (200, 10))

    # Update the display
    pygame.display.flip()
