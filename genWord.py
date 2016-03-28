import random
import string

vowels = ['a','o','u','e','i']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

random.shuffle(vowels,random.random)
random.shuffle(consonants,random.random)

randomVowels = ''.join(vowels.pop() for i in range(3))
randomConsonants = ''.join(consonants.pop() for i in range(4))
randomChar = ''.join(random.choice(string.ascii_lowercase) for i in range(2)) 

randomWord = randomVowels + randomConsonants + randomChar

print(randomWord)