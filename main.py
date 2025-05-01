import time, pygame, requests, sys  #remélhetőleg már vannak a 
from pygame import mixer            #célszemély gépén 

###############################################
#                                             #
# Elek Töhötöm Tamás - Csontrakéta            #
# ProjectKyiv in Pygame and other sus modules #
# 2025. 05. 01.                               #
# JEGYZETEK: kinn van githubon                #
#            nincs dokumentéció               #
#            meg van szépítve                 #   
#            próbál szabad szoftver lenni     #
#            nincsenek trágár szavak          #
#                                             #
###############################################

#(Ez már a program)

url = "https://kyiv.digital/storage/air-alert/stats.html" #modify to make errors

mixer.init()
mixer.music.load("siren.mp3") 
mixer.music.set_volume(0)
mixer.music.play(loops=-1) #végtelen cucc

pygame.init()
ablak = pygame.display.set_mode((1000, 600))
ablak.fill((0,0,0))
ablak.blit(pygame.image.load("loader.png"),(0,0))  
pygame.display.set_caption("---")
pygame.display.update()
time.sleep(5)

def szirenacheck():
    valasz = requests.get(url)
    valasz.raise_for_status() 

    tartalom = valasz.text
    sorok = tartalom.splitlines()

    if len(sorok) >= 98:
        kellosor = sorok[97]
        print(kellosor) #csak forráskóddal megy a cuccli
        if kellosor == "<td>🔴 Повітряна тривога!</td>": #checking lines
            mixer.music.set_volume(1) #Fun fact: mindig lejátszás alatt van, csak más hangerővel
        elif kellosor != "<td>🔴 Повітряна тривога!</td>":
            mixer.music.set_volume(0) #200 IQ moment
        else:
            print("HOGY") #Houston, we have a problem.
            pygame.quit()   
            sys.exit()
    else:
        print(f"sorok < 98")
        
   
running = True #modify this line for kaput

while running:
        ablak.fill((0,0,0))
        ablak.blit(pygame.image.load("background.png"),(0,0))  
        szirenacheck()
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
        
        pygame.display.update()