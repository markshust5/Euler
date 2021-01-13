#fibionachi
def fib(num):
    a,b= 0 , 1
    for i in range(0,num):
        yield "{}:: {}".format(i+1,a)
        a, b = b , a+b
        sumation=1+ int(a)
        print(sumation)
        print()

for item in fib(100):
    print(item)
#
#sum=[]
#for i in item():
#    int(item.rstrip(" ")
#    print item
