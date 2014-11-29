#!/usr/bin/python
a = []
a.append(0)
a.append(1)
def fib():
    for i in range(2,101):
	l=a[i-1]+a[i-2]
	a.append(l)
    
fib()
n=int(raw_input())
for i in range(n):
    k=int(raw_input())
    print a[k]