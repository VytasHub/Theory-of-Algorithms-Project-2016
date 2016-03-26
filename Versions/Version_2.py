# Vytas Vaiciulis
# G00304571
# Date


import time
import hashlib



mapDctionary = dict()
mapFilter = dict()
mapFilter = dict()
asciiValueInt = 0
asciiValueConcat = 0
finalResult = []


print("Preprocessing...")
with open("bigDictionary.txt") as f:
	dictionary = [line.strip() for line in f]# Brackets , its list comprahension
f.close()



for word in dictionary:
	ascii = str(sum(ord(ch) for ch in word))
	hash_object = hashlib.md5(ascii.encode())
	mapDctionary.update({word:hash_object.hexdigest()})
	

	
def proccesWord():
	word = "auctinoed"
	ascii = str(sum(ord(ch) for ch in word))
	hash_object = hashlib.md5(ascii.encode())
	hash_object.hexdigest()
	sortword = sorted(word)
	asciiConcat = [str(ord(ch)) for ch in sortword]
	asciiValueConcat = "".join(asciiConcat)
	
	return hash_object.hexdigest(),int(asciiValueConcat)
	
asciiValueInt, asciiValueConcat = proccesWord()



def	checAnagrams():	
	for word,count in mapDctionary.items():
		
		if count == asciiValueInt:
			
			sortword = sorted(word)
			ascii = [str(ord(ch)) for ch in sortword] 
			asciiJoined = "".join(ascii)
			mapFilter.update({word:int(asciiJoined)})
	return mapFilter


	
mapFilter = checAnagrams()

	

def	checAnagrams():	
	for word, count in mapFilter.items():
		if count == asciiValueConcat:
			print(word)
	
checAnagrams()








