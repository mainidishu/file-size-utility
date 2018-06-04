import os
l=os.listdir(os.getcwd())
n=len(l)
max=0
for i in range(0,n):
	f=open(l[i],"ab+")
	f.write('1')
	t=f.tell()
	if t>max:
		max=t
		fn=f.name

max=max-2
print fn," is the biggest file with ",max," characters"

