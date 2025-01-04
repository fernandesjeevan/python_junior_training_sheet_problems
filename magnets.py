# import sys
# reader = sys.stdin.read

# data = reader().split()
# num = data[0]

# magnets = int(data[2:])

# print(magnets)

num = int(input())
magnet_list = []
for i in range(num):
    magnet_list.append(i)

group = 0
for i in range(len(magnet_list)-1):
    if magnet_list[i] != magnet_list[i+1]:
        group = group+1