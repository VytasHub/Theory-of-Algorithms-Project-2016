# Theory-of-Algorithms-Project-2016

### Vytas Vaiciulis
#### G00304571

# Countdown Letters Game Solver
I have 3 versions of the program with Version_2 being most successful I describe each version and go in the most detail for Version_2 that’s where all my insight happened , and I describe how I solved the problem , and found a unique way to find anagrams without using any anagrams.

## Words list
My words list is in the file [wordslist.txt](wordslist.txt) in this repoistory/gist.
I got my words list from the [Oxford Learner's Dictionaries][1] website it contains 10 000 words also got the [bigDictionary.txt](bigDictionary.txt) it contains 235 886 words.

## Python script Version_1
My Version_1 uses from itertools import permutations. First it reads in bigDictionary.txt and strip of unwanted characters readIn(). Than gets all permutation of a give words it’s a 9 letter word so there will be 362880 getPermutations().Afther that it compares all permutations 362 880 against the bigDictionary.txt which contains 235 886.So the amount of checking up to do is mind blowing          85 598 311 680.Once that is done the result is ran throw printer() which is recursive function that only prints out the highest  word permutation.
This most important part as it uses contains so it finds all the sub permutations too.

```python
for angram in allPermu:
		if angram in dictionary:
```
This was my first attempt to crack the problem so I didn’t go to deep the other 2 attempts I got way more in depth into the problem and how to solve it.
## Python script Version_2

So first thing that happens is dictionary is read in from bigDictionary.txt
Than it stored in map.It stores word as key and the value is all character asci values added up together as follows: if word is abc than its key will be 97+98+99 = 294
![](https://github.com/VytasHub/Theory-of-Algorithms-Project-2016/blob/master/pics/ascii.png)
```python
mapDctionary.update({word:sum(ord(ch) for ch in word)})
```
Than we run method proccesWord() that first finds the total ASCII value and stores it in asciiValueInt as shown above for the dictionary words .And it also concatinates all the ASCCI values and stores that in asciiConcat variable.so as example words abc would have 979899 asciiConcat.The asciiValueInt and asciiConcat  will be used  to find word in the map.
```python
asciiConcat = [str(ord(ch)) for ch in sortword]
asciiValueConcat = "".join(asciiConcat)
```

Now we can run function checAnagrams() that finds anagrams so we will use asciiValueInt to look all words that contain same value which will find all the angrams but some anomolys will appear as some letter combination may give same ASCCi value so we will need some cleaning up to do.If we were to use word shuffled up version of word auctioned the angrams of auctioned are (auctioned,education) this what we would get:

```python
def	checAnagrams():	
	for word, count in mapDctionary.items():
		if count == asciiValueInt:)
```
![](https://github.com/VytasHub/Theory-of-Algorithms-Project-2016/blob/master/pics/anomolys.png)

As we can see bouth of our angrams are there that match the ASCII value but when dealing with big dictionaries other words will show as well that have same ASCII value.So here is where asciiConcat value will come in we will sort all of the words in this list and get asciiConcat value of all them and only take words out of the list that match our original word asciiConcat value.

![](https://github.com/VytasHub/Theory-of-Algorithms-Project-2016/blob/master/pics/output.png)

We can see that tere are 2 angrams in there that have same asciiConcat thats the ones we want and will get them runing this method:

```python
def	checAnagrams():	
	for word, count in mapFilter.items():
		if count == asciiValueConcat:
			print(word)
```
After this method we get our result 2 anagrams: auctioned, education

## Python script Version_3
This version is identical to Version_2 the only thing that’s different I am using md5 algorithm to hexdigest the ASCII value and stored as hash to see would it improve performance which show in performance section.

#### Version_3
```python
for word in dictionary:
	ascii = str(sum(ord(ch) for ch in word)) 
	hash_object = hashlib.md5(ascii.encode())
	mapDctionary.update({word:hash_object.hexdigest()})
```
```python
def proccesWord():
	word = "autcinoed"
	print("Word:"+ word)
	ascii = str(sum(ord(ch) for ch in word)) 
	hash_object = hashlib.md5(ascii.encode())
	hash_object.hexdigest()
```
#### Version_2
```python
for word in dictionary:
	mapDctionary.update({word:sum(ord(ch) for ch in word)})
```
```python
def proccesWord():
	word = "auctinoed"
	asciiValueInt = (sum(ord(ch) for ch in word))
```



## Preprocessing
Pre-processing is very important as it creates map with keys which can be looked up instantly. Pre-processing needs to be run once to map dictionary to the map. Pre-processing running time will depend on dictionary size. As we will see in Performance section as 2 dictionaries are used : wordslist.txt 10000 words and  bigDictionary.txt it contains 235 886 words.

## Efficiency
We can see the preformace of the programs using bigDictionary.txt which contains 235 886 words.

#### Version_1
![](https://github.com/VytasHub/Theory-of-Algorithms-Project-2016/blob/master/pics/Version_1b.png)
#### Version_2
![](https://github.com/VytasHub/Theory-of-Algorithms-Project-2016/blob/master/pics/Version_2b.png)
#### Version_3
![](https://github.com/VytasHub/Theory-of-Algorithms-Project-2016/blob/master/pics/Version_3b.png)

Here can see the preformace of the programs using wordslist.txt which contains 10 000 words.

#### Version_1
![](https://github.com/VytasHub/Theory-of-Algorithms-Project-2016/blob/master/pics/Version_3s.png)
#### Version_2
![](https://github.com/VytasHub/Theory-of-Algorithms-Project-2016/blob/master/pics/Version_3s.png)
#### Version_3
![](https://github.com/VytasHub/Theory-of-Algorithms-Project-2016/blob/master/pics/Version_3s.png)

## Results
My script runs very quickly, and certainly within the 30 seconds allowed in the Coutdown letters game.
As we can see all scripts run reasonably fast and all of the main work is done loading the dictionary, very big improvement is made when using maps maping key value pairs. In my Version_2 I used ASCII value as key to find the word and it was very fast using wordslist.txt it took 0.0019 which is 2 milliseconds and using hexdigest md5 it to a little bit more 0.003.

## References
[1]: http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/
[2]: http://stackoverflow.com/questions/1024847/add-key-to-a-dictionary-in-python/
[3]: http://stackoverflow.com/questions/3944876/casting-an-int-to-a-string-in-python/
[4]: http://stackoverflow.com/questions/25783460/python-changing-string-values-in-lists-into-ascii-values/
[5]: http://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary/
[6]: http://stackoverflow.com/questions/53513/best-way-to-check-if-a-list-is-empty/
[7]: http://stackoverflow.com/questions/23159200/how-to-get-every-single-permutation-of-a-string/
[8]: http://pythoncentral.io/hashing-strings-with-python/
[9]: https://docs.python.org/2/library/sets.html/









