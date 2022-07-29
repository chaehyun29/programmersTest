import numpy as np
from math import ceil

def solution(w,h):
    answer = w*h

    if h/w == 1:
        return answer - w 

    elif h/w < 1:
        for n in range(w) :
            y = (h/w)*n
            if y - round(y) != 0 :
                answer -= 2
    elif h/w > 1:
        for n in range(h) :
            x = n/(h/w)
            if x - round(x) != 0 :
                answer -= 2

    return answer



print(solution(8,12))

'''
    for x in range(0,w,0.5):
        y = ceil((h/w)*x)
        line_y = (h/w)*x
        if x%1 == 0 :

        if y - round(y) != 0:
            round(y)


    return answer



print(solution(5,4))


    answer = w*h
    list = np.arange(w*h)
    list = list.reshape(w,h)

    for n in range(w*h):
        i = int(np.where(list == n)[0])
        j = int(np.where(list == n)[1])
        
        y1 = (h/w)*i
        y2 = (h/w)*(i+1)

        if j+1 > y1 and j < y2:
            answer -= 1
        
    return answer




    
    #대각선으로 자를 선
    x = 0
    y = (h/w)*x

    for i in range(w):
        for j in range(h):
            y1 = (h/w)*i
            y2 = (h/w)*(i+1)
            if j+1 > y1 and j < y2:
                answer -= 1
        
    return answer


    for i in range(0,w):
        for j in range(1,h+1):

            if()




           
            #점i,j 와 직선 hx + (-w)y + c = 0 사이의 거리 
            d = round(abs(h*i - w*j) / (h**2+w**2)**(1/2),3 )

            y = (h/w)*i
            val = round(2**(1/2),3)

            if j >y and d < val:
                answer -= 1
    return answer
'''
     

    
    

