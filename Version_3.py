# Vytas Vaiciulis
# G00304571
# 28/03/2016


import time# To time functions
import hashlib#Used for md5



mapDctionary = dict() #De-clearing dictionary
mapFilter = dict() #De-clearing dictionary
asciiValueInt = 0 #declaring int
asciiValueConcat = 0 #declaring int
finalResult = [] #De-clearing list


dictionary_start = time.time()
with open("wordlist.txt") as f:#Read in bigDictiobary
	dictionary = [line.strip() for line in f]# Brackets , its list comprehension
f.close()#Close the file



for word in dictionary:
	ascii = str(sum(ord(ch) for ch in word)) #Get total ascii value of all chars in the string
	hash_object = hashlib.md5(ascii.encode())#Used total ascii value to hash md5 hash to uniquely identify a string
	mapDctionary.update({word:hash_object.hexdigest()})#Populates map with word and related hash
	#Note could not use Key as hash as there are same hashes and keys seam to be need to be unique
dictionary_end = time.time()
dictionary_time = (dictionary_end - dictionary_start)
print("Dictionary Loaded in:")
print(dictionary_time)
	
def proccesWord():
	word = "autcinoed"
	print("Generated word:"+word)
	print("Word:"+ word)
	ascii = str(sum(ord(ch) for ch in word)) #Get total ascii value of a string cast is as str
	hash_object = hashlib.md5(ascii.encode())#Get the hash-code of string so we can run it against the map
	hash_object.hexdigest()#Does the hash
	sortword = sorted(word)#Sorts the words
	asciiConcat = [str(ord(ch)) for ch in sortword]#Get ascii value of each char in string
	asciiValueConcat = "".join(asciiConcat)#Con-cats all ascii values abc would be 979695 its used later to identify anagram
	
	return hash_object.hexdigest(),int(asciiValueConcat) #Returns values
	
asciiValueInt, asciiValueConcat = proccesWord() # get 2 values back



def	checAnagrams():	
	for word,count in mapDctionary.items():#Loops throe the dictionary
		
		if count == asciiValueInt: #Checks if any of the hashes match
		#Note this will find the anagrams but it will also find some unwanted words too that are not anagrams	
			sortword = sorted(word)# Sort word if match is found
			ascii = [str(ord(ch)) for ch in sortword] #Get ascii value of each char in string
			asciiJoined = "".join(ascii)#joins the together
			mapFilter.update({word:int(asciiJoined)})#Populates mini map to be filtered
	return mapFilter


	

look_start = time.time()	
mapFilter = checAnagrams()#Brings back the map

	

def	checAnagrams():	# Filter unwanted words out
	for word, count in mapFilter.items():#Loops throw the maps
		if count == asciiValueConcat:#We use asciiValueConcat to find our anagrams
			print(word)#Print them if they match



print("Permutations Listed:")
checAnagrams()#Calls Function
look_end = time.time()
look_time = (look_end - look_start)
print("Time to find Permutations:")
print(look_time)














