import pygame
import math


def main():
    pygame.init()

    

    class WinsdowSize:
        def __init__(self, sizeh, sizew):
            self.csizeh = sizeh
            self.csizew = sizew

    newWindow = WinsdowSize(700, 1368)
    win = pygame.display.set_mode((newWindow.csizew, newWindow.csizeh))
    pygame.display.set_caption("MARIO")
    clock = pygame.time.Clock()
    #bg = pygame.image.load('mario.jpg')
    #clock=pygame.display.clock()
    FPS=60
    screen = pygame.display.set_mode((newWindow.csizew, newWindow.csizeh))
    pygame.display.set_caption("MARIO")
    bg = pygame.image.load("mario.jpg").convert()
    bg_width = bg.get_width()
    bg_rect = bg.get_rect()

    scroll = 0
    tiles = math.ceil(newWindow.csizew / bg_width ) + 1

    herovel = 5
    # width: int = 100
    # height: int = 100
    hero = pygame.Rect(100, newWindow.csizeh - 100, 100, 100)
    villain = pygame.Rect(newWindow.csizew - 100, newWindow.csizeh - 100, 100, 100)

    # w = sizew - width
    # z = sizeh - height
    # x = 10
    # y = sizeh - height
    velv = 25
    score = 0
    #highscore = 0
    right = True
    left = False
    charl = pygame.image.load('mri.png')
    charr = pygame.image.load('mri.png')
    vil = pygame.image.load('mariofacel.png')

    def redrawGameWindow():
        win.blit(bg, (0, 0))
        text = font.render(f'Score: {score}0', False, (0, 0, 0))
        #text1="LEVEL 1"
        if score <= 10:
            text2 = font.render(f'level 1', False, (0, 0, 0))
        else:
            text2 = font.render(f'level 2', False, (0, 0, 0))
        win.blit(text, (900, 20))
        win.blit(text2, (100, 20))
        if left:
            win.blit(charl, (hero.x, hero.y))
        if right:
            win.blit(charr, (hero.x, hero.y))
        win.blit(vil, (villain.x, villain.y))
        pygame.display.update()

    font = pygame.font.SysFont('comicsans', 70, True)
    run = True
    isJump = False
    jumpcount: int = 11
    while run:
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and hero.x > 0:
            left = True
            right = False
            if hero.x - herovel < 0:
                hero.x = 0
            else:
                hero.x -= herovel
        if keys[pygame.K_RIGHT] and hero.x < newWindow.csizew - hero.size[0]:
            right = True
            left = False
            if hero.x + herovel > newWindow.csizew - hero.size[0]:
                hero.x = newWindow.csizew - hero.size[0]
            else:
                hero.x += herovel
        if not isJump:
            #  if keys[pygame.K_UP] and y > 0:
            #     if y-vel < 0:
            #        y = 0
            #   else:
            #      y -= vel
            # if keys[pygame.K_DOWN] and y < size-height:
            #   if y+vel > size-height:
            #      y = size-height
            # else:
            #    y += vel
            if keys[pygame.K_SPACE]:
                isJump = True
        else:
            if jumpcount >= -11:
                neg = 1
                if jumpcount < 0:
                    neg = -1
                hero.y -= (jumpcount ** 2) * 0.9 * neg
                jumpcount -= 1
            else:
                isJump = False
                hero.y = newWindow.csizeh - 100
                jumpcount = 11
        if villain.x > 0:
            villain.x = villain.x - velv
        else:
            villain.x = newWindow.csizew - villain.size[0]
            velv += 2
            score = score + 1

        for i in range(0,tiles) :
            screen.blit(bg,(i*bg_width+scroll,0))
            bg_rect.x=i*bg_width+scroll
            pygame.draw.rect(screen,(255,0,0),bg_rect,1)
        scroll-=5

        if abs(scroll)>bg_width:
            scroll=0
        redrawGameWindow()
        #if hero.colliderect(villain):
        #    break

    pygame.quit()


if __name__ == "__main__":
    main()
