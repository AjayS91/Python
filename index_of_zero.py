t=int(raw_input())
while t:
    t=t-1
    a=raw_input()
    b=a.split()
    x=[]
    for i in xrange(len(b)):
	x.append(int(b[i]))
    prev_prev_zero=0
    prev_zero=0
    max_count=0
    max_index=0
    curr=0
    for curr in xrange(len(x)):
	if x[curr]==0:
	    if curr-prev_prev_zero>max_count:
		max_count=curr-prev_prev_zero
		max_index=prev_zero
	    prev_prev_zero=prev_zero
	    prev_zero=curr
    if curr-prev_prev_zero>max_count:
	max_index=prev_zero
	max_count=curr-prev_prev_zero
    print max_count
    print max_index
	
