#Import all the necessary things to run the game
from pygame import *
import menu
import random
from classes import *




def rungame():
    #Gameplay screen resolution and caption title
    screen = pygame.display.set_mode((800, 600))
    display.set_caption("Jet mission")

    #starting scores and background image
    scores = 0
    theClock = pygame.time.Clock()
    bg_image = Star_bg("star.gif")

    #The starting coordinate of the moving background
    x = 0
    y = 0
    x1 = bg_image.width
    y1 = 0

    #initiate pygame
    pygame.init()


    #Creating the jet
    jet1 = Jet(screen)
    Jet_sprites = Group(jet1)

    #Create group for the moving asteroid
    asteroid_group = Group()

    #Create group for shooting bullets
    bullets = Group()


    #Initial Fps and that it will be faster after every frame
    Fps = 40
    asteroid_timer = pygame.time.get_ticks()
    while True:
        theClock.tick(Fps)
        Fps += 0.01

        #Moving background

        x -= 5
        x1 -= 5
        bg_image.draw(screen,x,y)
        bg_image.draw(screen,x1, y1)
        if x < -bg_image.width:
            x = 0
        if x1 < 0:
            x1 = bg_image.width

        #Making The score board with Font style and size
        font=pygame.font.SysFont("Times New Romans",36)
        score_board=font.render("score:"+str(scores),True,(255,255,255))
        screen.blit(score_board,(10,550))


        #Draws the jet
        Jet_sprites.draw(screen)
        #Draws the bullets
        bullets.draw(screen)
        #Draws the moving asteroid
        asteroid_group.draw(screen)
        #update jet when the game is run
        display.update()

        event.get()
        #Controls to move the jet and fire bullets

        key = pygame.key.get_pressed()
        if key[K_LEFT] and jet1.rect.x>0:
            jet1.moveleft()

        if key[K_RIGHT] and jet1.rect.x<=700:
            jet1.moveright()

        if key[K_DOWN] and jet1.rect.y<=500:
            jet1.movedown()

        if key[K_UP] and jet1.rect.y>0:
            jet1.moveup()

        if key[K_SPACE] and len(bullets) <= jet1.firerates+(scores/4000):
            bullet = Bullet(screen, jet1.rect.x+50, jet1.rect.y+42)
            bullets.add(bullet)
            pygame.mixer.music.load("LaserBlast.wav")
            pygame.mixer.music.play()

        if key[K_ESCAPE]:
            menu.menu_screen(Button,rungame)

        if key[K_p]:
            menu.pause_menu(Button,rungame)


        #Creating the asteroid randomly on the screen and moves
        if pygame.time.get_ticks() - asteroid_timer >= 200:
            asteroid = Asteroid(screen, 50, 50, random.randint(1,4)*6, 800, (random.randint(1,28) * 20))
            asteroid_group.add(asteroid)
            asteroid_timer = pygame.time.get_ticks()

        #Updating the movement of the asteroids
        for asteroid in asteroid_group:
            asteroid.movement()
            if asteroid.rect.right <= 0:
                asteroid_group.remove(asteroid) #remove after screen
            if groupcollide(Jet_sprites,asteroid_group,dokilla=True,dokillb=True):#collition check
                menu.lose_menu(Button,rungame,scores)

        #Updating the bullets on screen
        for bullet in bullets:
            bullet.movement()
            if bullet.rect.left > 800:
                bullets.remove(bullet)
            if groupcollide(bullets,asteroid_group,dokilla=True,dokillb=True):
                scores += 100

#Main function to run the game
menu.menu_screen(Button,rungame)


#Thanks to the Help from Friends
#---------------SPECIAL THANKS to Pier,Excel,georgius,William,Nicander,Nicolas,Andy,Guntur,Adrian-----------------------
"""Acknowledgement (Source):
LaserBlast.wav(shooting sound) http://soundbible.com/472-Laser-Blasts.html
"""
