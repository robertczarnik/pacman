import pygame, sys,os
from pygame.locals import *
import random
random.seed()

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((570, 660)) # 19/21 kratki + 1 kratka tekst 

sciana_zwykla_pion = pygame.image.load('sciana_zwykla_pion.png')
sciana_zwykla_poziom = pygame.image.load('sciana_zwykla_poziom.png')

sciana_czapka=pygame.image.load('rog_gora.png')
sciana_buty=pygame.image.load('rog_dol.png')
sciana_p=pygame.image.load('rog_prawy.png')
sciana_l=pygame.image.load('rog_lewy.png')

gora3=pygame.image.load('sciana_3_gora.png')
dol3=pygame.image.load('sciana_3_dol.png')
prawa3=pygame.image.load('sciana_3_prawa.png')
lewa3=pygame.image.load('sciana_3_lewa.png')

kolanko_pg=pygame.image.load('kolanko_pg.png')
kolanko_pd=pygame.image.load('kolanko_pd.png')
kolanko_ld=pygame.image.load('kolanko_ld.png')
kolanko_lg=pygame.image.load('kolanko_lg.png')

punkt = pygame.image.load('pkt.png')
bonus = pygame.image.load('bonus.png')

screen = pygame.display.get_surface()

mapa =[[-8,3,3,3,3,3,3,3,3,-2,3,3,3,3,3,3,3,3,-5], #2-sciana_pion 3-sciana_poziom 7-bonus 8-punkt 9-puste 
       [2,8,8,8,8,8,8,8,8,2,8,8,8,8,8,8,8,8,2], # 0-czapka 4-buty 5-p 6-l -1-3gora -2-3dol -3-3prawa -4-3lewa
       [2,7,6,5,8,6,3,5,8,4,8,6,3,5,8,6,5,7,2],
       [2,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,2],
       [2,8,6,5,8,0,8,6,3,-2,3,5,8,0,8,6,5,8,2],
       [2,8,8,8,8,2,8,8,8,2,8,8,8,2,8,8,8,8,2],
       [-7,3,3,-5,8,-3,3,5,9,4,9,6,3,-4,8,-8,3,3,-6],
       [9,9,9,2,8,2,9,9,9,9,9,9,9,2,8,2,9,9,9],
       [-8,3,3,-6,8,4,9,-8,5,9,6,-5,9,4,8,-7,3,3,-5],
       [2,9,9,9,8,9,9,2,9,9,9,2,9,9,8,9,9,9,2],
       [-7,3,3,-5,8,0,9,-7,3,3,3,-6,9,0,8,-8,3,3,-6],
       [9,9,9,2,8,2,9,9,9,9,9,9,9,2,8,2,9,9,9],
       [-8,3,3,-6,8,4,9,6,3,-2,3,5,9,4,8,-7,3,3,-5],
       [2,8,8,8,8,8,8,8,8,2,8,8,8,8,8,8,8,8,2],
       [2,8,6,-5,8,6,3,5,8,4,8,6,3,5,8,-8,5,8,2],
       [2,7,8,2,8,8,8,8,8,9,8,8,8,8,8,2,8,7,2],
       [-3,5,8,4,8,0,8,6,3,-2,3,5,8,0,8,4,8,6,-4],
       [2,8,8,8,8,2,8,8,8,2,8,8,8,2,8,8,8,8,2],
       [2,8,6,3,3,-1,3,5,8,2,8,6,3,-1,3,3,5,8,2],
       [2,8,8,8,8,8,8,8,8,2,8,8,8,8,8,8,8,8,2],
       [-7,3,3,3,3,3,3,3,3,-1,3,3,3,3,3,3,3,3,-6]]

def ktora_kratka(pix):
    return (pix//30)
    

class pacman:

    def __init__(self, surface, x_coord, y_coord, direction):
        self.surface = surface
        self.x = x_coord
        self.y = y_coord
        self.image = pygame.image.load('pacman_dir2_2.png')
        self.direction = direction
        return

    def update(self, x_amount=3,y_amount=3): # 1-lewo 2-prawo 3-gora 4-dol 0-nic
        if(self.direction == 0):
            self.surface.blit(self.image, (self.x, self.y))
            
        elif(self.direction == 1):
            if(mapa[ktora_kratka(player.y)][ktora_kratka(player.x-3)]>6 and mapa[ktora_kratka(player.y+29)][ktora_kratka(player.x-3)]>6):
                self.x -= x_amount
            self.surface.blit(self.image, (self.x, self.y))

                
        elif(self.direction == 2):
            if(mapa[ktora_kratka(self.y)][ktora_kratka(self.x+29+3)]>6 and mapa[ktora_kratka(self.y+29)][ktora_kratka(self.x+29+3)]>6):
                self.x += x_amount
            self.surface.blit(self.image, (self.x, self.y))

                
        elif(self.direction == 3):
            if(mapa[ktora_kratka(self.y-3)][ktora_kratka(self.x)]>6 and mapa[ktora_kratka(self.y-3)][ktora_kratka(self.x+29)]>6):
                self.y -= y_amount
            self.surface.blit(self.image, (self.x, self.y))

                
        elif(self.direction == 4):
            if(mapa[ktora_kratka(self.y+29+3)][ktora_kratka(self.x)]>6 and mapa[ktora_kratka(self.y+29+3)][ktora_kratka(self.x+29)]>6):
                self.y += y_amount
            self.surface.blit(self.image, (self.x, self.y))

        return

player = pacman(screen,270,450,0)
sekw = 1

def animacja_pacman(sekw):
    
    if(player.direction==1):
        if(sekw==1):
            player.image=pygame.image.load('pacman_dir1_1.png')
        elif(sekw==2):
            player.image=pygame.image.load('pacman_dir1_2.png')
        elif(sekw==3):
            player.image=pygame.image.load('pacman_dir1_3.png')
        elif(sekw==4):
            player.image=pygame.image.load('pacman_dir1_2.png')
    
    elif(player.direction==2):
        if(sekw==1):
            player.image=pygame.image.load('pacman_dir2_1.png')
        elif(sekw==2):
            player.image=pygame.image.load('pacman_dir2_2.png')
        elif(sekw==3):
            player.image=pygame.image.load('pacman_dir2_3.png')
        elif(sekw==4):
            player.image=pygame.image.load('pacman_dir2_2.png')
            
    elif(player.direction==3):
        if(sekw==1):
            player.image=pygame.image.load('pacman_dir3_1.png')
        elif(sekw==2):
            player.image=pygame.image.load('pacman_dir3_2.png')
        elif(sekw==3):
            player.image=pygame.image.load('pacman_dir3_3.png')
        elif(sekw==4):
            player.image=pygame.image.load('pacman_dir3_2.png')
            
    elif(player.direction==4):
        if(sekw==1):
            player.image=pygame.image.load('pacman_dir4_1.png')
        elif(sekw==2):
            player.image=pygame.image.load('pacman_dir4_2.png')
        elif(sekw==3):
            player.image=pygame.image.load('pacman_dir4_3.png')
        elif(sekw==4):
            player.image=pygame.image.load('pacman_dir4_2.png')
    
    sekw+=1
    if(sekw==5):
        sekw=1
        
    return sekw


def losowy_duch():
    los_ducha = random.randrange(4)
    if(los_ducha==0):
        return pygame.image.load('ghost1.png')
    if(los_ducha==1):
        return pygame.image.load('ghost2.png') 
    if(los_ducha==2):
        return pygame.image.load('ghost3.png') 
    if(los_ducha==3):
        return pygame.image.load('ghost4.png') 

class ghost:

    def __init__(self, surface, x_coord, y_coord):
        self.surface = surface
        self.x = x_coord
        self.y = y_coord
        self.image = losowy_duch()
        self.direction = 1
        self.lewo=False
        self.prawo=False
        self.gora=False
        self.dol=False
        self.ile_rozdrozy=0
        self.poprzedni_kierunek=1
        return

    def update(self, x_amount=3,y_amount=3): # 1-lewo 2-prawo 3-gora 4-dol 0-nic
        
        # w ktora strone moze sie ruszyc
        if(mapa[ktora_kratka(self.y)][ktora_kratka(self.x-3)]>6 and mapa[ktora_kratka(self.y+29)][ktora_kratka(self.x-3)]>6):
            self.lewo=True
            self.ile_rozdrozy+=1
           
        if(mapa[ktora_kratka(self.y)][ktora_kratka(self.x+29+3)]>6 and mapa[ktora_kratka(self.y+29)][ktora_kratka(self.x+29+3)]>6):
            self.prawo=True
            self.ile_rozdrozy+=1
           
        if(mapa[ktora_kratka(self.y-3)][ktora_kratka(self.x)]>6 and mapa[ktora_kratka(self.y-3)][ktora_kratka(self.x+29)]>6):
            self.gora=True
            self.ile_rozdrozy+=1

        if(mapa[ktora_kratka(self.y+29+3)][ktora_kratka(self.x)]>6 and mapa[ktora_kratka(self.y+29+3)][ktora_kratka(self.x+29)]>6):
            self.dol=True
            self.ile_rozdrozy+=1

        # decyzja w ktora strone      
        if(self.poprzedni_kierunek==1): # lewo
            if(self.ile_rozdrozy>1):
                losowana = random.randrange(self.ile_rozdrozy-1)
                zmienna = 0
                if(self.lewo==True):
                    if(zmienna == losowana):
                        self.direction=1
                    zmienna+=1
                if(self.gora==True):
                    if(zmienna == losowana):
                        self.direction=3
                    zmienna+=1
                if(self.dol==True):
                    if(zmienna == losowana):
                        self.direction=4
            
        if(self.poprzedni_kierunek==2): # prawo
            if(self.ile_rozdrozy>1):
                losowana = random.randrange(self.ile_rozdrozy-1)
                zmienna = 0
                if(self.prawo==True):
                    if(zmienna == losowana):
                        self.direction=2
                    zmienna+=1
                if(self.gora==True):
                    if(zmienna == losowana):
                        self.direction=3
                    zmienna+=1
                if(self.dol==True):
                    if(zmienna == losowana):
                        self.direction=4
                        
        if(self.poprzedni_kierunek==3): # gora
            if(self.ile_rozdrozy>1):
                losowana = random.randrange(self.ile_rozdrozy-1)
                zmienna = 0
                if(self.lewo==True):
                    if(zmienna == losowana):
                        self.direction=1
                    zmienna+=1
                if(self.prawo==True):
                    if(zmienna == losowana):
                        self.direction=2
                    zmienna+=1
                if(self.gora==True):
                    if(zmienna == losowana):
                        self.direction=3
                    zmienna+=1
                        
        if(self.poprzedni_kierunek==4): # dol
            if(self.ile_rozdrozy>1):
                losowana = random.randrange((self.ile_rozdrozy-1))
                zmienna = 0
                if(self.lewo==True):
                    if(zmienna == losowana):
                        self.direction=1
                    zmienna+=1
                if(self.prawo==True):
                    if(zmienna == losowana):
                        self.direction=2
                    zmienna+=1
                if(self.dol==True):
                    if(zmienna == losowana):
                        self.direction=4
                        
        if(self.ile_rozdrozy==1):
            if(self.lewo==True):
                self.direction=1
            elif(self.prawo==True):
                self.direction=2
            elif(self.gora==True):
                self.direction=3
            elif(self.dol==True):
                self.direction=4


        # poruszenie sie
        if(self.direction==1):
            self.x -= x_amount
            self.surface.blit(self.image, (self.x, self.y))
           
        elif(self.direction==2):
            self.x += x_amount
            self.surface.blit(self.image, (self.x, self.y))

                
        elif(self.direction==3):
            self.y -= y_amount
            self.surface.blit(self.image, (self.x, self.y))

        elif(self.direction==4):
            self.y += y_amount
            self.surface.blit(self.image, (self.x, self.y))
        
        # ustawaienie pomocniczych zmiennych
        self.poprzedni_kierunek=self.direction
        self.lewo=False
        self.prawo=False
        self.gora=False
        self.dol=False
        self.ile_rozdrozy=0
        return

enemy_array = []


def input(events):
   for event in events:
      if event.type == pygame.QUIT:
         sys.exit(0) #terminate()
      elif event.type == KEYDOWN:
          if(event.key == K_ESCAPE):
              sys.exit(0)



czcionka = pygame.font.SysFont("dejavusans", 17) #napisy

wynik = "Wynik:"
wynik_render = czcionka.render(wynik, 1, (250, 250, 250))

punkty_wynik="0"
punkty_wynik_render = czcionka.render(punkty_wynik, 1, (250, 250, 250))

poziom="Poziom 1"
poziom_render = czcionka.render(poziom, 1, (250, 250, 250))

najlepszy="Najlepszy wynik: "
najlepszy_render = czcionka.render(najlepszy, 1, (250, 250, 250))

najlepszy_wynik="0"
najlepszy_wynik_render = czcionka.render(najlepszy_wynik, 1, (250, 250, 250))

jeszcze_raz="Nacisnij spacje zeby zagrac jeszcze raz!"
jeszcze_raz_render = czcionka.render(jeszcze_raz, 1, (250, 250, 250))

wyjscie=" Nacisnij ecsape zeby wyjsc z gry!"
wyjscie_render = czcionka.render(wyjscie, 1, (250, 250, 250))

if(True):
    while(True):
        for poziomik in range(2):
               
            wygrana=True
            kolizja=False
            zjadanko=False
            czas_zjadanka=0
            czas_animacji=0
            mruganie=0
            blue_or_white=1
            player.x=270
            player.y=450
            player.direction=0
            sekw=1
            restart=True
            
            if(poziomik==0): # poziomy
                mapa =[[-8,3,3,3,3,3,3,3,3,-2,3,3,3,3,3,3,3,3,-5], #2-sciana_pion 3-sciana_poziom 7-bonus 8-punkt 9-puste 
                   [2,8,8,8,8,8,8,8,8,2,8,8,8,8,8,8,8,8,2], # 0-czapka 4-buty 5-p 6-l -1-3gora -2-3dol -3-3prawa -4-3lewa
                   [2,7,6,5,8,6,3,5,8,4,8,6,3,5,8,6,5,7,2],
                   [2,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,2],
                   [2,8,6,5,8,0,8,6,3,-2,3,5,8,0,8,6,5,8,2],
                   [2,8,8,8,8,2,8,8,8,2,8,8,8,2,8,8,8,8,2],
                   [-7,3,3,-5,8,-3,3,5,9,4,9,6,3,-4,8,-8,3,3,-6],
                   [9,9,9,2,8,2,9,9,9,9,9,9,9,2,8,2,9,9,9],
                   [-8,3,3,-6,8,4,9,-8,5,9,6,-5,9,4,8,-7,3,3,-5],
                   [2,9,9,9,8,9,9,2,9,9,9,2,9,9,8,9,9,9,2],
                   [-7,3,3,-5,8,0,9,-7,3,3,3,-6,9,0,8,-8,3,3,-6],
                   [9,9,9,2,8,2,9,9,9,9,9,9,9,2,8,2,9,9,9],
                   [-8,3,3,-6,8,4,9,6,3,-2,3,5,9,4,8,-7,3,3,-5],
                   [2,8,8,8,8,8,8,8,8,2,8,8,8,8,8,8,8,8,2],
                   [2,8,6,-5,8,6,3,5,8,4,8,6,3,5,8,-8,5,8,2],
                   [2,7,8,2,8,8,8,8,8,9,8,8,8,8,8,2,8,7,2],
                   [-3,5,8,4,8,0,8,6,3,-2,3,5,8,0,8,4,8,6,-4],
                   [2,8,8,8,8,2,8,8,8,2,8,8,8,2,8,8,8,8,2],
                   [2,8,6,3,3,-1,3,5,8,2,8,6,3,-1,3,3,5,8,2],
                   [2,8,8,8,8,8,8,8,8,2,8,8,8,8,8,8,8,8,2],
                   [-7,3,3,3,3,3,3,3,3,-1,3,3,3,3,3,3,3,3,-6]]
                poziom="Poziom 1"
                poziom_render = czcionka.render(poziom, 1, (250, 250, 250))
                punkty_wynik="0"
            else:
                mapa =[[-8,3,3,3,3,3,3,3,3,-2,3,3,3,3,3,3,3,3,-5], #2-sciana_pion 3-sciana_poziom 7-bonus 8-punkt 9-puste 
                   [2,8,8,8,8,8,8,8,8,2,8,8,8,8,8,8,8,8,2], # 0-czapka 4-buty 5-p 6-l -1-3gora -2-3dol -3-3prawa -4-3lewa
                   [2,7,6,5,8,6,3,5,8,4,8,6,3,5,8,6,5,7,2],
                   [2,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,2],
                  [-3,3,5, 8,6,-5,8, 6,3,-2,3, 5,8,-8,5, 8,6,3,-4],
                   [2,8,8, 8,8, 2,8, 8,8, 2,8, 8,8, 2,8, 8,8,8,2],
                   [2,8,6,-5,8,-3,3, 5,9, 4,9, 6,3,-4,8,-8,5,8,2],
                   [2,8,8, 2,8, 2,9, 9,9, 9,9, 9,9, 2,8, 2,8,8,2],
                   [2,8,6,-6,8, 4,9,-8,5, 9,6,-5,9, 4,8,-7,5,8,2],
                   [2,8,8, 8,8, 9,9, 2,9, 9,9, 2,9, 9,8, 8,8,8,2],
                   [2,8,6,-5,8, 0,9,-7,3, 3,3,-6,9, 0,8,-8,5,8,2],
                   [2,8,8, 2,8, 2,9, 9,9, 9,9, 9,9, 2,8, 2,8,8,2],
                   [2,8,6,-6,8, 4,9, 6,3,-2,3, 5,9, 4,8,-7,5,8,2],
                   [2,8,8, 8,8, 8,8,8,8,2,8,8,8,8,8,8,8,8,2],
                   [2,8,6,-5,8,-8,3,5,8, 4,8,6,3,-5,8,-8,5,8,2],
                   [2,8,7, 2,8, 2,8,8,8, 9,8,8,8, 2,8, 2,7,8,2],
                   [2,8,6,-6,8, 4,8,6,3,-2,3,5,8, 4,8,-7,5,8,2],
                   [2,8,8, 8,8, 8,8,8,8, 2,8,8,8, 8,8, 8,8,8,2],
                   [2,8,6, 5,8, 6,3,5,8, 2,8,6,3, 5,8, 6,5,8,2],
                   [2,8,8,8,8,8,8,8,8,2,8,8,8,8,8,8,8,8,2],
                   [-7,3,3,3,3,3,3,3,3,-1,3,3,3,3,3,3,3,3,-6]]
                
                poziom="Poziom 2"
                poziom_render = czcionka.render(poziom, 1, (250, 250, 250))
            

        
        
            # działaj aż do przerwania
            while(True):
               clock.tick(60) #FPS
               window.fill((0,0,0)) # czyszczenie planszy
               
               screen.blit(wynik_render, (10,630))
               punkty_wynik_render = czcionka.render(punkty_wynik, 1, (250, 250, 250))
               screen.blit(punkty_wynik_render, (80,630))
               
               screen.blit(poziom_render, (480,630))
               
               
               if(zjadanko==True): #odliczanie czasu kiedy mozna zjadac przeciwnikow
                   czas_zjadanka+=1
                   if(czas_zjadanka>240):
                       czas_zjadanka=0
                       zjadanko=False
                       for enemy in enemy_array:
                           enemy.image = losowy_duch() 
               
               if(restart==True):
                   for enemy in enemy_array:
                           enemy.image = losowy_duch() 
                   
               for i in range(21): # rysowanie planszy
                   for j in range(19):
                       if(mapa[i][j]==7):
                           screen.blit(bonus, (j*30,i*30)) #bonus
                       elif(mapa[i][j]==8):
                           screen.blit(punkt, (j*30,i*30))
                           wygrana=False
                       elif(mapa[i][j]==2):
                           screen.blit(sciana_zwykla_pion, (j*30,i*30))
                       elif(mapa[i][j]==3):
                           screen.blit(sciana_zwykla_poziom, (j*30,i*30))
                       elif(mapa[i][j]==0):
                           screen.blit(sciana_czapka, (j*30,i*30))
                       elif(mapa[i][j]==4):
                           screen.blit(sciana_buty, (j*30,i*30))
                       elif(mapa[i][j]==5):
                           screen.blit(sciana_p, (j*30,i*30))
                       elif(mapa[i][j]==6):
                           screen.blit(sciana_l, (j*30,i*30))
                       elif(mapa[i][j]==-1):
                           screen.blit(gora3, (j*30,i*30))
                       elif(mapa[i][j]==-2):
                           screen.blit(dol3, (j*30,i*30))
                       elif(mapa[i][j]==-3):
                           screen.blit(prawa3, (j*30,i*30))
                       elif(mapa[i][j]==-4):
                           screen.blit(lewa3, (j*30,i*30))
                       elif(mapa[i][j]==-5):
                           screen.blit(kolanko_pg, (j*30,i*30))
                       elif(mapa[i][j]==-6):
                           screen.blit(kolanko_pd, (j*30,i*30))
                       elif(mapa[i][j]==-7):
                           screen.blit(kolanko_ld, (j*30,i*30))
                       elif(mapa[i][j]==-8):
                           screen.blit(kolanko_lg, (j*30,i*30))
                           
               if(wygrana==True): # sprawdzenie czy wygrana
                   break;
                   
               if(len(enemy_array)<4): # czterech wrogow
                   miejsce =  random.randrange(3)
                   if(miejsce==0):
                       enemy = ghost(screen,240,270)
                   elif(miejsce==1):
                       enemy = ghost(screen,270,270)
                   elif(miejsce==2):
                       enemy = ghost(screen,300,270)
                       
                   enemy_array.append(enemy)
                 
                    
                   
               for enemy in enemy_array: #kolizje
                   if((player.x>=enemy.x and player.x<=(enemy.x+29)) or (player.x+29>=enemy.x and player.x+29<=(enemy.x+29))):
                       if((player.y>=enemy.y and player.y<=(enemy.y+29)) or (player.y+29>=enemy.y and player.y+29<=(enemy.y+29))):
                           if(zjadanko==False):
                               kolizja=True
                           else:
                               punkty_wynik = str(int(punkty_wynik)+100)
                               enemy_array.remove(enemy)
                           
               if(kolizja==True): #zakonczenie gry po kolizji
                   break;
                   
                       
               if(mapa[player.y//30][player.x//30]==8): # usuwanie punktow z mapy
                   mapa[player.y//30][player.x//30]=9
                   punkty_wynik = str(int(punkty_wynik)+10)
               elif(mapa[player.y//30][player.x//30]==7):
                   zjadanko=True
                   czas_zjadanka=0
                   mapa[player.y//30][player.x//30]=9
                   
                   
               if (pygame.key.get_pressed()[pygame.K_LEFT] != 0): # poruszanie pacman'a
                   if(mapa[ktora_kratka(player.y)][ktora_kratka(player.x-3)]>6 and mapa[ktora_kratka(player.y+29)][ktora_kratka(player.x-3)]>6):
                       player.direction=1
               elif (pygame.key.get_pressed()[pygame.K_RIGHT] != 0):
                   if(mapa[ktora_kratka(player.y)][ktora_kratka(player.x+29+3)]>6 and mapa[ktora_kratka(player.y+29)][ktora_kratka(player.x+29+3)]>6):
                       player.direction=2
               elif (pygame.key.get_pressed()[pygame.K_UP] != 0):
                   if(mapa[ktora_kratka(player.y-3)][ktora_kratka(player.x)]>6 and mapa[ktora_kratka(player.y-3)][ktora_kratka(player.x+29)]>6):
                       player.direction=3
               elif (pygame.key.get_pressed()[pygame.K_DOWN] != 0):
                   if(mapa[ktora_kratka(player.y+29+3)][ktora_kratka(player.x)]>6 and mapa[ktora_kratka(player.y+29+3)][ktora_kratka(player.x+29)]>6):
                       player.direction=4
                           
               input(pygame.event.get())            
               player.update()
               
               
               
               czas_animacji+=1
               if(czas_animacji>7):
                   sekw=animacja_pacman(sekw)
                   czas_animacji=0
            
               
               for enemy in enemy_array: #aktualizacja duchow
                   if(zjadanko==True):
                       if(czas_zjadanka>150):
                           mruganie+=1
                           if(mruganie>60):
                               blue_or_white*=-1
                               mruganie=0
                           if(blue_or_white==1):
                               enemy.image = pygame.image.load('ghost_dead2.png')
                           else:
                               enemy.image = pygame.image.load('ghost_dead.png')
                           
                       else:
                           enemy.image = pygame.image.load('ghost_dead.png')
                           
                   enemy.update()
                   if(restart==True):
                       miejsce =  random.randrange(3)
                       if(miejsce==0):
                           enemy.x=240
                           enemy.y=270
                       elif(miejsce==1):
                           enemy.x=270
                           enemy.y=270
                       elif(miejsce==2):
                           enemy.x=300
                           enemy.y=270
                   
               restart=False
               pygame.display.update() 
               window.fill((0,0,0))
               wygrana=True
             
            again=False
            while(True): # scena z zagraj jeszczce raz
                clock.tick(60) #FPS
                if(wygrana==True and poziomik==0):
                    break
                
                window.fill((0,0,0))
                
                
                
                events=pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        sys.exit(0) #terminate()
                    elif event.type == KEYDOWN:
                        if(event.key == K_ESCAPE):
                            sys.exit(0)
                        if(event.key == K_SPACE):
                            again=True
    
                if(again==True):
                    break
                
                wynik_render = czcionka.render(wynik, 1, (250, 250, 250))
                screen.blit(wynik_render, (240,100))

                punkty_wynik_render = czcionka.render(punkty_wynik, 1, (250, 250, 250))
                screen.blit(punkty_wynik_render, (305,100))
                
                screen.blit(najlepszy_render, (205,200))
                screen.blit(najlepszy_wynik_render, (350,200))
                screen.blit(jeszcze_raz_render, (125,450))
                screen.blit(wyjscie_render, (145,520))
                
                
                
                pygame.display.update()

            if(int(punkty_wynik)>int(najlepszy_wynik) and wygrana==False): #bicie rekordu
                najlepszy_wynik=punkty_wynik
                najlepszy_wynik_render = czcionka.render(najlepszy_wynik, 1, (250, 250, 250))
                
            if(int(punkty_wynik)>int(najlepszy_wynik) and wygrana==True and poziomik==1): #bicie rekordu
                najlepszy_wynik=punkty_wynik
                najlepszy_wynik_render = czcionka.render(najlepszy_wynik, 1, (250, 250, 250))
   
            if(wygrana==False):
                break
            
   