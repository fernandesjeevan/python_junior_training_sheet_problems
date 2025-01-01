string = input()
unique_string = ""
for s in string:
    if s not in unique_string:
        unique_string+= s
if len(unique_string)%2 ==0:
    print("CHAT WITH HER!")
 
else:
    print("IGNORE HIM!")