# Vytas Vaiciulis
# G00304571
# Date


import random as rn

content = []

with open("wordlist.txt") as f:
	content = f.readlines()
	
print(content[2])

  
  
# gopup

#Go Pup
#Pug Op
  

  
# Taken almost verbatim from: http://www.quickperm.org/
def anagrams(word):
  p = list(range(len(word) + 1))
  i = 1
  # Word has to be mutable.
  word = list(word)
  
  while i < len(word):
    p[i] = p[i] - 1
    
    if i % 2 == 1:
      j = p[i]
    else:
      j = 0
    
    word[i], word[j] = word[j], word[i]
    
    i = 1
    while p[i] == 0:
      p[i] = i
      i = i + 1
    
    yield "".join(word)

    
word = "abcd"
i = 1

print("The anagrams of %s are:" % word)
print(word)
for anagram in anagrams(word):
  i = i + 1
  print(anagram)

print("There are %d anagrams in total." % i)

# This function is just a wrapper that shows how my script works.
# It does the preprocessing, then creates a random list of letters, and finally runs the solver.


#Add words from txt to to a list , than order them by lenght 