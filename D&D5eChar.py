# this is a program that allows someone to create a dnd fifth edition character and roll dice for their character after it is made -R
# importing random is for dice rolls, importing statistics is for math required later on, and importing time is to add little periods of time where the text pauses and lets the user read it before moving on. -R
import random
import statistics
import time

# this is foundational code that will be used for how the player selects a class, and also stores a hit die variable for later -R
hitDie = 0

classBarb = 1
classBard = 2
classCleric = 3
classDruid = 4
classFighter = 5
classMonk = 6
classPaladin = 7
classRanger = 8
classRogue = 9
classSorcerer = 10
classWarlock = 11
classWizard = 12

# these are just a few introductions to the program and how it works -R
print('Hello! And welcome to the Dungeons and Dragons 5th edition character folder, where you can host your own D&D character.')
time.sleep (4), print('This project is currently in beta, and only uses content from the original 2014 PHB, so consider that when crafting your character.')
time.sleep (5), print('Also, because it is currently in beta, multiclassing is not allowed.')
time.sleep (4), print('Other than that, feel free to create whatever you would like. The system will now boot up.')

# asks/stores the name for the character -R
time.sleep (5), print('*An old human man sits in a chair, reading from a book and smoking from his pipe. He stirs around in his rocking chair, before finally looking up to you...')
charName = time.sleep (8), input('Ah! Hello there, traveler... Tell me, what is your name?: | ')

# asks/stores character level, race, class -R
charLevel = time.sleep(2), int(input('Hmmm.... Yes, and what level are you at?: | '))

charRace = time.sleep(2), int(input('Wonderful... And what species - or lineage - do you derive from...?: | 1 for Human, 2 for Elf, 3 for Dwarf, 4, for Halfling, 5, for Dragonborn, 6 for Gnome, 7 for Half-Elf, 8 for Half-Orc, 9 for Tiefling'))

charClass = time.sleep(2), int(input('You are quite the interesting fellow... Tell me, what class grants you power? : | 1 for Barbarian, 2 for Bard, 3 for Cleric, 4 for Druid, 5 for Fighter, 6 for Monk, 7 for Paladin, 8 for Ranger, 9 for Rogue, 10 for Sorcerer, 11 for Warlock, 12 for Wizard'))

charSub = time.sleep(2), input('Can you be a bit more specific, friend? What is your subclass?: | ')

time.sleep(2), print('Hm.... Now then, I am going to ask you a series of questions, and I would like you to answer them honestly on a scale from 1 to 20... ')

charStr = time.sleep(2), int(input('How Strong do you believe you are?: | '))
charDex = time.sleep(2), int(input('How Dexterous are you?:  | '))
charCon = time.sleep(2), int(input('How much is your hearty Constitution?:  | '))
charInt = time.sleep(2), int(input('How would you weigh your booksmart Intelligence?:  | '))
charWis = time.sleep(2), int(input('How much Wisdom have you earned in your time?:  | '))
charCha = time.sleep(2), int(input('How much Charisma do you bring to the table?:  | '))

