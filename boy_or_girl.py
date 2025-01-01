# string = input()
# string = list(string)
# print(string)
# unique_string = set(string)

# # for s in string:
# #     if s not in unique_string:
# #         unique_string+= s
# if len(unique_string)%2 ==0:
#     print("CHAT WITH HER!")
 
# else:
#     print("IGNORE HIM!")


print("CHAT WITH HER!") if len(set(input()))%2 == 0 else print("IGNORE HIM!")