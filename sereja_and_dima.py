num = int(input())

cards = list(map(int,input().split()))
length = len(cards)
high = length-1
low = 0
count =1
sereja = dima = 0 
while(low<=high):
    if count%2 ==1:
        if cards[low]>cards[high]:
            sereja += cards[low]
            low+=1

        else:
            sereja += cards[high]
            high = high-1


    else:
        if cards[low]>cards[high]:
            dima += cards[low]
            low+=1

            
        else:
            dima += cards[high]
            high = high-1 

    count+=1
print(sereja,dima)