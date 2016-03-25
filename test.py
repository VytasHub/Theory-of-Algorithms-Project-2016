
text = "auctioned"

#auctioned
#education
print(sum(ord(ch) for ch in text)) #Square brackestis important treats it as a list

ascii2 = [str(ord(ch)) for ch in text] 

ascii = [ord(ch) for text in text for ch in text]

print(ascii[2])
print(ascii2)

sortword = "".join(ascii2)


     
print(int(sortword))
