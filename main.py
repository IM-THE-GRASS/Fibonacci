num=1
lastnum=0
amount = int(input("how many to generate?:\n"))
for i in range(amount):
    print(num)
    num = num + lastnum
    lastnum = num - lastnum
    
