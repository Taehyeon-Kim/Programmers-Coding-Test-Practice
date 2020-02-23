def solution(array, commands):
    answer = []
    for cmd in commands:
        answer.append(sorted(array[cmd[0]-1:cmd[1]])[cmd[2]-1])
    return answer