x=1
while x < 10:
    if x%2 == 0:
        print(str(x)+" is even")
    else:
        print(str(x)+" is odd")
    x +=1

i=0
while 1==1:
    print(i)
    i=i+1
    if i>=5:
        print("breaking")
        break
print("finished")

i=5
while True:
    print(i)
    i=i-1
    if i<=2:
        break