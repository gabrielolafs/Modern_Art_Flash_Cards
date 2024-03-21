from peices import peices as cards
from time import sleep
from random import randint, shuffle
import pygame

# Initialize Pygame
pygame.init()

clock = pygame.time.Clock()

# Set the dimensions of the display
width, height = 720, 960
screen = pygame.display.set_mode((width, height))
fps = 120

img_size = min(width, height)
i = 3
current_card = ''
img = ''

questions_conts = ['Name?', 'Artist?', 'Year?']
questions       = ['Artist?', 'Year?', 'Name?'] # example
answers =         ['joe',      1992,   'pants'] # example

questions = []
answers = []

def adjusted_index():
    temp = []
    for i in questions_conts:
        temp.append(questions.index(i))

    return temp

def assign_answers():
    global answers
    answers = [-1, -1, -1]
    answers2 = current_card.answers
    adjusted = adjusted_index()
    for i in range(len(adjusted)):
        answers[adjusted[i]] = str(answers2[i])

    print(answers, len(answers))

def randomize_questions():
    global questions 
    questions = []
    for i in questions_conts:
        questions.append(i)
    shuffle(questions)
    assign_answers()

def next_image():
    global i, current_card, questions
    i = 0
    index = randint(0, len(cards) - 1)
    print(index)
    current_card = cards[index]
    print('curr card', current_card)
    randomize_questions()
    cards.pop(index)
    img_maker()

def reveal_next():
    global i
    if i > 2:
        next_image()
    else:
        i += 1

def img_maker():
    global img
    img = pygame.image.load("images/" + str(current_card.name) + '.png')
    x = img.get_width()
    y = img.get_height()
    if x > y: # landscape mode
        scaler = x / img_size
    else: # portate mode
        scaler = y / img_size
    img = pygame.transform.scale(img, (x // scaler, y // scaler))

reveal_next()

def pad_x():
    return abs(img.get_width() - img_size) / 2

def pad_y():
    return abs(img.get_height() - img_size) / 2

times = pygame.font.match_font("Times", bold = False)
font = pygame.font.Font(times, 24)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif  event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KSCAN_SPACE:
            reveal_next()

    # Clear the screen
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 0), (0, 0, img_size, img_size))

    screen.blit(img, (pad_x(), pad_y()))

    clock.tick(fps)

    if i > -1:
        screen.blit(font.render(questions[0], True, (0,0,0)), (10, img_size + 10))
    if i > 0:
        screen.blit(font.render(answers[0], True, (0,0,0)), (10, img_size + 40))
        screen.blit(font.render(questions[1], True, (0,0,0)), (10, img_size + 90))
    if i > 1:
        screen.blit(font.render(answers[1], True, (0,0,0)), (10, img_size + 120))
        screen.blit(font.render(questions[2], True, (0,0,0)), (10, img_size + 170))
    if i > 2:
        screen.blit(font.render(answers[2], True, (0,0,0)), (10, img_size + 200))


    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()