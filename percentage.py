'''
Solution for the problem on hackerrank

https://www.hackerrank.com/contests/pythonista-practice-session/challenges/finding-the-percentage


'''

n=int(raw_input())
stu=[]
while n:
    n=n-1
    k={}
    l=raw_input()
    a=l.split()
    su=0.0
    #k[a[0]]=[a[i+1] for i in range(3) ]
    for i in range(3):
	su+=float(a[i+1])
    su=su/3
    k[a[0]]=su
    stu.append(k)
name=raw_input()

for names in stu:
    if name in names:
	print("%.2f"%names[name])