# Vytas Vaiciulis
# G00304571
# Date

# use a set to get rid of duplicates
# generating random word use ASCI range values
# use md5  encryption
import time






mapDctionary = dict()
mapFilter = dict()
mapFilter = dict()
asciiValueInt = 0
asciiValueConcat = 0
finalResult = []

startPreProcces = time.time()
print("Preprocessing...")
with open("wordlist.txt") as f:
	#dictionary = f.readlines()
	dictionary = [line.strip() for line in f]# Brackets , its list comprahension
f.close()


#http://stackoverflow.com/questions/1024847/add-key-to-a-dictionary-in-python

#http://stackoverflow.com/questions/3944876/casting-an-int-to-a-string-in-python

#key value
for word in dictionary:
	mapDctionary.update({word:sum(ord(ch) for ch in word)})
	
endPreProcces = time.time()
print(endPreProcces - startPreProcces)
print("Preprocessing Done")
#http://stackoverflow.com/questions/25783460/python-changing-string-values-in-lists-into-ascii-values
	
startAngram = time.time()
def proccesWord():
	word = "auctinoed"
	asciiValueInt = (sum(ord(ch) for ch in word))
	sortword = sorted(word)
	asciiConcat = [str(ord(ch)) for ch in sortword]
	asciiValueConcat = "".join(asciiConcat)
	
	return asciiValueInt,int(asciiValueConcat)
	
asciiValueInt, asciiValueConcat = proccesWord()

print(asciiValueInt)
print(asciiValueConcat)



#http://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary

def	checAnagrams():	
	for word, count in mapDctionary.items():
		if count == asciiValueInt:
			sortword = sorted(word)
			ascii = [str(ord(ch)) for ch in sortword] 
			asciiJoined = "".join(ascii)
			mapFilter.update({word:int(asciiJoined)})
	return mapFilter
	
	
mapFilter = checAnagrams()
print(mapFilter)	

def	checAnagrams():	
	for word, count in mapFilter.items():
		if count == asciiValueConcat:
			print(word)
	
checAnagrams()
endAngram = time.time()
print(endAngram - startAngram )



				
		#sortword = sorted(word)

		
#956 auctioned ,education

#print("Over")


# for word, count in mapFilter.items():
				# if count == asciiValueConcat:
					# print(word)






# Comment out blok of code select ctrl + Q
# def checker():
	# for angram in angramWords:
		# if angram in dictionary:
			# if len (angram) > 8:
				# print(angram)
			# elif len (angram) > 7:
				# print(angram)
			# elif len (angram) > 6:
				# print(angram)
			# elif len (angram) > 5:
				# print(angram)
			# elif len (angram) > 4:
				# print(angram)
			# elif len (angram) > 3:
				# print(angram)
			# elif len (angram) > 2:
				# print(angram)
				
				
				


	

#print(angramWords[2])
#print(dictionary[2])






  


# This function is just a wrapper that shows how my script works.
# It does the preprocessing, then creates a random list of letters, and finally runs the solver.


#Add words from txt to to a list , than order them by lenght 