import random
import string


#According to the rules of scrabble
vowels = ['a','a','a','a','a','a','a','a','a','e','e','e','e','e','e','e','e','e','e','e','e','i','i','i','i','i','i','i','i','i','o','o','o','o','o','o','o','o','u','u','u','u',]
consonants = ['b','b','c','c','d','d','d','d','f','f','g','g','g','h','j','k','l','l','l','l','m','m','n','n','n','n','n','n','p','p','q','r','r','r','r','r','r','s','s','s','s','t','t','t','t','t','t','v','v','w','w','x','y','y','z']

random.shuffle(vowels,random.random)
random.shuffle(consonants,random.random)

randomVowels = ''.join(vowels.pop() for i in range(3))
randomConsonants = ''.join(consonants.pop() for i in range(4))
randomChar = ''.join(random.choice(string.ascii_lowercase) for i in range(2)) 

randomWord = randomVowels + randomConsonants + randomChar

print(randomWord)