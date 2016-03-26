# Vytas Vaiciulis
# G00304571
# Date



mapDctionary = dict() #De-clearing dictionary
mapFilter = dict() #De-clearing dictionary
asciiValueInt = 0 #declaring int
asciiValueConcat = 0 #declaring int
finalResult = [] #De-clearing list


print("Preprocessing...")
with open("wordlist.txt") as f:#Read in bigDictiobary
	dictionary = [line.strip() for line in f]# Brackets , its list comprahension
f.close()#Close the file




for word in dictionary:
	mapDctionary.update({word:sum(ord(ch) for ch in word)})#Get total ascii value of all chars in the string and populates the map

	
def proccesWord():
	word = "auctinoed"
	asciiValueInt = (sum(ord(ch) for ch in word))#Get total ascii value of a string cast is as str
	sortword = sorted(word)#Sorts word
	asciiConcat = [str(ord(ch)) for ch in sortword]#Get ascii value of each char in string
	asciiValueConcat = "".join(asciiConcat)#Con-cats all ascii values abc would be 979695 its used later to identify anagram
	
	return asciiValueInt,int(asciiValueConcat)#Returns values
	
asciiValueInt, asciiValueConcat = proccesWord()# get 2 values back


def	checAnagrams():	
	for word, count in mapDctionary.items():#Loops throe the dictionary
		if count == asciiValueInt:#Checks if any of the hashes match
		#Note this will find the anagrams but it will also find some unwanted words too that are not anagrams
			sortword = sorted(word)# Sort word if match is found
			ascii = [str(ord(ch)) for ch in sortword] #Get ascii value of each char in string
			asciiJoined = "".join(ascii)#joins the together
			mapFilter.update({word:int(asciiJoined)})#Populates mini map to be filtered
	return mapFilter
	
	
mapFilter = checAnagrams()#Brings back the map
	

def	checAnagrams():		# Filter unwanted words out
	for word, count in mapFilter.items():#Loops throw the maps
		if count == asciiValueConcat:#We use asciiValueConcat to find our anagrams
			print(word)#Print them if they match
	
checAnagrams()#Calls Function




