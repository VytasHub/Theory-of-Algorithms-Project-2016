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
	


 

word = "auctioned"
        
#http://stackoverflow.com/questions/23159200/how-to-get-every-single-permutation-of-a-string
allPermu = ([''.join(w) for i in range(1, len(word)+1) for w in permutations(word, i)])
#perms = [''.join(p) for p in permutations(word)]

#http://stackoverflow.com/questions/53513/best-way-to-check-if-a-list-is-empty
print("Checking Angrams...")
def checker():						#Compares all Angrams agianst the dictionary
	for angram in allPermu:
		if angram in dictionary:
			if len (angram) == 9:    #Tryes to find longest angram first of lenght 9 and works its way down
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
checker()





def printer(num,checker): 
	if checker == 1:
		exit(0)
	for word in set(result):
		if len (word) == num:
			print(word)
			checker = 1
	return printer(num-1,checker)

printer(9,0)
	

# Other way checking Angrams agains the Dictionary
#for anagram in angramWords:
	#print("Outer " + anagram)
	#for word in dictionary:
		#print("Dictionary " + word)
		#if anagram == word:
			#print("Inner " + word)
print("Finished")

#To run script open cmd in folowing directory and type Version_1.py to run the script

