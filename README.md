# Theory-of-Algorithms-Project-2016

### Vytas Vaiciulis
#### G00304571

# Countdown Letters Game Solver
Insert introduction here.
This gist is just an example of how you might layout your submission.
Please change it to suit your needs.

## Background
The first task I completed as part of this project was to Google "countdown letters game solver".
Google gave me two relevant results on the first page, these are [Cool Project name][2] and [Cool Solver][3].

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
![alt text](https://github.com/RonanC/Countdown-Letters-Game-Solver/blob/master/resources/v2-standby-top.png "v2-standby-top")
![](https://github.com/VytasHub/Theory-of-Algorithms-Project-2016/blob/master/pics/ascii.png "ascii")
![](https://github.com/VytasHub/Theory-of-Algorithms-Project-2016/blob/master/pics/ascii.png)



```python
mapDctionary.update({word:sum(ord(ch) for ch in word)})
```

## Python script Version_3
My Version_1 uses from itertools import permutations. First it reads in bigDictionary.txt and strip of unwanted characters readIn(). Than gets all permutation of a give words it’s a 9 letter word so there will be 362880 getPermutations().Afther that it compares all permutations 362 880 against the bigDictionary.txt which contains 235 886.So the amount of checking up to do is mind blowing          85 598 311 680.Once that is done the result is ran throw printer() which is recursive function that only prints out the highest  word permutation.
This most important part as it uses contains so it finds all the sub permutations too.

```python
for angram in allPermu:
		if angram in dictionary:
```

Previously it looks like this:
```python
# Note that the following snippet of code was adapted from
# the Stack Overflow post available here: http://www.so.com/post/123
import nothing
```
That didn't work too well, so I changed it.

## Preprocessing
My script does a lot of preprocessing, which only needs to be run once.
Once the preprocessing is done we can run the game solver again and again without that overhead.

## Efficiency
Here's some stuff about how efficient my code is, including an analysis of how many calculations my algorithm requires.

## Results
My script runs very quickly, and certainly within the 30 seconds allowed in the Coutdown letters game.


## References
[1]: http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/
[2]: http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/
[3]: http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/
