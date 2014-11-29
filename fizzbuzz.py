#!/usr/bin/python
b=raw_input()
c=b.split()
x=int(c[0])
y=int(c[1])
a = []
for i in range(x,y+1):
    if i%15==0:
	a.append("FizzBuzz")
    elif i%3==0:
	a.append("Fizz")
    elif i%5==0:
	a.append("Buzz")
    else:
	a.append(str(i))
print " ".join(a)