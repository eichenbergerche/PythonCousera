x = 3
y = 2
if x<y:
    print(x, "es menor que", y)
elif x>y:
    print(x, "es mayor que", y)
else:
    print(x, "es igual a", y)

a=3
b=14
if a==b:
    print(a, "es igual a", b)
else:
    if a<b:
        print(a, "es menor que", b)
    else:
        print(a, "es mayor que", b)    

x=1+4*3+8/2*4+5**2
if x%2==0:
    print(x+1)
else:
    print(x+2)

def fib(n):
    """Escribe la serie de Fibonacci hasta n."""
    a, b=0,1
    while a<n:
        print(a,end=" ")
        a, b=b,a+b
        print()
fib(2000)
f=fib
def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
f100

f(100)
fib(0)
print(fib(0))


