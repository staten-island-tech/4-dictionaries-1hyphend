quarters = input(int())
first = input(int())
second=input(int())
third=input(int())
count = 0
while quarters > 0:
    quarters - 1
    first +=1
    count +=1
    if first == 35:
        first=0
        quarters +30
    
    quarters-1
    second+=1
    count+=1
    if second==100:
        second=0
        quarters += 60
    
    quarters -1
    third +=1
    count+=1
    if third == 10:
        third = 0
        quarters += 9

if quarters ==0:
    print(f"She plays {count} times before going broke.")