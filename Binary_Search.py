pos=-1
def binarysearch(lst,num):
	'''Function that returns True and index number of element if found else returns False and -1'''
	lst.sort()#any sort algorithm can be used
	print(lst)
	l=0
	u=len(lst)-1
	while l<= u:
		mid=(u+l)//2
		if  lst[mid] == num:
			global pos
			pos=mid
			return True,pos
			
			
		else:
			if  lst[mid] < num:
				l=mid+1
			else:
				u=mid-1
	return False,pos
a=[1,3,12,8,34,2]
s,index=binarysearch(a,102)	
print(s,'\nIndex:',index)

	