'''
Solution of hackerearth problem

http://www.hackerearth.com/problem/algorithm/the-best-internet-browser-3/

'''

n=int(raw_input())
while n:
    n=n-1
    cnt=0
    st=raw_input()
    for i in range(len(st)-4):
	if st[i+4] not in 'aeiou':
	    cnt=cnt+1
    print str(cnt+1)+"/"+str(len(st))