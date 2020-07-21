import pygame
import math

FPS = 60
W = 1200 # ширина экрана
H = 800 # высота экрана
BLUE = (135, 206, 235)

pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

a = 0
b = 0
c = 0
alf = 0
x = 190
y = H - 135
x1 = W + 120
y1 = 125
rock = 23
x2 = 0
y2 = 0
flag = 0
puskflag = 0
pusk1= 1
pusk = 40


tungus_surf = pygame.image.load('tunguska.png')
tungus_rect = tungus_surf.get_rect(bottomright=(750, 790))
h11_surf = pygame.image.load('he111.png')
h11_rect = h11_surf.get_rect(bottomright=(1000, 150))
racket_surf = pygame.image.load('raket.png')
racket_rect = racket_surf.get_rect(bottomright=(1000, 150))
boom_surf = pygame.image.load('boom.png')
boom_rect = boom_surf.get_rect(center=(x, y))
scale0 = pygame.transform.scale(boom_surf, (boom_surf.get_width() // 3,
                                          boom_surf.get_height() // 3))

scale0_rect = scale0.get_rect(center=(x, y))

scale = pygame.transform.scale(h11_surf, (h11_surf.get_width() // 2,
                                          h11_surf.get_height() // 2))

scale_rect = scale.get_rect(center=(1000, 150))
sc.blit(scale, scale_rect)

scale1 = pygame.transform.scale(tungus_surf, (tungus_surf.get_width() // 2,
                                          tungus_surf.get_height() // 2))

scale1_rect = scale1.get_rect(bottomleft=(100, 750))
sc.blit(scale1, scale1_rect)

scale2 = pygame.transform.scale(racket_surf, (racket_surf.get_width() // 3,
                                          racket_surf.get_height() // 3))

scale2_rect = scale2.get_rect(bottomleft=(500, 750))
sc.blit(scale2, scale2_rect)

running = True
while running:

    pygame.display.update()
    sc.fill(BLUE)
    pygame.draw.rect(sc, (34, 139, 34), (0, 750, W, H))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LALT] and keys[pygame.K_F4]:
        exit()

    if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
        x -= 10
        y -= 10
    elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
        x += 10
        y -= 10
    elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
        x -= 10
        y += 10
    elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
        x += 10
        y += 10
    elif keys[pygame.K_LEFT]:
        x -= 10
    elif keys[pygame.K_RIGHT]:
        x += 10
    elif keys[pygame.K_UP]:
        y -= 10
    elif keys[pygame.K_DOWN]:
        y += 10

    if x1 < -130:
        x1 = W + 130
    if x < -130:
        x = W + 130
    if x > (W-150):
        x = (W-150)
    if y < -150:
        y = -150
    if y > H:
        y = H

   # sc.blit(tungus_surf, tungus_rect)
   # sc.blit(h11_surf, h11_rect)


  #  scale2_rect = scale2.get_rect(center=(x+140, 665))

    x2 = (x1-x-4)
    y2 = (y-y1)
    pressed = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()
    x1 -= 4
    scale_rect = scale.get_rect(center=(x1, y1))
    sc.blit(scale, scale_rect)

    if pressed[0] or flag:
        if pusk1<pusk and puskflag == 0 :
            a = 6 * math.cos(math.radians(rock))
            b = 6 * math.sin(math.radians(rock))
            rot = pygame.transform.rotate(scale2, rock)
            rot_rect = rot.get_rect(center=(x + a, y-b ))
            sc.blit(rot, rot_rect)
            x += a
            y-=b
            pusk1 +=1
        else:
            pusk1 = 1
            puskflag = 1

        if y2 >= 0 and puskflag:
            alf = x2/math.sqrt(x2*x2 + y2*y2)
            alf = math.degrees(math.acos(alf))
        elif x2 < 0 and y2 < 0 and puskflag:
            x2 = abs(x1 - x-4)
            y2 = abs(y - y1)
            alf = y2 / math.sqrt(x2 * x2 + y2 * y2)
            alf = 180 + math.degrees(math.acos(alf))
        else:
            alf = y2 / math.sqrt(x2 * x2 + y2 * y2)
            alf = math.degrees(math.asin(alf))
        if alf - rock > 0 and puskflag:
            if alf - rock >=3:
                rock += 3
            if alf - rock == 2:
                rock += 2
            if alf - rock == 1:
                rock += 1
            a = 10*math.cos(math.radians(rock))
            b = 10*math.sin(math.radians(rock))
            rot = pygame.transform.rotate(scale2, rock)
            rot_rect = rot.get_rect(center=(x+a, y-b))
            sc.blit(rot, rot_rect)
            x += a
            y -= b
        elif alf - rock < 0 and puskflag:
            if alf - rock <= -3:
                rock -= 3
            if alf - rock == -2:
                rock -= 2
            if alf - rock == -1:
                rock -= 1
            a = 10 * math.cos(math.radians(rock))
            b = 10 * math.sin(math.radians(rock))
            rot = pygame.transform.rotate(scale2, rock)
            rot_rect = rot.get_rect(center=(x+a, y-b))
            sc.blit(rot, rot_rect)
            x += a
            y -= b
        elif alf - rock == 0 and puskflag:
            rock -= 3
            a = 10 * math.cos(math.radians(rock))
            b = 10 * math.sin(math.radians(rock))
            rot = pygame.transform.rotate(scale2, rock)
            rot_rect = rot.get_rect(center=(x + a, y - b))
            sc.blit(rot, rot_rect)
            x += a
            y -= b
            print(rock)


        flag = 1
        if (x-x1 < 100 and y-y1 < 20) and (y-y1 > -20 and x-x1 > -100) and puskflag:
            scale0_rect = scale0.get_rect(center=(x, y))
            sc.blit(scale0, scale0_rect)
            scale1_rect = scale1.get_rect(bottomleft=(100, H-30))
            sc.blit(scale1, scale1_rect)
            flag = 0
            pygame.display.update()
            a = 0
            b = 0
            alf = 0
            x = 190
            y = H - 135
            x1 = W + 120
            y1 = 125
            rock = 23
            puskflag = 0
            pygame.time.delay(1000)

    scale1_rect = scale1.get_rect(bottomleft=(100, H-30))
    sc.blit(scale1, scale1_rect)

    if pressed[2]:
        flag=0
        a = 0
        b = 0
        alf = 0
        x = 190
        y = H - 135
        x1 = W + 120
        y1 = 125
        rock = 23

    clock.tick(FPS)

