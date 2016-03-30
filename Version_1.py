# Vytas Vaiciulis
# G00304571
# 28/03/2016
from itertools import permutations
import random
import string
import time

result = []

vowels = ['a','o','u','e','i'] # Creates list of vowels
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']# Creates list consonants

random.shuffle(vowels,random.random)#Shuffles the list to avoid duplication
random.shuffle(consonants,random.random)#Shuffles the list to avoid duplication

randomVowels = ''.join(vowels.pop() for i in range(3))#Pops one of the list avoids duplication
randomConsonants = ''.join(consonants.pop() for i in range(4))#Pops one of the list avoids duplication
randomChar = ''.join(random.choice(string.ascii_lowercase) for i in range(2))#Generates one random char

randomWord = randomVowels + randomConsonants + randomChar#Adds word together

#wordlist.txt
def readIn():
	with open("wordlist.txt") as f: # Opens up wordlist.txt and saves in to the dictionary list
		dictionary = {line.strip() for line in f}#line.strip() strips of unwanted characters as /n if don't do this words wont match as they all contain /n 
	f.close()
	return dictionary	
	
def getPermutations():
	allPermu = ([''.join(w) for i in range(1, len(randomWord)+1) for w in permutations(randomWord, i)]) # Finds all Permutations of a words using itertools
	return allPermu
#perms = [''.join(p) for p in permutations(randomWord)]


        
#http://stackoverflow.com/questions/23159200/how-to-get-every-single-permutation-of-a-string

def checker():						#Compares all Anagrams against the dictionary
	for angram in allPermu:
		if angram in dictionary:	#if in works as contains all anagrams are 9 letter words but some contain words within
			if len (angram) == 9:    #Tries to find longest anagram first of length 9 if match adds to a list and works its way down
				result.append(angram)
			if len (angram) == 8:
				result.append(angram)
			if len (angram) == 7:
				result.append(angram)
			if len (angram) == 6:	
				result.append(angram)
			if len (angram) == 5:	
				result.append(angram)
			if len (angram) == 4:	
				result.append(angram)
			if len (angram) == 3:	
				result.append(angram)
			if len (angram) == 2:	
				result.append(angram)


#If want to see all anagrams simply uncomment this line
#print(result)
		
def printer(num,checker): #This recursive function prints all words of length 9 if not recursively decreases words length by -1 and prints all words length 8
	if checker == 1:#Is used to see if there is already words printed if there are it exist as you only want to print words with same length
		exit(0)
	for word in set(result):#cast it as set to avoid duplicates
		if len (word) == num:
			print(word)
			checker = 1
	return printer(num-1,checker)#Recursive call

	
dictionary_start = time.time()
dictionary = readIn()
dictionary_end = time.time()
dictionary_time = (dictionary_end - dictionary_start)
print("Dictionary Loaded in:")
print(dictionary_time)


print("Generated random word:"+ randomWord)

look_start = time.time()

allPermu = getPermutations()
checker()

look_end = time.time()
look_time = (look_end - look_start)
print("Time to find Permutation:")
print(look_time)

print("Permutations Listed:")
printer(9,0)



#To run script open cmd in following directory and type Version_1.py to run the script





