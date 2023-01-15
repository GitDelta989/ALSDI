import speech_recognition
import pygame
from deep_translator import single_detection

W_W = 480
W_H = 170
W_C = (20, 20, 30)

screen = pygame.display.set_mode((W_W, W_H))
pygame.display.set_caption('ALSDI - The Language Speech Detecting AI')
ALSDILogo = pygame.image.load('ALSDILogo.png')
pygame.display.set_icon(ALSDILogo)

pygame.init()

F_T = pygame.font.Font('ITCKabelStdMedium.ttf', 24)
F_S = pygame.font.Font('ITCKabelStdBook.ttf', 48)
F_L = pygame.font.Font('ITCKabelStdBold.ttf', 48)

text = "???"
language = "--"

recognizer = speech_recognition.Recognizer()

def updateScreen():
    screen.fill(W_C)
    title1 = pygame.font.Font.render(F_T, "What you said:", True, (255, 255, 255))
    screen.blit(title1, dest=(10, 10))
    textdisplay = pygame.font.Font.render(F_S, text, True, (255, 255, 255))
    screen.blit(textdisplay, dest=(10, 35))
    title2 = pygame.font.Font.render(F_T, "The language you spoke:", True, (255, 255, 255))
    screen.blit(title2, dest=(10, 90))
    languagedisplay = pygame.font.Font.render(F_L, language, True, (255, 255, 255))
    screen.blit(languagedisplay, dest=(10, 115))
    pygame.display.flip()

while True:
    try:
        with speech_recognition.Microphone() as mic:
            updateScreen()
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()
            language = single_detection(text, api_key='2a9bf660a04eba4b77125642ad4a1c81')
    except:
        pass