def solution(s):
    answer = 100
    sliceSize = 0
    sList = []
    count = 1
    slicedS = ''
        
    while sliceSize != len(s):   
        sliceSize += 1

        for i in range(0,len(s),sliceSize):
            slicedS = ''
            if i == 0:
                for j in range(sliceSize):
                    slicedS += s[i]
                sList.append(slicedS)
            else:
                for j in range(sliceSize):
                    slicedS += s[i]
                if sList[i-1] == slicedS:
                    sList.insert(i-1,count+1)
                else:
                    sList.append(slicedS)
            
           
        if answer > len(sList):
            answer = len(sList)
            print(sList)
        

        
    return answer


print(solution('aabbaccc'))

