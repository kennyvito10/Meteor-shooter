#Importing pygame and sys to create the start and quit menu buttons
from pygame import *
import sys
import pygame

#Menu module
def menu_screen(Button,run_game):
    #Window Caption title and resoultion of the window
    display.set_caption("Jet Mission")
    screen = pygame.display.set_mode((800, 600))
    #Menu button for starting the game and quitting the game
    start_button = Button("New Piskel.png")
    quit_button = Button("quit button.png")
    #Background image
    bg_image=pygame.image.load("asteroid_wall.jpg")
    bg_image=pygame.transform.scale(bg_image, (800, 600))


    pygame.init()
    #Menu Options whether to start or quit the game
    while True:
        rect_start= draw.rect(screen, (0, 0, 0), (250, 200, 300, 150))
        rect_quit = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150))
        screen.blit(bg_image,(0,0))

        screen.blit(start_button.button,(250,200))
        screen.blit(quit_button.button,(250,300))

        ev=event.wait()

        if ev.type == MOUSEBUTTONDOWN:
            if rect_start.collidepoint(mouse.get_pos()):
                run_game()
            if rect_quit.collidepoint(mouse.get_pos()):
                sys.exit()

        if ev.type == QUIT:
            sys.exit()

        display.update()

def pause_menu(Button,run_game):
    #The Pause menu of the game
    display.set_caption("Jet Mission")
    screen = pygame.display.set_mode((800, 600))

    #Buttons for start and quit the game
    start_button = Button("quit button.png")
    return_button = Button("pause button.png")

    #Background image of the menu
    bg_image = pygame.image.load("asteroid_wall.jpg")
    bg_image = pygame.transform.scale(bg_image, (800, 600))


    pygame.init()
    paused=True
    #The display of the game when the game is paused
    while paused:
        rect_start = draw.rect(screen, (0, 0, 0), (250, 200, 300, 150))
        rect_return = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150))
        screen.blit(bg_image, (0, 0))

        screen.blit(start_button.button, (250, 200))
        screen.blit(return_button.button, (250, 300))

        ev = event.wait()

        #What the users clicked, either to start or quit
        if ev.type == MOUSEBUTTONDOWN:
            if rect_start.collidepoint(mouse.get_pos()):
                menu_screen(Button,run_game)
            if rect_return.collidepoint(mouse.get_pos()):
                paused = False

        #Quits the game if user select quit
        if ev.type == QUIT:
            sys.exit()


        display.update()

def lose_menu(Button,run_game,score):
    #Creates a screen when you lose, such as the asteroid hits your jet
    display.set_caption("Jet Mission")
    screen = pygame.display.set_mode((800, 600))
    font=pygame.font.SysFont("times new roman",100)
    text=font.render("Replay?",True,(255,255,255))
    score_text=font.render("score:"+str(score),True,(255,255,255))

    #Start and quit buttons
    start_button = Button("New Piskel.png")
    quit_button = Button("quit button.png")

    #Background image for menu
    bg_image = pygame.image.load("asteroid_wall.jpg")
    bg_image = pygame.transform.scale(bg_image, (800, 600))

    pygame.init()

    #more or less the same with pause menu
    while True:
        rect_start = draw.rect(screen, (0, 0, 0), (250, 200, 300, 150))
        rect_quit = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150))
        screen.blit(bg_image, (0, 0))
        screen.blit(text,(200,10))
        screen.blit(start_button.button, (250, 200))
        screen.blit(quit_button.button, (250, 300))
        screen.blit(score_text,(200,400))

        ev = event.wait()

        #waiting the menu for selecting start or quit
        if ev.type == MOUSEBUTTONDOWN:
            if rect_start.collidepoint(mouse.get_pos()):
                run_game()
            if rect_quit.collidepoint(mouse.get_pos()):
                sys.exit()

        #quits the game if the user select the quit button
        if ev.type == QUIT:
            sys.exit()

        display.update()
