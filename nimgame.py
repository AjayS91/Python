#http://www.hackerearth.com/problem/algorithm/nim-game/description/
t=int(raw_input())
while t:
    t=t-1
    n=int(raw_input())
    ans=0
    for i in range(n):
	k=raw_input()
	j=k.split()
	x=long(j[0])
	m=long(j[1])
	a=(x*(x-1))/2
	b=((x+m-1)*(x+m))/2
	c=b-a
	ans=ans^c
	
    if ans:
	print 'bob'
    else:
	print 'alice'