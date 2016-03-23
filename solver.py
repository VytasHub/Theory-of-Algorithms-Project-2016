# Vytas Vaiciulis
# G00304571
# Date

# Import random to shuffle a list.
import random as rn

# This preprocessing function loads the words list file into a Python list.
def preprocessing(fname):
	with open(fname) as f:
		content = f.readlines()
	return [content]
  
  
preprocessing("wordlist.txt")
  
print("Hi")

print(preprocessing("wordlist.txt"))
  
# This is the function that actually checks the random letters for words.
def check(letters):
  while (letters):
    letters.pop()
  return []

# This function is just a wrapper that shows how my script works.
# It does the preprocessing, then creates a random list of letters, and finally runs the solver.


#Add words from txt to to a list , than order them by lenght 