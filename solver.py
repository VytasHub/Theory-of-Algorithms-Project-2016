# Vytas Vaiciulis
# G00304571
# Date

# use a set to get rid of duplicates
# generating random word use ASCI range values
# use md5  encryption
import time
import hashlib

mystring = "Preprocessing..."
# Assumes the default UTF-8
hash_object = hashlib.md5(mystring.encode())
print(hash_object.hexdigest())


mapDctionary = dict()
mapFilter = dict()
mapFilter = dict()
asciiValueInt = 0
asciiValueConcat = 0
finalResult = []

startPreProcces = time.time()
print("Preprocessing...")
with open("bigDictionary.txt") as f:
	#dictionary = f.readlines()
	dictionary = [line.strip() for line in f]# Brackets , its list comprahension
f.close()


#http://stackoverflow.com/questions/1024847/add-key-to-a-dictionary-in-python

#http://stackoverflow.com/questions/3944876/casting-an-int-to-a-string-in-python

#key value
for word in dictionary:

	ascii = str(sum(ord(ch) for ch in word))
	hash_object = hashlib.md5(ascii.encode())
	mapDctionary.update({word:hash_object.hexdigest()})
	
#print(mapDctionary)
	
endPreProcces = time.time()
print(endPreProcces - startPreProcces)
print("Preprocessing Done")
#http://stackoverflow.com/questions/25783460/python-changing-string-values-in-lists-into-ascii-values
	
startAngram = time.time()
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

print(asciiValueInt)
print(asciiValueConcat)



#http://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary

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
endAngram = time.time()
print(endAngram - startAngram )






# Comment out blok of code select ctrl + Q

