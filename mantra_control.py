# -*- coding: utf-8 -*-
import pygame, numpy, random, time, platform, os, string, re, math
from pygame.constants import *
import numpy as np
from math import * 
pygame.init()
pygame.display.list_modes()

'''
        CONSTANTS
'''
# COLOURS
gray = (127, 127, 127) # backrgound colour
black = (0, 0, 0) # letter colour
white = (255, 255, 255)
green = (0, 255, 0) # colour for correct feedback
red = (255, 0, 0) # colour for incorrect feedback
bg = gray

# DIMENSIONS
W, H = 1024, 768 # screen dimention
res = (W, H) # resolution of screen
center_screen = (W/2, H/2) # center of screen
above_center_screen = (W/2, H/2-100)

# SPEED PARAMETERS
letPerSec = 1 # speed between each letter apparition (the lower the number, the longer the delay between each letter)
blipDur = 200 # duré d'affichage de chaque lettre - between 200 and 500 ms
postRespDur = 200 # delay after response has been made (ms)
feedbackDur = 500 # time between each trial

halflife=10000 # la moyenne tiré du distribution exponentielle (assure que tu ne peux pas prédire la longueure de la sequ) 
## --> Constant hazard rate (eliminate waiting bias) --> durée 

# DESIGN : After each block there is a pause. 
nBlocks = 3 # Total number of blocks in experiement
nTrials_per_block = 5 # Number of trials per block

# OUTPUT file variables/setup
os.makedirs('data', exist_ok=True)
manip='mantraLetters'
suj = input("Participant-e?: ")
data_directory='data'

TM =  time.strftime('%H%M') #time of the day (for data)
MM = time.strftime('%d%b%Y') #date of testing (for data)
output_file = data_directory + '/' + manip + '_' + suj + '.txt'
out = open(output_file, 'at')
print('manip', 'suj', 'TM', 'MM', 'trial', 'stims', 'lenStims', 'resp', 'corrResp', 'corrRespNum', 'respNum', 'rt', file=out)

## GLOBALS
fullscreen=False
refresh = 85
system = platform.system()
print('system:', system)
if system == 'Windows':    # tested with Windows 7
   os.environ['SDL_VIDEODRIVER'] = 'directx'
elif system == 'Darwin':   # tested with MacOS 10.5 and 10.6
   os.environ['SDL_VIDEODRIVER'] = 'Quartz'

if fullscreen:
    screen = pygame.display.set_mode(res, HWSURFACE | FULLSCREEN | DOUBLEBUF) # res = W,H
    strict=True
else:
    screen = pygame.display.set_mode(res)

pygame.mouse.set_visible(False)
police=pygame.font.SysFont("Arial", 80) #set font of stimuli

## FIXATION CROSS
x = police.render('+', 1, black)
rectx = x.get_rect()
rectx.center = center_screen

## QUESTION MARK (traget)
ptdint = police.render('?', 1, black)
rectptdint = ptdint.get_rect()
rectptdint.center = center_screen

## LETTER STIMULI
maxWidth = max([police.render(w.encode('utf-8'), 1, white).get_rect().width for w in string.ascii_uppercase])
maxHeight=  max([police.render(w.encode('utf-8'), 1, white).get_rect().height for w in string.ascii_uppercase])
marginX, marginYTop, marginYBottom = 150, 150, 200
ncols, nrows = 2, 2 

'''
        TRIAL SETUP
'''
# Define the Trial 

def doTrial (dur, nLetters, feedback=True):
    for i in range(nLetters):
        stim = lList[i%lenStims] # modulo pour faire un cycle --> stim is a triplet (stim 0 = stimulus, 1 = surface (liste de pixels), 2 = rectangle dimensions)
        screen.fill(bg) # efface surface screen (on met en background)
        screen.blit(stim[1], stim[2]) #bliter qq chose sur la surface screen = (quel parametre, ou)
        pygame.display.flip() # affiché sur écran
        pygame.time.wait(blipDur)
        screen.fill(bg) # background colour
        pygame.display.flip()
        pygame.time.wait(int(1000./letPerSec) - blipDur)
    t0 = pygame.time.get_ticks() # heur on fini de faire ces 3 series
    j = nLetters # index qui va prendre la suite de i (nLetter-1)

    while(pygame.time.get_ticks()-t0 < dur): # tant que l'heure (ticks en ms) depuis de commencement de pyGame - t0 est < a la durée
        j +=1 
        stim = lList[j%lenStims] # boucle comme dans la tete du participant
        screen.fill(bg)
        pygame.draw.circle(screen, black, center_screen, 25) # black dot in center of screen
        pygame.display.flip()
        pygame.time.wait(blipDur)
        screen.fill(bg)
        pygame.display.flip()
        pygame.time.wait(int(1000./letPerSec) - blipDur)
        corrResp = stim[0] # la bonne réponse , 1 of list of triplets stim 
        screen.fill(bg)
        pygame.display.flip()

    screen.fill(bg) # efface écran quand on sort de la boucle, après les pt noirs
    screen.blit(ptdint, rectptdint) # point d'interogration
    pygame.display.flip()
    done, t0 = False, pygame.time.get_ticks() # t0 commence temps en attendnat une reponses
    pygame.event.clear()

    
    while not done: # en attendnat rep du sujet
        ev = pygame.event.wait()
        if ev.type == KEYDOWN: # if key pressed
            if re.search(ev.unicode, string.ascii_lowercase): # if this key is a letter
                done, resp , rt = True, ev.unicode, pygame.time.get_ticks() - t0 # participants has given answern done = True
                screen.fill(bg)

    try:    
        respN = stims.index(resp.upper()) # essayer de trouver la lettre du partciipant dans stims
    except:
        respN = 'NA' # si la lettre n'y est pas, alors reponse c'est NA

    j = j%lenStims # reprends l'ordre du cycle pour savoir la bonne reponse 
    if respN == j: # si subject resp = bonne reponse alors correct response --> green
        acc, feedbackCol = 1, green
    else:
        acc, feedbackCol = 0, red # faux donc red

    print(j, respN) # print correct response, and number of letter that we respond or NA for letter that is not in serie


    screen.fill(bg)
    pygame.display.flip()
    pygame.time.wait(postRespDur)
    resp = resp.upper()
    response = police.render(resp, 1, feedbackCol) #  pour afficher la reponse du sujet a l'écran
    responseRect = response.get_rect()
    responseRect.center = center_screen # on centre la lettre
    screen.blit(response, responseRect) # on blip la reponse du particiipant

    pygame.display.flip()
    pygame.time.wait(feedbackDur)

    screen.fill(bg)
    pygame.display.flip()

    return(resp, corrResp, j, respN, rt) 


'''
        ENDING EXPERIEMENT
''' 
def endSession():
    endfont = pygame.font.SysFont("Arial", 50)
    p1Text = endfont.render("L'experience est fini!!", True, black)
    p1TextRec = p1Text.get_rect()
    p1TextRec.center = center_screen

    pauseText = endfont.render("Appuyer sur [ESPACE] pour tout fermer", True, black)
    pauseTextRec = pauseText.get_rect()
    done = False

    while not done:
        screen.fill(bg)
        screen.blit(pauseText, pauseTextRec)
        screen.blit(p1Text, p1TextRec)
        pygame.event.clear()
        pygame.display.flip()
        pygame.time.wait(feedbackDur)
        for ev in pygame.event.get():
            if ev.type == KEYDOWN and ev.key == K_SPACE:
                done = True
    out.close()
    pygame.quit()
    # sys.exit()


'''
        PAUSE BETWEEN BLOCKS
'''
def pause(nTrial):
    myfont = pygame.font.SysFont("Arial", 50)
    pauseText = myfont.render("Pause !", True, black)
    pauseTextRec = pauseText.get_rect()
    pauseTextRec.center = (above_center_screen)
    timeText = myfont.render("Moins de 30 secondes restantes", True, black)# not sure
    timeTextRec = timeText.get_rect()
    timeTextRec.center = center_screen # not sure

    t0 = pygame.time.get_ticks()
    while pygame.time.get_ticks() - t0 < 30000:
        timeElapsed = str(int(round((35 - (pygame.time.get_ticks() - t0)/1000) /10)*10))
##        if timeElapsed == "0": timeElapsed = "Moins de 10"
        timeText = myfont.render("Moins de " + timeElapsed + " secondes restantes", True, black)
        screen.fill(bg)
        screen.blit(pauseText, pauseTextRec)
        screen.blit(timeText, timeTextRec)
        pygame.display.flip()
        pygame.time.wait(feedbackDur)

    done = False
    pygame.event.clear()
    while not done:
        pauseText = myfont.render("Appuyer sur [ESPACE] pour reprendre", True, black)
        pauseTextRec = pauseText.get_rect()
        pauseTextRec.center = center_screen
        screen.fill(bg)
        screen.blit(pauseText, pauseTextRec)
        pygame.display.flip()
        pygame.time.wait(feedbackDur)
        for ev in pygame.event.get():
            if ev.type == KEYDOWN and ev.key == K_SPACE:done = True


'''
EXPERIEMENT BODY
'''
screen.fill(bg)
pygame.display.flip()
pygame.time.wait(1000)

block_list = np.arange(1,nBlocks,1) #not sure
block_number = 1

for nt in range(0,(nTrials_per_block*nBlocks)+1): # + 1 TRUE?? 

    print(nTrials_per_block*nBlocks,"end of trial:",nt)
    print(nTrials_per_block*nBlocks,"start of trial:",nt+1)
    #print("Block: " + str(block_list[block_number]))

    if nt >= (nTrials_per_block*nBlocks): # quand le trial number (i) excede le nombre total de trials (+1), alors stop exp
        print("total number of blocks: " + str(nBlocks))
        print("The experiment has ended")
        endSession()

    elif nt == (nTrials_per_block*block_number): # quand le trial number (i) == + 1 que le nombre total de trials dans un block (+1, car sinon le block s'arrete 1 trial trop tot)

        print("PAUSE PTN, block: " + str(block_number))
        pause(nt)
        block_number +=1 # not sure, maybe not inside the elif
        
    #else # not sure
    repetition = random.randint(3,4) # repetition of the list (how many times you see the list before dots) T1
    lenStims = random.randint(5,8) # longeure de la liste T2
    letters = string.ascii_uppercase
    stims = [letters[i] for i in random.sample(list(range(26)), lenStims)] # stimulus
    random.shuffle(stims)
    lettersRendered = [police.render(i, 1, black) for i in stims] # transforme chaque letter en une surface = Liste
    lettersRect = [i.get_rect() for i in lettersRendered] # rectangele qui entoure la lettre (pour centre au centre de l'écran en fonction de la taille de la lettre)
    
    for i in lettersRect: # centrer chaqsue rectangle sur centre de l'écran
        i.center = center_screen
    
    lList = list(zip(stims, lettersRendered, lettersRect)) # the list of stimuli : 
    
    nLetters = repetition * (lenStims) # présente 3 fois la sequ lettre = 3 repetition
    
    dur = 5000 # dot duration ! 5 secondes
    print(f"Duration of dots !! (not trial) = {dur}") # duration of dots

    screen.fill(bg) # repli la surface screen du background colour
    pygame.display.flip()
    
        ## We don't pass the list of stimuli to the doTrial function, because it is
        ## a global variable in the for loop...
    
    resp, corrResp, j, respN, rt = doTrial(dur, nLetters)
    
    print(manip, suj, TM, MM, nt+1, ''.join(stims), lenStims, resp, corrResp, j, respN, rt, file=out)
    pygame.time.wait(2500)
    screen.fill(bg)
    pygame.display.flip()

