from random import randint
import pygame

from time import sleep
pygame.init()    #включаем модуль

width =  1200  #1369     #ширина
height = 600  #768     #высота
fps = 30      #кадров в секунду
game_name = "Zombie"
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(game_name)
bg = pygame.image.load('i.webp')
bg = pygame.transform.scale(bg, (width, height))
green = "#BDB76B"
won = pygame.image.load('won.webp')
won = pygame.transform.scale(won,(width, height))
loose = pygame.image.load('loose.webp')
loose = pygame.transform.scale(loose,(width,height))
scream = pygame.image.load('scream1.webp')
scream = pygame.transform.scale(scream,(width,height))
scream2 = pygame.image.load('scream2.webp')
scream2 = pygame.transform.scale(scream2,(width,height))
scream3 = pygame.image.load('scream3.webp')
scream3 = pygame.transform.scale(scream3,(width,height))
scream4 = pygame.image.load('scream4.webp')
scream4 = pygame.transform.scale(scream4,(width,height))
scream5 = pygame.image.load('scream5.webp')
scream5 = pygame.transform.scale(scream5,(width,height))
scream6 = pygame.image.load('scream6.webp')
scream6 = pygame.transform.scale(scream6,(width,height))

pygame.mixer.music.load('main_music.mp3')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

screamer = pygame.mixer.Sound('horror.mp3')
wons = pygame.mixer.Sound('won.mp3')
zoms = pygame.mixer.Sound('zombie_sound.mp3')
hit = pygame.mixer.Sound('bit.mp3')
lose = pygame.mixer.Sound('loose.mp3')

def draw_text(screen,text,size,x,y,color):
    font_name = pygame.font.match_font('arial')    # Выбираем тип шрифта для текста
    font = pygame.font.Font(font_name, size)       # Шрифт выбранного типа и размера
    text_image = font.render(text, True, color)    # Превращаем текст в картинку
    text_rect = text_image.get_rect()              # Задаем рамку картинки с текстом
    text_rect.center = (x,y)                       # Переносим текст в координаты
    screen.blit(text_image, text_rect)             # Рисуем текст на экране


player = pygame.image.load('skeleton.png')
player_rect = player.get_rect()

player_rect.y = 200
zombie = pygame.image.load('zombie1.png')
zombie_rect = zombie.get_rect()
zombie_rect.y = 200
zombie_rect.x = player_rect.x + 1000

zombie2 = pygame.image.load('zombie2.png')
zombie2_rect = zombie2.get_rect()
zombie2_rect.y = 200
zombie2_rect.x = player_rect.x + 900

palka = pygame.image.load('palka.png')
palka_rect = palka.get_rect()
count = 0
speed = 20
timer = pygame.time.Clock()
run = True
while run:
    timer.tick(fps)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and palka_rect.left > 0:
        palka_rect.x -= speed
    if key[pygame.K_RIGHT] and palka_rect.right < width:
        palka_rect.x += speed
    if key[pygame.K_UP] and palka_rect.top > 0:
        palka_rect.y -= speed
    if key[pygame.K_DOWN] and palka_rect.bottom < height:
        palka_rect.y += speed
    if palka_rect.colliderect(zombie_rect) and key[pygame.K_a]:
        hit.play()
        zoms.play()
        zombie_rect.x += randint(10, 500)
        count += 1
    if palka_rect.colliderect(zombie2_rect) and key[pygame.K_a]:
        hit.play()
        zoms.play()
        zombie2_rect.x += randint(10, 500)
        count += 1
    if not player_rect.colliderect(zombie_rect) or not player_rect.colliderect(zombie2_rect):
        zombie_rect.x -= randint(10, 20)
        zombie2_rect.y += randint(1, 10)
        zombie_rect.y += randint(1, 10)
        zombie2_rect.x -= randint(10, 20)
        zombie2_rect.y -= randint(1, 10)
        zombie_rect.y -= randint(1, 10)
    if count == 50:
        speed = 15
    if count == 70:
        speed = 10
        for i in range(1):
            palka_rect.x = randint(0, 1000)
            palka_rect.y = randint(0, 1000)
    if count == 90:
        for i in range(1):
            palka_rect.x = randint(0, 1000)
            palka_rect.y = randint(0, 1000)
        speed = 9
    if count == 70:
        if not player_rect.colliderect(zombie_rect) or not player_rect.colliderect(zombie2_rect):
            zombie_rect.x -= randint(10, 100)
            zombie2_rect.y += randint(1, 20)
            zombie_rect.y += randint(1, 20)
            zombie2_rect.x -= randint(10, 200)
            zombie2_rect.y -= randint(1, 100)
            zombie_rect.y -= randint(1, 10)
    screen.blit(bg, (0, 0))
    screen.blit(player, player_rect)
    screen.blit(zombie, zombie_rect)
    screen.blit(zombie2, zombie2_rect)
    screen.blit(palka, palka_rect)
    draw_text(screen,"Убито "+ str(count) + " из 100",  50, width//2, 30, green )

    if count == 100:
        sleep(1)
        wons.play()
        screen.blit(won,(0, 0))
        pygame.display.update()
        sleep(5)
        count = 101
    if count == 101:
        run = False
    if zombie_rect.colliderect(player_rect) or zombie2_rect.colliderect(player_rect):
        sleep(1)
        lose.play()
        screen.blit(loose, (0, 0))
        pygame.display.update()
        sleep(3)
        count = 101
    if count == 5 or count ==6 :
        zoms.stop()
        screamer.play()
        screen.blit(scream,(0, 0))
    if count == 20 or count==21 :
        zoms.stop()
        screamer.play()
        screen.blit(scream2, (0, 0))
    if count == 45 or count==46:
        zoms.stop()
        screamer.play()
        screen.blit(scream3, (0, 0))
    if count == 65 or count==66:
        zoms.stop()
        screamer.play()
        screen.blit(scream4, (0, 0))
    if count == 75 or count == 76:
        zoms.stop()
        screamer.play()
        screen.blit(scream5, (0, 0))
    if count == 95 or count == 96:
        zoms.stop()
        screamer.play()
        screen.blit(scream6, (0, 0))
    pygame.display.update()