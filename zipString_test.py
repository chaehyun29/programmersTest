def solution(s):
    answer = 100
    sliceSize = 0

    count = 1
    slicedS = ''
        
    while sliceSize != len(s): 
        sList = []  
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
                    if type(sList[i-2])==type(0):
                        sList[i-2] += 1
                    else:
                        sList.insert(i-1,count+1)
                else:
                    sList.append(slicedS)
            
           
        if answer > len(sList):
            answer = len(sList)
            print(sList)
        
    return answer


print(solution('aabbaccc'))
print(solution('ababcdcdababcdcd'))
print(solution('abcabcdede'))
print(solution('abcabcabcabcdededededede'))
print(solution('xababcdcdababcdcd'))
print()

'''

"aabbaccc"	7
"ababcdcdababcdcd"	9
"abcabcdede"	8
"abcabcabcabcdededededede"	14
"xababcdcdababcdcd"	17



'''

