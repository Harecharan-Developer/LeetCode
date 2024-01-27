def cookies(k, A):
    counter=0
    for i in range (len(A)):
        A.sort()
        print("A=",A)
        if A[0]<k:
            x=A.pop(0)
            print(x)
        else:
            break
        y=A.pop(0)
        A.append(2*y+x)
        counter+=1
    
    return counter if all(i>=k for i in A) else -1

print("answer is ",cookies(7,[1, 2, 3, 9, 10, 12]   ))