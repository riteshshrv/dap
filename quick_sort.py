def quick_sort(a, start, end):
	if start>=end:
		return
	pIndex=partition(a, start, end)
	quick_sort(a, start, pIndex-1)
	quick_sort(a, pIndex+1, end)

def partition(a, start, end):
	pivot=a[end]
	pIndex=start
	for i in range(start,end):
		if a[i]<=pivot:
			a[i],a[pIndex]=a[pIndex],a[i]
			pIndex+=1
	a[pIndex],a[end]=a[end],a[pIndex]
	return pIndex


if __name__=="__main__":
	a=[7,6,5,4,3,1,2,0]
	quick_sort(a,0,len(a))
	print(a)