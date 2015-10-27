def merge(a,l,r):
    i,j,k=0,0,0
    while (i<len(l) and j<len(r)):
        if l[i]<r[j]:
            a[k]=l[i]
            i+=1
        elif r[j]<l[i]:
            a[k]=r[j]
            j+=1
        k+=1
    while i<len(l):
        a[k]=l[i]
        i+=1
        k+=1
    while j<len(r):
        a[k]=r[j]
        k+=1
        j+=1

def merge_sort(a):
    n=len(a)
    if n<2:
        return
    mid=n//2
    l=a[:mid]
    r=a[mid:]
    merge_sort(l)
    merge_sort(r)
    merge(a,l,r)
    
if __name__ == '__main__':
    a=[2,4,1,6,8,5,3,7]
    merge_sort(a)
    print(a)
# assert merge_sort([2,4,1,6,8,5,3,7])