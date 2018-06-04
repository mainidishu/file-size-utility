#This program works for files more than or equal to 5 bytes

import os
source='/home/deepanshu/Desktop/python/file check/'	#Source and Destination path can be changed accordingly
dest='/home/deepanshu/Desktop/python/file check 1/'
l=os.listdir(source)					#Get the list of directories in the path
n=len(l)						#len() finds the number of files
for i in range(0,n):
	size=os.path.getsize(source + l[i])		#path.getsize() finds the size of files
	if size >= 5:
		os.rename(source + l[i],dest + l[i])	#rename() is used to move the file

