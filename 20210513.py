# Programmers 3진법 뒤집기 (level1)

def tri(n,i,res):
    x,y = n//i, n%i
    if x==0:
        res.append(y)
        return res
    res.append(y)
    return tri(x,i,res)

def solution(n):
    return sum([n*(3**i) for i,n in enumerate(tri(n,3,[])[::-1])])
 
# pass
