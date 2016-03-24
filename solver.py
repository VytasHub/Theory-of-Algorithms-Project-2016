# Vytas Vaiciulis
# G00304571
# Date


import random as rn

dictionary = []
angramWords = []
words = []

with open("wordlist.txt") as f:
	#dictionary = f.readlines()
	dictionary = [line.strip() for line in f]
	

print(dictionary[2])


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

word = "gald"
i = 0

#print("The anagrams of %s are:" % word)




angramWords = anagrams(word)
print(angramWords)



for anagram in angramWords:
	#print("Outer " + anagram)
	for word in dictionary:
		#print("Dictionary " + word)
		if anagram == word:
			print("Inner " + word)
	
			
print("Over")

#print(angramWords[2])
#print(dictionary[2])






  


# This function is just a wrapper that shows how my script works.
# It does the preprocessing, then creates a random list of letters, and finally runs the solver.


#Add words from txt to to a list , than order them by lenght 