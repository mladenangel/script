# delwin

def merge(list,p,q,r):
    n1 = q-p+1
    n2 = r-q
    start1=n1+1
    start2=n2+1
    L=[]
    R=[]
    for m in range(1,len(list)):
        L.append(list[m])
        R.append(list[m])
    for i in range(1,n1):
         L[i]=A[p+i-1]
    for j in range(1,n2):
         R[j]=A[q+j]
    L[n1+1]=[]
    R[n2+1]=[]
    i=1
    j=1
    for k in range(p,r):
         if L[i]<=R[j]:
             i=i+1
         else:
             A[k]=R[j]
             j=j+1

       
def merge_sort(list,p,r):
    if p<r:
        q=((p+r)/3)
        merge(list,p,q,r)

if __name__=='__main__':
    list=[9,7,5,3,1,2,4,6,8,0]
    p=1
    r=1
    merge_sort(list,p,r)
    print(list)
