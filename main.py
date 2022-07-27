# Task1 Guess the Number

# Tkinter  GUI or we can use pygame
# random module main  randomly select a number
# Hint Method

# _______________________________________________________
# importing all modules


import math
import os
import sys
import random
import pygame


class MAIN_GAME:
    # playerName = input("Hi, what is your name? : ")
    count = 0

    def Main_game():
        number = random.randint(1, 10)
        Instructions.config(text='Ok '  # +playerName +
                                        + )
        count += 1
        while count < 5:
            guess = Input()
            if guess < number:
                Instructions.config(text='Your guess is too low')
            elif guess > number:
                Instructions.config(text=' Your guess is too high')
            elif guess == number:
                count = 0
                Instructions.config(text='Congratulations You guessed the number in ' +
                                    str(count) + ' tries!')
            break
        else:
            Instructions.config(
                text='OOPS! You did not guess the number, The number was ' + str(number))
            break

    def display_text():
        pass


# 856ff8
pygame.init()

# creating game window
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Guess the  Number ')

# creating tittle bar icon
icon = pygame.image.load('numbers.png')
pygame.display.set_icon(icon)


# Game triggering variable
# to quit or exit the game
exit_game = False
game_over = False


# create a game loop
while not exit_game:
    for event in pygame.event.get():  # this will give all the events that occur on the game screen like coordinates of mouse key press values etc
        # print(event)
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_RIGHT:
                print("you have pressed right arrow key")
    gameDisplay.fill((200, 255, 100))
    pygame.display.update()


pygame.quit()
