from gtts import gTTS
from random import shuffle
from os import system
from io import BytesIO
import inflect
import pygame
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
X = 400
Y = 400

def numGen(p):
    NumWords = []
    nums = list(range(1,91))
    shuffle(nums)
    for num in nums:
        word = p.number_to_words(num)
        NumWords.append(str(num)+" : "+word)
    return NumWords

def showTheNum(NumWords):
    i=0
    run = True
    while run:
        try:
            Wordd=NumWords[i]
        except IndexError:
            Wordd = "The End!"
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            Wordd = NumWords[i]
            i+=1
        if keys[pygame.K_LEFT]:
            if i > 0:
                i=i-1
                Wordd = NumWords[i]
            else:
                Wordd = NumWords[i]
        display_surface = pygame.display.set_mode((X,Y))
        pygame.display.set_caption('New Game')
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(Wordd,True, green, blue)
        textRect = text.get_rect()
        textRect.center = (X // 2, Y // 2)
        display_surface.fill(white)
        display_surface.blit(text, textRect)
        pygame.display.update()
    pygame.quit()



if __name__=='__main__':
    p = inflect.engine()
    pygame.init()
    NumWords = numGen(p)
    showTheNum(NumWords)
