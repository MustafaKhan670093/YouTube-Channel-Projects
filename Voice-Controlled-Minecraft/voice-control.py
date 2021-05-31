'''
author: Mustafa Khan
date: Sunday, May 30th, 2021
youtube video: https://youtu.be/j_EaB1UJEp0
summary: I used the speech_recognition library to capture audio from my microphone, then using 
the  google speech to text recognition module I extracted phrases from the audio, and finally, 
substrings identified in the phrases corresponded to certain key presses conducted by the 
pyautogui library. All of that just to play minecraft with my voice.
'''

import pyautogui as pg
import time
import speech_recognition as sr
import subprocess

CMD = '''
on run argv
  display notification (item 2 of argv) with title (item 1 of argv)
end run
'''

#helper function for identifying mouse positions
def reportMousePosition(seconds = 10):
    for i in range(0, seconds):
        print(pg.positio())
        time.sleep(1)

#function used to create the notifications as shown in the youtube video. this was necessary
#to make sure the program didn't crash and to also help viewers gauge what's being picked up
def notify(title, text):
  subprocess.call(['osascript', '-e', CMD, title, text])

#these progression of holding down and letting go of a key was used repeatedly so I made it
#into its own function that passes in a key and performs the same action to that key
def holdKey(key, seconds):
    pg.keyDown(key)
    time.sleep(seconds)
    pg.keyUp(key)

#Note regarding imports:
#in order to use speech_recognition I needed to pip install pocketsphinx
#in order for pocketsphinx to work, I had to fix a bug using the comments found here: https://github.com/bambocher/pocketsphinx-python/issues/28
#finally, that change didn't work entirely either so I had to edit the setup files using this link: https://github.com/bambocher/pocketsphinx-python/issues/67
#kindof a mess tbh and I hope the devs working on this repo fix the issue but I guess they haven't yet.


#initializing some things
program_run = True
cur_key = ''
cur_mouse = ' '
r = sr.Recognizer()

#if the user puts their mouse to top left corner, program stops
pg.FAILSAFE = True

#this is the main program
while program_run:
    #taking in a microphone input and doing some preprocessing on it
    with sr.Microphone(device_index = 0) as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source, phrase_time_limit=2) #phrase_time_limit=1
    if pg.press('fn'):
        #an alternative escape key in case the failsafe defined on line 44 doesn't work
        program_run = False
    #I put everything into a try block to avoid any errors from stopping the program
    try:
        notify("Listening", "...")
        phrase = r.recognize_google(audio) #using google's free speech to text recognition api here 
        phrase = phrase.lower() #turning everything into lower case 
        notify("Captured Message", phrase)
        print("Google Speech Recognition thinks you said " + phrase) 

        #next, everything here is just different commands I defined. I tried to come up with words that did not sound similar to each other.
        #some weren't used that much in game while others were used a lot. feel free to add functionality, change the phrases or use the code.
        #just send people over to my vid :) or give some form of attribution
        if "stop" in phrase:
            phrase = ' '
            pg.keyUp(cur_key)
            if cur_mouse != ' ':
                pg.mouseUp(button=cur_mouse)
                cur_mouse = ' '
        elif "jump" in phrase:
            pg.keyDown('space')
        elif "stump" in phrase: #stop + jump = stump lol
            pg.keyUp('space')
        elif "crouch" in phrase: 
            pg.keyDown('shift')
        elif "stand" in phrase:
            pg.keyUp('shift')
        elif "walk" in phrase:
            cur_key = 'w'
            phrase = ' '
            pg.keyDown('w')
        elif "run" in phrase:
            cur_key = 'w'
            phrase = ' '
            holdKey('w', 0)
            pg.keyDown('w')
        elif "jog" in phrase:
            cur_key = 'w'
            phrase = ' '
            holdKey('w', 5)
        elif "forward" in phrase:
            cur_key = 'w'
            phrase = ' '
            holdKey('w', 1)
        elif "inventory" in phrase:
            cur_key = 'e'
            phrase = ' '
            pg.press('e')
        elif "back" in phrase:
            cur_key = 's'
            phrase = ' '
            pg.keyDown('s')
        elif "sack" in phrase: #slowly + back
            cur_key = 's'
            phrase = ' '
            holdKey('s', 1)
        elif "rocket" in phrase:
            holdKey('w', 0)
            pg.keyDown('w')
            holdKey('space', 0)
            pg.keyUp('w') 
        elif "block" in phrase:
            for i in range(0,10):
                pg.keyDown('s')
                time.sleep(1)
                pg.mouseDown(button='right')
                pg.mouseUp(button='right')
        elif "tower" in phrase:
            for i in range(0,10):
                holdKey('space', 0.1)
                pg.mouseDown(button='right')
                pg.mouseUp(button='right')
        elif "clutch" in phrase:
            holdKey('w', 0) 
            holdKey('space', 0.1)
            for i in range(0,15):
                pg.mouseDown(button='right')
                pg.mouseUp(button='right')
        elif "right" in phrase:
            cur_key = 'd'
            phrase = ' '
            pg.keyDown('d')
        elif "left" in phrase:
            cur_key = 'a'
            phrase = ' '
            pg.keyDown('a')
        elif "mine" in phrase:
            pg.mouseDown(button='left')
            cur_mouse = 'left'
        elif "pick" in phrase:
            pg.mouseDown(button='left')
            cur_mouse = 'left'
            pg.mouseUp(button='left')
        elif "attack" in phrase:
            cur_mouse = 'left'
            for i in range(0,15):
                pg.mouseDown(button='left')
                time.sleep(1)
                pg.mouseUp(button='left')
        elif "place" in phrase:
            cur_mouse = 'right'
            pg.mouseDown(button='right')
        elif "shoot" in phrase:
            cur_mouse = 'right'
            pg.mouseDown(button='right')
            time.sleep(2.5)
            pg.mouseUp(button='right')
        elif "use" in phrase:
            pg.mouseDown(button='right')
            time.sleep(0.1)
            pg.mouseUp(button='right')
        elif "1" in phrase or "one" in phrase:
            holdKey('1', 1)
        elif "2" in phrase or "two" in phrase:
            holdKey('2', 1)
        elif "3" in phrase or "three" in phrase:
            holdKey('3', 1)
        elif "4" in phrase or "four" in phrase:
            holdKey('4', 1)
        elif "5" in phrase or "five" in phrase:
            holdKey('5', 1)
        elif "6" in phrase or "six" in phrase:
            holdKey('6', 1)
        elif "7" in phrase or "seven" in phrase:
            holdKey('7', 1)
        elif "8" in phrase or "eight" in phrase:
            holdKey('8', 1)
        elif "9" in phrase or "nine" in phrase:
            holdKey('9', 1)
        elif "coordinates" in phrase:
            holdKey('f3', 8)
        else:
            print("No meaningful input")
            pass
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))