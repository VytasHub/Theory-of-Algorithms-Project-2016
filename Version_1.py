# Vytas Vaiciulis
# G00304571
# Date
from itertools import permutations
import random
import string


result = []



def readIn():
	with open("wordlist.txt") as f: # Opens up wordlist.txt and saves in to the dictionary list
		dictionary = {line.strip() for line in f}#line.strip() strips of unwanted characters as /n if don't do this words wont match as they all contain /n 
	f.close()
	print("Dictionary loaded...")
	return dictionary	
	
def getPermutations():
	allPermu = ([''.join(w) for i in range(1, len(word)+1) for w in permutations(word, i)]) # Finds all Permutations of a words using itertools
	return allPermu
#perms = [''.join(p) for p in permutations(word)]

word = "auctioned"# Word used to check angrams 
        
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

	


dictionary = readIn()

allPermu = getPermutations()

checker()

printer(9,0)

#To run script open cmd in following directory and type Version_1.py to run the script





