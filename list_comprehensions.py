'''
Solution for the problem on hackerrank

https://www.hackerrank.com/contests/pythonista-practice-session/challenges/list-comprehensions
'''

ans=[]
x=int(raw_input())
y=int(raw_input())
z=int(raw_input())
n=int(raw_input())
'''
for a in range(x+1):
    for b in range(y+1):
	for c in range(z+1):
	    if a+b+c != n:
		ans1=[a,b,c]
		ans.append(ans1)
'''
ans = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n ]
print ans