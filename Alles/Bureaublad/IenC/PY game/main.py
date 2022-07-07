import pygame
import random
import os

pygame.init()
clock = pygame.time.Clock()
op_grond = 0
checken = 0
collision = 0
level = 2
punt_x = [1, 60, 89, 223]
punt_y = []

scherm_breete = 700
size = (scherm_breete, 500)

zwart = (0, 0, 0)
wit = (255, 255, 255)
rood = (255, 0, 0)
blauw = (31, 133, 222)
geel = (255, 255, 0)
groen = (0, 255, 0)

snelheid_x = 0
snelheid_y = -50
pos_x = 350
pos_y = 20

weerstand = 1.002
acceleratie = 0.5
zwaartekracht = 0.001
bounce_efficientie = -1.4
aantal = 4
levelomhoogperlazer = 0.0002
levens = 5

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Zeno's Game :O")


def maakpunt_x(aantal, punt_x, scherm_breete):
  punt_x.clear()
  for i in range(aantal):
    punt_x.append(
      random.randint(scherm_breete / aantal * i,
                           scherm_breete / aantal * (i + 1)))
  return punt_x

def maakpunt_y(aantal, punt_y, scherm_breete):
  punt_y.clear()
  for i in range(aantal):
    punt_y.append(
      random.randint(scherm_breete / aantal * i, scherm_breete / aantal * (i + 1)))
  return punt_y

def spawn_enemies_verticaal(aantal, checken, pos_x, pos_y, punt_x, punt_y, scherm_breete, levens, done):
  for i in range(aantal):
    pygame.draw.rect(screen, (checken, 0, 0), [punt_x[i], 0, 5, 500])
  if checken > 254:
    collision = 0
    for i in range(len(punt_x)):
      if punt_x[i]- 40 <= pos_x and punt_x[i] + 40 > pos_x:
        collision = 1
    for i in range(len(punt_y)):
      if punt_y[i] - 40 <= pos_y and punt_y[i] + 40 > pos_y:
        collision = 1
    if collision == 1:
      levens = levens - 1
      if levens == 1:
        print("je hebt nu nog maar: ", levens, " leven over :(")
      elif levens == 0:
        done = True
      else:
        print("je hebt nu nog maar: ", levens, " levens over :(")
    punt_x.clear()
    for i in range(aantal):
      punt_x.append(
        random.randint(scherm_breete / aantal * i, scherm_breete / aantal * (i + 1)))
    checken = 0
  return pos_x, pos_y, checken, punt_x, levens, done

def spawn_enemies_horizontaal(aantal, checken, pos_x, pos_y, punt_x, punt_y, scherm_breete , levens, done):
  for i in range(aantal):
    pygame.draw.rect(screen, (checken, 0, 0), [0, punt_y[i], scherm_breete, 5])
  if checken > 254:
    collision = 0





    for i in range(len(punt_x)):
      if punt_x[i] < (pos_x + 40) and punt_x[i] > (pos_x - 40):
        collision = 1
    for i in range(len(punt_y)):
      if punt_y[i] < (pos_y + 40) and punt_y[i] > (pos_y - 40):
        collision = 1
    if collision == 1:
      levens = levens - 1
      if levens == 1:
        print("je hebt nu nog maar: ", levens, " leven over :(")
      elif levens == 0:
        done = True
      else:
        print("je hebt nu nog maar: ", levens, " levens over :(")
    punt_y.clear()
    for i in range(aantal):
      punt_y.append(random.randint(scherm_breete / aantal * i, scherm_breete / aantal * (i + 1)))
    checken = 0
    print(punt_y)
  return pos_x, pos_y, checken, punt_y, levens, done






punt_x = maakpunt_x(aantal, punt_x, scherm_breete)
punt_y = maakpunt_y(aantal, punt_y, scherm_breete)
done = False
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snelheid_x -= acceleratie
            if event.key == pygame.K_RIGHT:
                snelheid_x += acceleratie
            if event.key == pygame.K_UP:
                if op_grond == 0:
                    snelheid_y -= acceleratie
            if event.key == pygame.K_DOWN:
                snelheid_y += acceleratie

    snelheid_y = snelheid_y + zwaartekracht

    snelheid_y = snelheid_y / weerstand
    snelheid_x = snelheid_x / weerstand
    pos_x = pos_x + snelheid_x
    pos_y = pos_y + snelheid_y

    checken_y = pos_y + snelheid_y
    if checken_y > 436:
        pos_y = 436
        op_grond = 1
        snelheid_y = snelheid_y / bounce_efficientie
    checken_y = pos_y + snelheid_y
    if checken_y < 0:
        pos_y = 0
        snelheid_y = snelheid_y / bounce_efficientie
    checken_x = pos_x + snelheid_x
    if checken_x < 0:
        pos_x = 0
        snelheid_x = snelheid_x / bounce_efficientie
    if checken_x > 665:
        pos_x = 665
        snelheid_x = snelheid_x / bounce_efficientie
    else:
        op_grond = 0

    screen.fill(blauw)

    checken = checken + level / 30
    pos_x, pos_y, checken, punt_x, levens, done = spawn_enemies_verticaal(aantal, checken, pos_x, pos_y, punt_x, punt_y, scherm_breete, levens, done)

    pos_x, pos_y, checken, punt_y, levens, done = spawn_enemies_horizontaal(aantal, checken, pos_x, pos_y, punt_x, punt_y, scherm_breete , levens, done)




    pygame.draw.line(screen, wit, [0, 499], [700, 499], 50)

    pygame.draw.ellipse(screen, geel, [pos_x, pos_y, 40, 40], 20)

    pygame.display.flip()

print("gemaakt met plezier door Zeno Smit ;)")
