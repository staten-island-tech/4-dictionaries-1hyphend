quarters = int(input(":  "))
first = int(input(":  "))
second=int(input(":  "))
third=int(input(":  "))
count = 0
while quarters > 0:
    print(count)
    first +=1
    quarters -=1
    count +=1
    
    if first == 35:
        quarters +30
        first=0

    second+=12
    quarters-=1
    count+=1

    if second==100:
        quarters += 60
        second=0

    third +=1
    quarters -=1
    count+=1

    if third == 10:
        quarters += 9
        third=0

print(f"She plays {count} times before going broke.")