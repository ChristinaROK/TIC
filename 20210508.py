# 2021 kakao internship 

# 2. manhattan distance
def isOkay(middleList: list, M)->int:
    
    for middle in middleList:
        middleNum=list(M)
        for idx in middle:
            middleNum=middleNum[idx]
        print(f"what is middle: {middleNum}")
        if middleNum!="X":
            return 0
    return 1

def isRoomOkay(x:list)->int:
    print(f"\n start: {x}")
    M = [[col for col in row] for row in x]
    
    people = []
    for i, row in enumerate(M):
        for j, col in enumerate(row):
            if col=="P":
                people.append((i,j))
    if len(people)==0:
        return 1
    
    print(f"people list: {people}")
    for i, one in enumerate(people):
        for other in people[i+1:]:
            dis = 0
            for x,y in zip(one,other):
                dis+=abs(x-y)
            
            if dis==1:
                return 0
            elif dis==2:
                print(one, other)
                for x,y in zip(one,other):
                    if x==y:
                        middle = [tuple((x+y)//2 for x,y in zip(one,other))]
                        print(f"same {middle}")
                        return isOkay(middle,M)
                middleList=[(one[0], other[1]), (other[0], one[1])]
                print(f"diff {middleList}")
                return isOkay(middleList,M)
    return 1

def solution(places):
    return [isRoomOkay(place) for place in places]
  
places = [["PPPPP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
solution(places)

# fail 오류 케이스 나옴 

# 3. go up down copy reverse
def solution(n,k,cmd):
    change = ["O"]*n
    delIdx = []
    
    for code in cmd:

        M = code.split()[0]

        if M == "D":
            k+=int(code.split()[1])
            print(f"go down k: {k}")
        elif M == "U":
            k-=int(code.split()[1])
            print(f"go up k: {k}")
        elif M == "C":
            n-=1
            print(f"delete n: {n}")
            offset = len([idx for idx in delIdx if idx<=k])
            change[k+offset] = "X"
            delIdx.append(k+offset)
            print(f"update change: {change}, delIdx: {delIdx}")
            k = min(n-1, k)
            print(f"k after delete: {k}")
        elif M == "Z":
            n+=1
            print(f"recover n: {n}")
            addidx = delIdx.pop()
            change[addidx] = "O"
            print(f"update change: {change}, delIdx: {delIdx}")
            if addidx<k:
                k+=1
            print(f"k after recovery: {k}")
    return "".join(change)
            

cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
#cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
solution(n=8,k=2,cmd=cmd)

# 오류 케이스 나옴
    
