def merge(a,l,r):
    i=j=0
    while i+j<len(a):
        if j==len(r) or (i<len(l) and l[i]<r[j]):
            a[i+j]=l[i]
            i+=1
        else:
            a[i+j]=r[j]
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