# Vytas Vaiciulis
# G00304571
# Date

# use a set to get rid of duplicates
# generating random word use ASCI range values



import random as rn
import hashlib

dictionary = []
angramWords = []


with open("wordlist.txt") as f:
	#dictionary = f.readlines()
	dictionary = [line.strip() for line in f]# Brackets , its list comprahension 
	
	

#print(dictionary[2])
#print(hashlib.algorithms_available)

#hash_object = hashlib.md5(b'Hello World')
#print(hash_object.hexdigest())

#for x in dictionary:   
	#x = x.strip()
	#words.append(x)
  
  
# gopup

#Go Pup
#Pug Op
  
def anagrams(letters):
  if len(letters) <=1:
    return letters
  else:
    anagramlist = []
    for anagram in anagrams(letters[1:]):
      for i in range(len(letters)):
        anagramlist.append(anagram[:i] + letters[0:1] + anagram[i:])
    return anagramlist

word = "auctieond"
#auctioned
i = 0

#print("The anagrams of %s are:" % word)




angramWords = anagrams(word)
#print(angramWords)





def checker():
	for angram in angramWords:
		if angram in dictionary:
			if len (angram) > 8:
				print(angram)
			elif len (angram) > 7:
				print(angram)
			elif len (angram) > 6:
				print(angram)
			elif len (angram) > 5:
				print(angram)
			elif len (angram) > 4:
				print(angram)
			elif len (angram) > 3:
				print(angram)
			elif len (angram) > 2:
				print(angram)
				
				
				
checker()
#for anagram in angramWords:
	#print("Outer " + anagram)
	#for word in dictionary:
		#print("Dictionary " + word)
		#if anagram == word:
			#print("Inner " + word)
	
			
print("Over")

#print(angramWords[2])
#print(dictionary[2])






  


# This function is just a wrapper that shows how my script works.
# It does the preprocessing, then creates a random list of letters, and finally runs the solver.


#Add words from txt to to a list , than order them by lenght 