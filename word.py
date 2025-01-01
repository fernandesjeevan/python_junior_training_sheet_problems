word = input()
l = u = 0
for w in word:
    if w.islower():
        l = l+1
        
    else:
       
        u = u+1
print(word.lower()) if l>=u else print(word.upper())