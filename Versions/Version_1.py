# Vytas Vaiciulis
# G00304571
# Date

from itertools import permutations
import random
import string


result = []

with open("wordlist.txt") as f: # Opens up wordlist.txt and saves in to the dictionary list
	dictionary = {line.strip() for line in f}#line.strip() strips of unvanted characters as /n if dont do this words wount match as they all contain /n 
f.close()
print("Dictionary loaded...")	
	


 

word = "auctieond"

#http://stackoverflow.com/questions/23159200/how-to-get-every-single-permutation-of-a-string
allPermu = ([''.join(p) for i in range(1, len(word)+1) for p in permutations(word, i)])
#perms = [''.join(p) for p in permutations(word)]


print("Checking Angrams...")
def checker():						#Compares all Angrams agianst the dictionary
	for angram in allPermu:
		if angram in dictionary:
			if len (angram) > 8:    #Tryes to find longest angram first of lenght 9 and works its way down
				result.append(angram)
			elif len (angram) > 7:
				result.append(angram)
			elif len (angram) > 6:
				result.append(angram)
			elif len (angram) > 5:	
				result.append(angram)
			elif len (angram) > 4:	
				result.append(angram)
			elif len (angram) > 3:	
				result.append(angram)
			elif len (angram) > 2:	
				result.append(angram)
checker()

print(result)
# Other way checking Angrams agains the Dictionary
#for anagram in angramWords:
	#print("Outer " + anagram)
	#for word in dictionary:
		#print("Dictionary " + word)
		#if anagram == word:
			#print("Inner " + word)
print("Finished")

#To run script open cmd in folowing directory and type Version_1.py to run the script

