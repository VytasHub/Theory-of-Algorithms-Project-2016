# Vytas Vaiciulis
# G00304571
# Date



mapDctionary = dict()
mapFilter = dict()
asciiValueInt = 0
asciiValueConcat = 0
finalResult = []


print("Preprocessing...")
with open("wordlist.txt") as f:
	#dictionary = f.readlines()
	dictionary = [line.strip() for line in f]# Brackets , its list comprahension
f.close()



for word in dictionary:
	mapDctionary.update({word:sum(ord(ch) for ch in word)})

	
def proccesWord():
	word = "auctinoed"
	asciiValueInt = (sum(ord(ch) for ch in word))
	sortword = sorted(word)
	asciiConcat = [str(ord(ch)) for ch in sortword]
	asciiValueConcat = "".join(asciiConcat)
	
	return asciiValueInt,int(asciiValueConcat)
	
asciiValueInt, asciiValueConcat = proccesWord()


def	checAnagrams():	
	for word, count in mapDctionary.items():
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




