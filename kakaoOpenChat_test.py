def solution(record):
    answer = []
    user = {}

    for order in record :
        splitorder = order.split(' ')

        if splitorder[0] != 'Leave' :
            user[splitorder[1]] = splitorder[2]

    for order in record :
        splitorder = order.split(' ')
        if splitorder[0] == 'Enter':
            s = f'{user[splitorder[1]]}님이 들어왔습니다.'
            answer.append(s)

        elif splitorder[0] == 'Leave':
            s = f'{user[splitorder[1]]}님이 나갔습니다.'
            answer.append(s)

    
    return answer

print(solution([
    "Enter uid1234 Muzi", 
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan"
    ]))