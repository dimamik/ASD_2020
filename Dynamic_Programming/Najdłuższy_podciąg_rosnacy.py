#Oblicz długość najdłuższego podciągu rosnącego (niekoniecznie spójnego)


def LIS(A):
    n=len(A)
    F=[1]*n
    P=[-1]*n
    for i in range(1,n):
        for j in range(i):
            if A[j]<A[i] and F[i]<F[j]+1:
                F[i]=F[j]+1
                P[i]=j
    return (max(F),F,P)

def printLIS(A,P,i):
    if P[i]>=0:
        printLIS(A,P,P[i])
    print(A[i])



print(printLIS(LIS([3,1,5,7,2,4,9,3,17,3]))

    


