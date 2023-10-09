list = [int (x) for x in input().split(' ')]
list2 = set()
for num in list:
    if num not in list2:
        list2.add(num)
        print("NO")
    else:
        print("YES")
            
    
    



