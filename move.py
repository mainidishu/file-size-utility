#This program workss for files more than or equal to 5 bytes

import os
source='/home/deepanshu/Desktop/python/file check/'
dest='/home/deepanshu/Desktop/python/file check 1/'
l=os.listdir(source)
n=len(l)
for i in range(0,n):
	size=os.path.getsize(source + l[i])
	if size >= 5:
		os.rename(source + l[i],dest + l[i])

