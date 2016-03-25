# Vytas Vaiciulis
# G00304571
# Date


dictionary = [] #Creates dictionary list
angramWords = [] #Creats angramWords list


with open("wordlist.txt") as f: # Opens up wordlist.txt and saves in to the dictionary list
	dictionary = [line.strip() for line in f]# Brackets , its list comprahension , line.strip() strips of unvanted characters as /n if dont do this words wount match as they all contain /n 
print("Dictionary loaded...")	
	


 
def anagrams(letters): # Finds all angrams of a given word
  if len(letters) <=1: # Wount look for angrams if word is 0 or 1
    return letters
  else:
    anagramlist = []
    for anagram in anagrams(letters[1:]): # Finds all angrams by switching char around 1 at time
      for i in range(len(letters)):
        anagramlist.append(anagram[:i] + letters[0:1] + anagram[i:])
    return anagramlist
print("Angrams Found...")	

word = "auctieond" #Word used to find angrams
#auctioned


angramWords = anagrams(word) #Populates globaly decleared list with all the anagrams


print("Checking Angrams...")
def checker():						#Compares all Angrams agianst the dictionary
	for angram in angramWords:
		if angram in dictionary:
			if len (angram) > 8:    #Tryes to find longest angram first of lenght 9 and works its way down
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

# Other way checking Angrams agains the Dictionary
#for anagram in angramWords:
	#print("Outer " + anagram)
	#for word in dictionary:
		#print("Dictionary " + word)
		#if anagram == word:
			#print("Inner " + word)
print("Finished")

#To run script open cmd in folowing directory and type Version_1.py to run the script

