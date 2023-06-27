import pygame
import sys
import random

pygame.init()

clock = pygame.time.Clock()

width = 800
height = 500

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Hangman")
icon = pygame.image.load("img_9.png")
pygame.display.set_icon(icon)

game_over = False

row = 2
col = 13
gap = 20
size = 40
boxes = []

button_width, button_height = 190, 30
button_pos = (width - button_width-3, 3)
def draw_button1():
    pygame.draw.rect(screen, (0, 0, 0), (button_pos, (button_width, button_height)), 2)
    font = pygame.font.Font(None, 18)
    text = font.render('Made by Jaskarandeep Singh', True, (0, 0, 0))
    text_rect = text.get_rect(center=(button_pos[0] + button_width / 2, button_pos[1] + button_height / 2))
    screen.blit(text, text_rect)


# To draw boxes
for row in range(row):
    for col in range(col):
        x = ((col * gap) + gap) + (size * col)
        y = ((row * gap) + gap) + (size * row) + 330
        box = pygame.Rect(x, y, size, size)
        boxes.append(box)

buttons = []
A = 65

for ind, box in enumerate(boxes):
    letter = chr(A + ind)
    button = [box, letter]
    buttons.append(button)


def draw_buttons(buttons):
    for box, letter in buttons:
        btn_text = font.render(letter, True, (0, 0, 0))
        btn_rect = btn_text.get_rect(center=(box.x + 20, box.y + 20))
        screen.blit(btn_text, btn_rect)
        pygame.draw.rect(screen, (0, 0, 0), box, 2)


def display_guess():
    display_text = ''
    for letter in word:
        if letter in guessed:
            display_text += f"{letter} "
        else:
            display_text += '_ '

    text = letter_font.render(display_text, True, (0, 0, 0))
    screen.blit(text, (400, 200))


images = []
hangman_status = 0

# creating the words list
words = ['UNITED STATES', 'UNITED KINGDOM', 'CANADA', 'AUSTRALIA', 'GERMANY', 'FRANCE', 'ITALY', 'JAPAN', 'BRAZIL', 'CHINA', 'RUSSIA', 'INDIA', 'MEXICO']
word = random.choice(words)
guessed = []

# Display the initial image
image = pygame.image.load("img_21.png")
images.append(image)

# setting the font style
font = pygame.font.SysFont("arial", 30)
game_font = pygame.font.SysFont("arial", 80)
letter_font = pygame.font.SysFont("arial", 60)

# Title parameters
title = "Hangman"
title_text = game_font.render(title, True, (255, 0, 0))
title_rect = title_text.get_rect(center=(width // 2, title_text.get_height() // 2 + 10))
# subtitle = "Guess the country name"
# subtitle_text = game_font.render(subtitle, True, (0, 0, 0))
# subtitle_rect = title_text.get_rect(center=(width // 2, subtitle_text.get_height() // 2 + 35))
font = pygame.font.Font(None, 28)
subtext = font.render('Guess the country name', True, (155, 0, 155))
subtext_rect = subtext.get_rect(center=(width // 2, subtext.get_height() // 2 + 100))


# Game loop
running = True
while running:
    screen.fill((255, 255, 255))
    # Checking for event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # quit event
            running = False
        # Checking for mouse position
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = event.pos

            # Checking  for correct letter
            for button, letter in buttons:
                if button.collidepoint(click_pos):
                    if letter not in word:
                        hangman_status += 1
                    if hangman_status == 6:
                        game_over = True
                    guessed.append(letter)
                    buttons.remove([button, letter])

            # displaying the images accordingly
            for i in range(5):
                if hangman_status == 1:
                    image = pygame.image.load("img_23.png")
                    images.append(image)
                elif hangman_status == 2:
                    image = pygame.image.load("img_22.png")
                    images.append(image)
                elif hangman_status == 3:
                    image = pygame.image.load("img_24.png")
                    images.append(image)
                elif hangman_status == 4:
                    image = pygame.image.load("img_25.png")
                    images.append(image)
                elif hangman_status == 5:
                    image = pygame.image.load("img_26.png")
                    images.append(image)
                elif hangman_status == 6:
                    running = False
    screen.blit(image, (150, 150))
    for box in boxes:
        pygame.draw.rect(screen, (0, 0, 0), box, 2)

    # Win and Lost
    won = True
    for letter in word:
        if letter not in guessed:
            won = False
    if won:
        game_over = True
        game_text = "YOU WON!"
        game_font = pygame.font.SysFont("arial", 90)
    else:
        text1 = "YOU LOST! the word was : "
        game_text = text1+word
        game_font = pygame.font.SysFont("arial", 40)


    draw_buttons(buttons)
    draw_button1()
    display_guess()
    screen.blit(title_text, title_rect)
    screen.blit(subtext, subtext_rect)
    clock.tick(50)
    pygame.display.update()


    # Displaying the result text
    if game_over:
        screen.fill((255, 255, 255))
        text = game_font.render(game_text, True, (0, 0, 0))
        text_rect = text.get_rect(center=(width // 2, height // 2))
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
        sys.exit()
pygame.quit()
